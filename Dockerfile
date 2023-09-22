FROM python:3.9

WORKDIR /usr/src/app

COPY Pipfile ./
COPY Pipfile.lock ./


RUN pip install pipenv && \
	pipenv install --system

COPY . .

CMD [ "python", "-u", "./main_slack.py" ]
