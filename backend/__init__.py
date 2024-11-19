import logging
import os

def set_logger():
    logger = logging.getLogger('logfile')
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    LOG_DIR = os.path.join(BASE_DIR, 'logs/')
    
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    hdlr = logging.FileHandler(os.path.join(LOG_DIR, 'logfile.log'))
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)

    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG) 

    return logger

logger = set_logger()

logger.info("If the issue persists, please contact our customer happiness team.")