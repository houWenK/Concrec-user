import requests
from rank.config import config


def get_recall(user_id):
    params = {}
    if user_id is not None:
      params['user_id'] = user_id
    res = requests.get(config['recall_endpoint'], params=params)
    return res.json()
