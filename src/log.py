import logging
from logging.config import dictConfig
# when the default logger isn't configure, it will only show 3 critical, error and warning, so we need to change
# the basic config. cn write to a generic file too. w: write, a: append , %(name): 
#logging.basicConfig(level=logging.DEBUG, format='%(levelname)-10s: %(name)-s :  %(message)s')
# (
#     level=logging.DEBUG, 
#     filename="logs/app_log.log", 
#     filemode="a", 
#     encoding="utf-8"
#     )

# dict config, define a dictionary with the needed configuration then pass it to dictConfig()
config = {
    'version': 1,
    "disable_existing_loggers": False,
    'formatters': {
        'standard': {
            "format": '%(levelname)-10s:%(name)s:%(message)s'
        }
    },
    'handlers': {
        'default': {
            'level': "DEBUG",
            'formatter': "standard",
            'class': "logging.StreamHandler",
            'stream': "ext://sys.stdout"
        },
        'file': {
            'level': "WARNING",
            'formatter': "standard",
            'class': "logging.FileHandler", #smtp, http look up the documentation
            'filename': "logs/fileH.log",
            'mode': "a"

        }
    },
    'loggers': {
        "": {# logger name
            'level': "DEBUG",
            'handlers': ['default','file'],
            'propagate': True
        },
         "API_LOGGER": {# logger name
            'level': "DEBUG",
            'handlers': ['default','file'],
            'propagate': False
        }
    }

}

dictConfig(config)
my_logger = logging.getLogger("API_LOGGER")

my_logger.critical("It's Critical")
my_logger.error("It's Error")
my_logger.warning("It's Warning")
my_logger.info("it's Info")
my_logger.debug("It's Debug")