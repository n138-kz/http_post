# refs docs: https://birdie0.github.io/discord-webhooks-guide/discord_webhook.html
import requests
import json
import sys
import os

stdin = sys.stdin
stdin = stdin.read()

api_url = 'https://discord.com/api/webhooks/xxxxx/xxxxx'
post_data = {
  'username' : os.uname()[1],
  'content'  : stdin,
};

curl_res = requests.post(api_url, data=post_data)
if curl_res.status_code >= 400:
  print(curl_res.status_code)
  print(curl_res.text)
