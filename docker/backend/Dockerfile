FROM python:3.7.1

VOLUME ["/app"]
COPY start.sh /scripts/start.sh
WORKDIR /app/src

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.5.0/wait /wait
RUN chmod +x /wait

CMD /wait && /scripts/start.sh

#ENTRYPOINT [""]
