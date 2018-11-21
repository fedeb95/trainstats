FROM ubuntu:latest

RUN apt-get update && apt-get install -y software-properties-common

RUN apt-get update && apt-get install -y python3.4 python3-pip

WORKDIR /app

ADD . /app

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

ADD crontab /etc/cron.d/trains-cron

RUN chmod 0644 /etc/cron.d/trains-cron

RUN touch /var/log/cron.log

CMD cron && tail -f /var/log/cron.log
