import logging.config

from settings import logger_config


logger = logging.getLogger('app_logger')


def new_function(name):
    logger.debug('Entering new_function() ...', extra={'user_name': name})


def main():
    # logger.debug('Entering main() ...')
    pass


if __name__ == '__main__':
    logging.config.dictConfig(logger_config)

    names = ['john', 'mary', 'jack', 'oliver']

    for name in names:
        new_function(name)