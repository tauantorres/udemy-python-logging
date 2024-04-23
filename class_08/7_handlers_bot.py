import logging.config


logger = logging.getLogger('app_logger')


def main():
    from settings import logger_config
    logging.config.dictConfig(logger_config)

    logger.debug('New message')


if __name__ == '__main__':
    main()