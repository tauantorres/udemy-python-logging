import logging

import requests


API_TOKEN = '6042430097:AAFj-HHaM9Ap4_v-6NU-qRkCBTm4ijs2NGQ'
CHAT_ID = '180876400'


class NewFunctionFilter(logging.Filter):
    def filter(self, record):
        return record.user_name == 'oliver'


class Bot:
    def __init__(self, token=API_TOKEN):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{self.token}'

    def send_message(self, text, chat_id=CHAT_ID):
        data = dict(
            chat_id=chat_id,
            text=text
        )
        return requests.post(
            f'{self.base_url}/sendMessage',
            data=data,
            timeout=5
        )


class BotHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self._bot = Bot(token=API_TOKEN)

    def emit(self, record):
        message = self.format(record)
        self._bot.send_message(chat_id=CHAT_ID, text=message)



logger_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'std_format': {
            # 'format': '{asctime} - {levelname} - {name} - {message}',
            'format': '%(asctime)s - %(levelname)s - %(name)s - \
%(message)s - %(module)s: %(funcName)s: %(lineno)s'
            # 'style': '{'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'std_format',
            # 'filters': ['new_function_filter']
        },
        'rotating_files': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'std_format',
            'filename': 'debug.log',
            'maxBytes': 2000,
            'backupCount': 5
        },
        'bot_handler': {
            'class': 'settings.BotHandler',
            # 'bot': Bot(),
            'formatter': 'std_format',
            'level': 'DEBUG'
        }
    },
    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': ['console', 'bot_handler'],
            # 'propagate': False
        }
    },

    # 'filters': {
    #     'new_function_filter': {
    #         '()': NewFunctionFilter
    #     }
    # },
    # 'root': {} or '': {}
    # 'incremental': True

}