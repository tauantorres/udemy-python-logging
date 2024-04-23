import logging
import logging.config

from settings import logger_config
from utils import get_response


logger = logging.getLogger('chuck_jokes')


def get_joke(response):
    joke = response.json()['value']
    print(joke)
    return joke


def main():
    url = 'https://api.chucknorris.io/jokes/random'

    logger.info('Getting a joke')

    joke = get_joke(get_response(url))

    logger.debug('main(), %s, %s', url, joke)
    logger.info('Got a joke')


if __name__ == '__main__':
    logging.config.dictConfig(logger_config)
    main()