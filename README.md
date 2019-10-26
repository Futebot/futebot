# Futebot

[![CircleCI](https://circleci.com/gh/mrisoli/futebot/tree/master.svg?style=svg)](https://circleci.com/gh/mrisoli/futebot/tree/master)
[![codecov](https://codecov.io/gh/mrisoli/futebot/branch/master/graph/badge.svg)](https://codecov.io/gh/mrisoli/futebot)

Simple Discord Bot

## Installation

Export a discord bot token and run:

```
$ docker build . -t futebot:latest

$ docker run -it -e DISCORD_APP_TOKEN=${DISCORD_APP_TOKEN} -e GOOGLE_CUSTOM_SEARCH_API_TOKEN=${GOOGLE_CUSTOM_SEARCH_API_TOKEN} -e GOOGLE_CUSTOM_SEARCH_API_ID=${GOOGLE_CUSTOM_SEARCH_API_ID} -e COMMANDS_DATA_FILE=${COMMANDS_DATA_FILE} -e OPENWEATHER_KEY=${OPENWEATHER_KEY} -e CLARIFAI_API_KEY=${CLARIFAI_API_KEY} -e IMGUR_CLIENT_ID=${IMGUR_CLIENT_ID} -e IMGUR_CLIENT_SECRET=${IMGUR_CLIENT_SECRET} -e SPOTIFY_CLIENT_ID=${SPOTIFY_CLIENT_ID} -e SPOTIFY_CLIENT_SECRET=${SPOTIFY_CLIENT_SECRET} --name futebot futebot:latest
```

Or

```
docker-compose up --build
```

Or

Download pipenv:

```
pip install pipenv
pipenv install
```

The step above expects a file `keys.env` in the root directory with the following variables:
```.env
DISCORD_APP_TOKEN=<HUETOKEN>
GOOGLE_CUSTOM_SEARCH_API_TOKEN=<HUEAPITOKEN>
GOOGLE_CUSTOM_SEARCH_API_ID=<HUEAPIID>
COMMANDS_DATA_FILE=<COMMANDS_DATA_FILE>
OPENWEATHER_KEY=<OPENWEATHER_KEY>
CLARIFAI_API_KEY=<CLARIFAI_API_KEY>
IMGUR_CLIENT_ID=<CLIENTID>
IMGUR_CLIENT_SECRET=<CLIENTSECRET>
SPOTIFY_CLIENT_ID = <SPOTIFY_CLIENT_ID>
SPOTIFY_CLIENT_SECRET = <SPOTIFY_CLIENT_SECRET>
BOT_ENV=dev
```

## Testing

To run tests run:

```
pipenv run pytest
```


## Lint check

```
pipenv run pycodestyle
```