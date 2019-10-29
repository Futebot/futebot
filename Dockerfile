FROM python:3.7.4

RUN git clone https://github.com/Futebot/futebot.git
WORKDIR /futebot


RUN pip install pipenv && \
	pipenv install --system

CMD [ "python", "./main.py" ]
