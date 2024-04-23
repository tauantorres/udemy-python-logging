import logging


class MyClass:
    def __str__(self):
        raise Exception('Hello world')


mc = MyClass()


logger = logging.getLogger()

# message = 'Logging %s' % mc
# message = 'Logging {}'.format(mc)
# message = f'Logging {mc}'
logger.debug('Logging %s', mc)

