from config import Config
import os, time
import requests
from datetime import timedelta
from discord_webhook import DiscordWebhook, DiscordEmbed
import logging

Config = Config()

def get_crypto_price(symbol):
    api_url = f'https://cloud.iexapis.com/stable/crypto/{symbol}/price?token={Config.IEXAPIKEY}'
    raw = requests.get(api_url,headers={'Cache-Control': 'no-cache',"Pragma": "no-cache"}).json()
    price = raw['price']
    return float(price)

def main():
    logging.basicConfig(format=Config.LOG_FORMAT ,level=Config.LOG_LEVEL)
    logging.info('Started application {} in {}'.format(Config.APPNAME, Config.ENV))
    symbol = Config.CRYPTO.lower() + Config.CURRENCY.lower()
    while True:
        try: 
            oldprice
        except:
            oldprice = get_crypto_price(symbol)
            logging.info(f'Discord Webhook = {Config.DISCORDWEBHOOK}')
            logging.info('Current Price {} sleeping for {} seconds'.format(oldprice,Config.PRICEWAITTIME))
        time.sleep(Config.PRICEWAITTIME)
        newprice = get_crypto_price(symbol)
        increase = round((newprice - oldprice) / oldprice * 100,2)
        logging.info('New Price {} {}% change'.format(newprice,increase,2))
        if newprice == oldprice:
            title = 'Graph is flat'
            colour = 'FFBF00'
            icon = Config.EMOJIFLAT
            move = ''
        elif newprice > oldprice:
            #graph goes up
            title = 'Graph goes up'
            colour = '00FF00'
            icon = Config.EMOJIUP
            move = 'increase'
        else:
            #graph goes down
            title = 'Graph goes down'
            colour = 'FF0000'
            icon = Config.EMOJIDOWN
            move = 'decrease'
        
        webhook = DiscordWebhook(url=Config.DISCORDWEBHOOK)
        embed = DiscordEmbed(title=title,description=f'{icon} {increase}% {move}', color=colour)
        embed.set_author(name='GraphGoesUp', url='https://github.com/jameslloyd/graphsgoesup', icon_url='https://www.freeiconspng.com/uploads/growth-icon-28.png')
        embed.set_timestamp()
        embed.add_embed_field(name='Change', value=f'{increase}%', inline=False)
        embed.add_embed_field(name='Value', value=f'{newprice}', inline=False)
        webhook.add_embed(embed)
        response = webhook.execute()
        oldprice = newprice

if __name__ == '__main__':
    main()