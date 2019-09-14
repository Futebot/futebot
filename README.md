# Futebot

[![CircleCI](https://circleci.com/gh/mrisoli/futebot/tree/master.svg?style=svg)](https://circleci.com/gh/mrisoli/futebot/tree/master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8aad709b46e74762a946811c009d92b7)](https://www.codacy.com/manual/mrisoli/futebot?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mrisoli/futebot&amp;utm_campaign=Badge_Grade)
[![codecov](https://codecov.io/gh/mrisoli/futebot/branch/master/graph/badge.svg)](https://codecov.io/gh/mrisoli/futebot)

Simple Discord Bot

## Installation

Export a discord bot token and run:

```
$ docker build . -t futebot:latest

$ docker run -it -e DISCORD_APP_TOKEN=${DISCORD_APP_TOKEN} -e GOOGLE_CUSTOM_SEARCH_API_TOKEN=${GOOGLE_CUSTOM_SEARCH_API_TOKEN} -e GOOGLE_CUSTOM_SEARCH_API_ID=${GOOGLE_CUSTOM_SEARCH_API_ID} --name futebot futebot:latest
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
```

## Testing

To run tests run:

```
pytest
```
