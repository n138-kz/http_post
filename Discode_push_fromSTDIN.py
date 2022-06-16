# refs docs: https://birdie0.github.io/discord-webhooks-guide/discord_webhook.html
import requests
import json
import sys
import os

VERSION = 1.0
api_url = 'https://discord.com/api/webhooks/xxxxx/xxxxx'

stdin = sys.stdin
stdin = stdin.read()
stdin = str(stdin)

try:
    hostname = os.uname()[1]
except Exception as e:
    hostname = ''

post_data = {
  'username' : hostname,
  'content'  : stdin,
};

curl_res = requests.post(api_url, data=post_data)
if curl_res.status_code >= 400:
  print(curl_res.status_code)
  print(curl_res.text)
