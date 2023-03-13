#!/usr/bin/env python3

import argparse
from os import environ
import requests
from urllib.parse import urlencode

ZUKO_SESSIONS_API_URL = 'https://egress.api.zuko.io/sessions'

try:
  ZUKO_API_KEY = environ['ZUKO_API_KEY']
except KeyError:
  exit('The ZUKO_API_KEY environment variable must be set with your Zuko API key')

parser = argparse.ArgumentParser()
parser.add_argument('--form-uuid', '-f', required=True)
parser.add_argument('--start-time', '-s', required=True)
parser.add_argument('--end-time', '-e', required=True)
args = parser.parse_args()

def fetch_sessions(params):
  resp = requests.get(
    ZUKO_SESSIONS_API_URL + "?" + urlencode(params),
    headers={
      'X-Api-Key': ZUKO_API_KEY
    }
  )
  resp.raise_for_status()
  next_page_id = resp.json().get('next_page_id')
  sessions = resp.json()['sessions']
  return [next_page_id, sessions]

params = {
  'form_uuid': args.form_uuid,
  'time[from]': args.start_time,
  'time[to]': args.end_time,
}

sessions = []
next_page_id = True

while next_page_id:
  next_page_id, batch = fetch_sessions(params)
  sessions += batch
  params['next_page_id'] = next_page_id

views, starters, completions, abandons = 0, 0, 0, 0

for session in sessions:
  if session['viewed']:
    views += 1

  if session['started']:
    starters += 1

    if session['completed']:
      completions += 1
    else:
      abandons += 1

vs_rate = (completions/views) * 100

print('There were {} views for your form'.format(views))
print('There were {} starters for your form'.format(starters))
print('There were {} completions for your form'.format(completions))
print('There were {} abandons for your form'.format(abandons))
print('The overall view-to-completion rate for your form was {}%'.format(round(vs_rate, 2)))
