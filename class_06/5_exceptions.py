import logging
import logging.config

from settings import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')



def main():

    words = ['new house', 'icecream', 'car', 3]

    for word in words:
        try:
            print(word.split())
        except:
            # logger.debug('An exception was raised', exc_info=True)
            logger.exception('An exception was raised')


if __name__ == '__main__':
    main()