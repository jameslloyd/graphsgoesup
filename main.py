from config import Config
import os, time
import requests
from datetime import timedelta
from discord_webhook import DiscordWebhook, DiscordEmbed
import logging

Config = Config()

def get_crypto_price(symbol):
    api_key = Config.IEXAPIKEY
    api_url = f'https://cloud.iexapis.com/stable/crypto/{symbol}/price?token={api_key}'
    raw = requests.get(api_url).json()
    price = raw['price']
    return float(price)

def main():
    logging.basicConfig(format=Config.LOG_FORMAT ,level=Config.LOG_LEVEL)
    logging.info('Started application {} in {}'.format(Config.APPNAME, Config.ENV))
    while True:
        try: 
            oldprice
        except:
            oldprice = get_crypto_price('ethgbp')
            logging.info(f'Discord Webhook = {Config.DISCORDWEBHOOK}')
            logging.info('Current Price {} sleeping for {} seconds'.format(oldprice,Config.PRICEWAITTIME))
        time.sleep(Config.PRICEWAITTIME)
        newprice = get_crypto_price('ethgbp')
        increase = round((newprice - oldprice) / oldprice * 100,2)
        logging.info('New Price {} {}% change'.format(newprice,increase,2))
        if newprice == oldprice:
            title = 'Graph is flat'
            colour = 'FFBF00'
            icon = ':StockIndexUpicon:'
        elif newprice > oldprice:
            #graph goes up
            title = 'Graph goes up'
            colour = '00FF00'
            icon = ':meh:'
        else:
            #graph goes down
            title = 'Graph goes down'
            colour = 'FF0000'
            icon = ':StockIndexDownicon:'
        
        webhook = DiscordWebhook(url=Config.DISCORDWEBHOOK)
        embed = DiscordEmbed(title=title,description='{} {}% increase'.format(icon,increase), color=colour)
        embed.set_footer(text='{}% change'.format(increase))
        webhook.add_embed(embed)
        response = webhook.execute()
        oldprice = newprice

if __name__ == '__main__':
    main()