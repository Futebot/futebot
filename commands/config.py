import os

AVAILABLE_SPOILER_ACTIONS = ["--spoiler", "--nsfw"]
CHARADA_ENDPOINT = "https://us-central1-kivson.cloudfunctions.net/charada-aleatoria"
COACH_ENDPOINT = "http://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang=en"
YT_RESULTS_ENDPOINT = "http://www.youtube.com/results?"
YT_WATCH_ENDPOINT = "http://www.youtube.com/watch?v="
HOROSCOPO_ENDPOINT = "http://babi.hefesto.io/signo/{}/dia"
IMGUR_CLIENT_ID = os.getenv('IMGUR_CLIENT_ID')
IMGUR_CLIENT_SECRET = os.getenv('IMGUR_CLIENT_SECRET')
