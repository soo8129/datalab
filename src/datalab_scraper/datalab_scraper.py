# logger 공통 객체
import utils.logger_config
import logging

from utils.NaverCategory import NaverCategory

def _datalab_scraper():
    logger = logging.getLogger("datalab_scraper")
    try:
        cid_list = NaverCategory().get_cid_list()
        # rank_data = networktest(cid_list)
        # db_insert(rank_data)
    except Exception as e:
        logger.error(e)
    return cid_list

# for test
def main():
    logger = logging.getLogger("datalab_scraper")
    cid_list = _datalab_scraper()
    for cid, cname in cid_list:
        logger.info(f"{cid} {cname}")
    logger.info(len(cid_list))

if __name__ == '__main__':
    main()
