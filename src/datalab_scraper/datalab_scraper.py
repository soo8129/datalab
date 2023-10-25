import utils.logger_config
import logging

from utils.NaverCategory import NaverCategory

def _datalab_scraper():
    logger = logging.getLogger("datalab_scraper")
    try:
        urls = NaverCategory().get_cid_list()
        logger.info(urls)
        # rank_data = 
        # db_insert(rank_data)
    except Exception as e:
        logger.error(e)

def main():
    _datalab_scraper()

if __name__ == '__main__':
    main()
