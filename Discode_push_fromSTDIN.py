import requests
import json
import sys
# refs docs: https://birdie0.github.io/discord-webhooks-guide/discord_webhook.html

stdin = sys.stdin
stdin = stdin.read()

api_url = 'https://discord.com/api/webhooks/971034845620879410/LlT2O5nGsycGY4745uPgnNnRdA0hya5_TAchiPFS-i81COHCDh0-n4467DDrtiauyTim'
post_data = {
  'title'    : 'Notice Test',
  'content'  : stdin,
};

curl_res = requests.post(api_url, data=post_data)
if curl_res.status_code >= 400:
  print(curl_res.status_code)
  print(curl_res.text)

