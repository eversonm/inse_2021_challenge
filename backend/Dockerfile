FROM python:3.10.13-alpine3.18

WORKDIR /app

COPY /backend/requirements.txt /backend/entrypoint.sh ./

RUN apk add --no-cache \
	postgresql-dev gcc python3 python3-dev musl-dev libffi-dev build-base
RUN python3 -m ensurepip && \
	rm -r /usr/lib/python*/ensurepip && \
	pip3 install --upgrade pip setuptools && \
	rm -r /root/.cache
RUN pip3 install -r requirements.txt && \
	pip3 install -U flask-cors

EXPOSE 5000

COPY /backend/src /app/src
COPY /backend/alembic.ini /app

ENTRYPOINT ["sh", "/app/entrypoint.sh"]
