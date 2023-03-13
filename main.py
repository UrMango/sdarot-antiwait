import time

import requests
import json

REMEMBER = "<REMEMBER COOKIE HERE>"
COOKIE = "Sdarot=<COOKIE HERE>; remember=" + REMEMBER
URL = "https://sdarot.tw/ajax/watch"


def get_token(SID, season, episode):
    payload = {'preWatch': 'true', 'SID': str(
        SID), 'season': str(season), 'ep': str(episode)}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'referer': 'https://sdarot.tw/'
    }

    response = requests.post(URL, data=payload, headers=headers)

    token = response.text
    print("TOKEN GOT: ", token)

    return token


def get_vast():
    payload = {'vast': 'true'}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'origin': 'https://sdarot.tw',
        'referer': 'https://sdarot.tw/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'scheme': 'https',
        'X-Requested-With': 'XMLHttpRequest',
        'cookie': COOKIE
    }

    response = requests.post(URL, data=payload, headers=headers)

    print("VAST GOT: ", response.text)


def get_episode(token, SID, season, episode):
    payload = {'watch': 'false', 'token': str(token), 'serie': str(
        SID), 'season': str(season), 'episode': str(episode), 'type': 'episode'}
    print(payload)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'origin': 'https://sdarot.tw',
        'referer': 'https://sdarot.tw/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.7',
        'Cookie': COOKIE
    }

    response = requests.post(URL, data=payload, headers=headers)
    print(response.request.headers)
    decode = json.JSONDecoder()
    res = decode.decode(response.text)
    return res


if __name__ == '__main__':
    print(COOKIE)
    SID = 8327  # Series ID to watch
    season = 1  # Season
    episode = 3  # Episode

    token = get_token(SID, season, episode)
    get_vast()
    time.sleep(3)
    print(get_episode(token, SID, season, episode))
