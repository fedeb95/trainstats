FROM python:3.6-slim

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ADD crontab /etc/cron.d/trains-cron

RUN chmod 0644 /etc/cron.d/trains-cron

RUN touch /var/log/cron.log

CMD cron && tail -f /var/log/cron.log

CMD ["python","runner.py","config"]
