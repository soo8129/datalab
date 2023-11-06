import requests
import json
import time
import sys
import logging
from datetime import datetime, timedelta
from utils.NaverCategory import NaverCategory


logger = logging.getLogger("datalab_scraper")

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/87.0.4280.66 "
    "Safari/537.36"
)

nav_url = "https://datalab.naver.com/shoppingInsight/getCategoryKeywordRank.naver"

date_info  = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

def set_categories(cids):
    genders = ['m', 'f']
    ages = ['10', '20', '30', '40', '50','60']
    categories = []
    for gender in genders:
        for age in ages:
            for cid in cids:
                categories.append((gender, age, cid))
    return categories

def _datalab_scraper(data):
    json_decoded = None
    try:
        req = requests.post(nav_url, data=data, headers={"user-agent": USER_AGENT, "Referer": nav_url, "Origin": "https://datalab.naver.com"})
        if req.status_code == 200:
            json_decoded = json.loads(req.text)
            logger.info(json_decoded)
        
        elif req.status_code == 429:
            time.sleep(60)
            json_decoded = _datalab_scraper(data)  # Retry
        
        return json_decoded
    
    except Exception as e:
        print(f'{e} error occur')
        return None

def datalab_keywords(categories):
    keyword_list = []
    for gender, age, cid in categories:
        keyword_info = {
            "CID": int(cid),
            "GENDER": gender,
            "AGE": int(age),
            "DATE": date_info,
            "KEYWORD": None
        }
        data = {
            "cid": cid,
            "timeUnit": "date",
            "startDate": date_info,
            "endDate": date_info,
            "age": age,
            "gender": gender,
            "page": 1,
            "count": 20
        }
        data = _datalab_scraper(data)

        if data:
            keywords = [{'rank': item['rank'], 'keyword': item['keyword']} for item in data['ranks']]
            if keywords:
                keyword_info["KEYWORD"] = keywords
                keyword_list.append(keyword_info)
                logger.info(keyword_info)
        time.sleep(0.3)
    return keyword_list

def datalab_parser(cid_list):
    logger = logging.getLogger("datalab_parser")
    cids = [item[0] for item in cid_list]
    categories = set_categories(cids)
    rank_data = datalab_keywords(categories)
    return rank_data

# for test
if __name__ == '__main__':
    cid_list = NaverCategory().get_cid_list()
    datalab_parser(cid_list)
