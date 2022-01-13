# Graph Goes Up

get an iexcloud apikey from https://iexcloud.io/console/

## Docker
```
docker run --name graphgoesup -it jameslloyd/graphgoesup     
    -e PRICEWAITTIME=30 / # number of seconds to wait 
    -e IEXAPIKEY='\<YOUR IEXAPIKEY\>' /
    -e DISCORDWEBHOOK='\<YOUR DISCORD WEBHOOK\>'
```
## docker-compose
```
---
version: "2.1"
services:
  graphgoesup:
    image: jameslloyd/graphgoesup
    container_name: graphgoesup
    environment:
     - DISCORDWEBHOOK=<SOME DISCORD WEB HOOK>
     - IEXAPIKEY=<YOUR API KEY>
     - PRICEWAITTIME=86400 #one day
     - EMOJIUP=":thumbsup:"
     - EMOJIDOWN=":thumbsdown:"
     - EMOJIFLAT=":pause_button:"
     - CURRENCY=GBP
     - CRYPTO=ETH
     - LOG_LEVEL=INFO
```

