FROM python:3.7.4

WORKDIR /usr/src/app

RUN git clone https://github.com/Futebot/futebot.git

RUN cd futebot && \
    pip install pipenv && \
	pipenv install --system

CMD [ "python", "/usr/src/app/futebot/main.py" ]
