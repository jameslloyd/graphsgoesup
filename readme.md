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
     # - DISCORDWEBHOOK=https://discord.com/api/webhooks/931137345456066620/xJbBeXzqxAzpgNs6YEABoPxSZrGz52S6EjqfN7s3s9xcW3amdOQJuyXxwDcYTJEarxVj 
     - DISCORDWEBHOOK=https://discord.com/api/webhooks/271935678223220737/XvA13Bd4rtyr7pP97DescJOnLA1h_O4vKo26EtQyIdyo5LAzwodhHfO7T6HqqG-E4f1v
     - IEXAPIKEY=pk_3bf84a5d119e4c66bca92300da352256
     - PRICEWAITTIME=86400 
     - EMOJIUP=":thumbsup:"
     - EMOJIDOWN=":thumbsdown:"
     - EMOJIFLAT=":pause_button:"
     - CURRENCY=GBP
     - CRYPTO=ETH
     - LOG_LEVEL=INFO
```

