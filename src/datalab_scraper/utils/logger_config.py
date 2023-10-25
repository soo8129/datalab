import logging
import logging.handlers

filehandler = logging.handlers.TimedRotatingFileHandler(filename='src/datalab_scraper/logs/datalab_logfile_', when='midnight', interval=1,
                                                    encoding='utf-8')
filehandler.suffix = "%Y%m%d"
filehandler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s : %(message)s'))
logger = logging.getLogger("datalab_scraper")
logger.setLevel(logging.INFO)
logger.addHandler(filehandler)