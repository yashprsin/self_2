import logging
import logging.config

logging.config.fileConfig('logging.conf')
#logging.config.dictConfig('logging.conf')
'''
Also used the file method
'''
logger = logging.getLogger('Simple Example')
logger.debug('this is a debug message')
