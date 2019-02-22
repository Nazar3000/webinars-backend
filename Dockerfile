FROM python:3.7-slim

WORKDIR /app

COPY . /app

RUN set -xe \
    && pip3 install -r requirements.txt \
	&& . ./env.sh

EXPOSE 8000

CMD ["python3", "manage.py", "migrate"]