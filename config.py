import os
class Config(object):
    ENV = os.getenv("ENV") or "DEV" 
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SKIPHIDDEN = True
    APPNAME = 'Graph Goes Up!'
    LOG_FORMAT = os.getenv("LOG_FORMAT") or '%(asctime)s - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(levelname)s - %(message)s' # https://docs.python.org/3/howto/logging.html#changing-the-format-of-displayed-messages
    LOG_LEVEL = os.getenv("LOG_LEVEL") or 'INFO'
    PRICEWAITTIME = int(os.getenv("PRICEWAITTIME"))
    IEXAPIKEY = os.getenv('IEXAPIKEY')
    DISCORDWEBHOOK = os.getenv('DISCORDWEBHOOK')