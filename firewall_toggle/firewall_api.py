import os
import requests 
import json
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
BASE_URL = os.getenv('BASE_URL')


def get_firewall_rules():
    url =BASE_URL + 'searchRule?current=1&rowCount=7'
    r = requests.get(
        url,
        verify=False,
        auth=(API_KEY, API_SECRET),
    )
    return json.loads(r.text)["rows"]


def change_firewall_rule(rule_uuid, state=None):
    if state is not None:
        toggle_url = BASE_URL + f"toggleRule/{rule_uuid}/{state}"
    else:
        toggle_url = BASE_URL + f"toggleRule/{rule_uuid}"
    apply_url = BASE_URL + "apply"
    r = requests.post(
        toggle_url,
        verify=False,
         auth=(API_KEY, API_SECRET)
    )
    if r.status_code == 200:
        r = requests.post(
            apply_url,
            verify=False,
            auth=(API_KEY, API_SECRET)
        )
        if r.status_code == 200:
            return
    else:
        print(r.status_code)
        print(r.text)
        raise Exception('api failed to toggle rule')
