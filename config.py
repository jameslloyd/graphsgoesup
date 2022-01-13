import os
class Config(object):
    APPNAME = 'GraphGoes'
    ENV = os.getenv("ENV") or "DEV" 
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    LOG_FORMAT = os.getenv("LOG_FORMAT") or '%(asctime)s - %(levelname)s - %(message)s \t - %(name)s (%(filename)s).%(funcName)s(%(lineno)d) ' # https://docs.python.org/3/howto/logging.html#changing-the-format-of-displayed-messages
    LOG_LEVEL = os.getenv("LOG_LEVEL") or 'INFO'
    PRICEWAITTIME = int(os.getenv('PRICEWAITTIME'))
    IEXAPIKEY = os.getenv('IEXAPIKEY')
    DISCORDWEBHOOK = os.getenv('DISCORDWEBHOOK')
    EMOJIUP = os.getenv('EMOJIUP') or ":thumbsup:"
    EMOJIDOWN = os.getenv('EMOJIDOWN') or ":thumbsdown:"
    EMOJIFLAT = os.getenv('EMOJIFLAT') or ":pause_button:"
    CURRENCY = os.getenv('CURRENCY') or "GBP"
    CRYPTO = os.getenv('CRYPTO') or "ETH"
    INFLUXTOKEN = os.getenv('INFLUXTOKEN')
    INFLUXORG = os.getenv('INFLUXORG')
    INFLUXBUCKET = os.getenv('INFLUXBUCKET')
    INFLUXHOST = os.getenv('INFLUXHOST')