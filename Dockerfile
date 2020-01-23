FROM python:3.7.4

WORKDIR /usr/src/app

COPY Pipfile ./
COPY Pipfile.lock ./

RUN pip install pipenv && \
	pipenv install --system

COPY . .

CMD [ "python", "./main_slack.py" ]
