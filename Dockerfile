FROM python:latest

WORKDIR /usr/src/app

COPY Pipfile ./

RUN pip install pipenv && \
	pipenv lock && \
	pipenv install --system

COPY . .

CMD [ "python", "./main.py" ]
