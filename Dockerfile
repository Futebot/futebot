FROM python:latest

WORKDIR /usr/src/app

COPY Pipfile ./
COPY Pipfile.lock ./

RUN pip install pipenv && \
	pipenv install --system

COPY . .

CMD [ "python", "./main.py" ]
