import logging

import requests


logger = logging.getLogger('chuck_jokes.utils')


def get_response(url):
    try:
        response = requests.get(url, timeout=2)
        response.raise_for_status()

    except requests.exceptions.Timeout:
        logger.exception('Timeout')

    except requests.exceptions.ConnectionError:
        logger.exception('ConnectionError')

    except requests.exceptions.HttpError:
        logger.exception('HttpError')

    if response.status_code == 200:
        logger.info('Got %s status code', response.status_code)
    else:
        logger.warning(
            'Server responded with %s status code',
            response.status_code
        )

    return response

