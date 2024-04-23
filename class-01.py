# # NOTES:
# NOTSET = 0
# DEBUG = 10
# INFO = 20
# WARNING = 30
# ERROR = 40
# CRITICAL = 50

import logging


logging.basicConfig(level='DEBUG')
logger = logging.getLogger()

## logger.setLevel(level='DEBUG') 
## logging.DEBUG == 'DEBUG' == 10

print(logger)
print(logger.handlers)

logger.debug('This is a debug message')