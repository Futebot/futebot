# Futebot

[![CircleCI](https://circleci.com/gh/mrisoli/futebot/tree/master.svg?style=svg)](https://circleci.com/gh/mrisoli/futebot/tree/master)
[![codecov](https://codecov.io/gh/mrisoli/futebot/branch/master/graph/badge.svg)](https://codecov.io/gh/mrisoli/futebot)

Simple Discord Bot

## Installation

Export a discord bot token and run:

```
$ docker build . -t futebot:latest

$ docker run -it -e DISCORD_APP_TOKEN=${DISCORD_APP_TOKEN} -e GOOGLE_CUSTOM_SEARCH_API_TOKEN=${GOOGLE_CUSTOM_SEARCH_API_TOKEN} -e GOOGLE_CUSTOM_SEARCH_API_ID=${GOOGLE_CUSTOM_SEARCH_API_ID} COMMANDS_DATA_FILE=${COMMANDS_DATA_FILE} OPENWEATHER_KEY=${OPENWEATHER_KEY} --name futebot futebot:latest
```

Or

```
docker-compose up --build
```
The step above expects a file `keys.env` in the root directory with the following variables:
```.env
DISCORD_APP_TOKEN=<HUETOKEN>
GOOGLE_CUSTOM_SEARCH_API_TOKEN=<HUEAPITOKEN>
GOOGLE_CUSTOM_SEARCH_API_ID=<HUEAPIID>
COMMANDS_DATA_FILE=<COMMANDS_DATA_FILE>
IMGUR_CLIENT_ID=<CLIENTID>
IMGUR_CLIENT_SECRET=<CLIENTSECRET>
OPENWEATHER_KEY=<OPENWEATHER_KEY>
BOT_ENV=dev
```

## Testing

To run tests run:

```
pytest
```
