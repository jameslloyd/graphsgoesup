FROM alpine
RUN apk update
RUN apk add --no-cache python3 py3-pip
RUN pip3 install --no-cache-dir --upgrade pip
COPY requirements.txt /graphgoesup/requirements.txt
RUN pip3 install -r /graphgoesup/requirements.txt

COPY ./ /graphgoesup

RUN rm -rf /var/cache/* 
RUN rm -rf /root/.cache/* 

ENV UID=1000
ENV GID=1000
RUN addgroup -g ${GID} -S appgroup && adduser -u ${UID} -S appuser -G appgroup
USER appuser

ENTRYPOINT [ "python3", "-u", "/graphgoesup/main.py"]
LABEL maintainer=james.lloyd@gmail.com