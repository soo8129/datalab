# 로거 객체 하나로 통일시 사용
import logging
import logging.handlers
import os

class Logger:
    def __init__(self):
        self.path = os.getcwd() + 'src/datalab_scraper/logs'
        self.name = "datalab_scraper"

        if not os.path.exists(self.path):
            os.makedirs(self.path)

        filehandler = logging.handlers.TimedRotatingFileHandler(filename='src/datalab_scraper/logs/datalab_logfile_', when='midnight', interval=1,
                                                        encoding='utf-8')
        filehandler.suffix = "%Y%m%d"
        filehandler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s : %(message)s'))
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.INFO)
        logger.addHandler(filehandler)

def test():
    logger_config = Logger()
    logger = logging.getLogger('datalab_scraper')
    logger.info('logger config test')

if __name__=='__main__':
    test()