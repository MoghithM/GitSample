import logging

#the level is set to warning by default:
#if we want info or debug logs you have to set the level lower
logging.basicConfig(level=logging.DEBUG)
logging.debug('Hello, Debug!')
logging.info('AHello, Info!')
logging.warning('Hello, Warning!')
logging.error('Hello, Error!')
logging.critical('Hello, Critical!')