

import requests
from core.domain.entity.joke import Joke
from core.domain.repositories.get_joke import GetJokeDefinition


class GetJokeImpl(GetJokeDefinition):
    def get_joke(self):
        URL = 'https://api.chucknorris.io/jokes/random' 
        resp = requests.get(url=URL)
        data = resp.json()
        joke = Joke(data['id'], data['icon_url'], data['url'], data['value'])
        return joke