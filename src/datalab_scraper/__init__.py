import logging
import logging.handlers
from datalab_scraper import _datalab_scraper

def setup_logger():
    filehandler = logging.handlers.TimedRotatingFileHandler(filename='/src/datalab/logs/datalab_logfile_', when='midnight', interval=1,
                                                        encoding='utf-8')
    filehandler.suffix = "%Y%m%d"
    filehandler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s : %(message)s'))
    logger = logging.getLogger("datalab_scraper")
    logger.setLevel(logging.INFO)
    logger.addHandler(filehandler)


if __name__ == '__main__':
    setup_logger()
    _datalab_scraper()