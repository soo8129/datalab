import requests
import json
import time
import sys
import utils.logger_config
import logging

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/87.0.4280.66 "
    "Safari/537.36"
)

nav_url = "https://datalab.naver.com/shoppingInsight/getCategoryKeywordRank.naver"

def set_categories():
    #test용 카테고리
    genders = ['m', 'f']
    ages = ['10', '20', '30', '40', '50','60']
    cids = ['50000000', '50000001', '50000002', '50000003', '50000004', '50000005', '50000006', '50000007', '50000008', '50000009']

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
        elif req.status_code == 429:
            time.sleep(10)
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
            "KEYWORD": None
        }
        data = {
            "cid": cid,
            "timeUnit": "date",
            "startDate": "2023-09-22",
            "endDate": "2023-10-22",
            "age": age,
            "gender": gender,
            "page": 1,
            "count": 20
        }
        data = _datalab_scraper(data)

        if data:
            keywords = [rank['keyword'] for rank in data['ranks']]
            keyword_info["KEYWORD"] = keywords
            keyword_list.append(keyword_info)
        time.sleep(0.3)

    return keyword_list

def datalab_parser():
    logger = logging.getLogger("datalab_parser")
    categories = set_categories()
    keywords = datalab_keywords(categories)
    return keywords

# for test
if __name__ == '__main__':
    datalab_parser()
