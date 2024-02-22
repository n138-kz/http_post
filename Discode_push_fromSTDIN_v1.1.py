# refs docs: https://birdie0.github.io/discord-webhooks-guide/discord_webhook.html
import requests
import json
import sys
import os
import argparse

VERSION = 1.1
api_url = 'https://discord.com/api/webhooks/xxxxx/xxxxx'

stdin = sys.stdin
stdin = stdin.read()
stdin = str(stdin).strip()

try:
    hostname = os.uname()[1]
except Exception as e:
    hostname = ''

parser = argparse.ArgumentParser(
                                    prog=os.path.basename(__file__),
                                    description=''
                                )

parser.add_argument('--discord',
                    help='specify the discord webhooks uri.',
                    nargs=1,
                    default=None,
                    metavar='URL',
                   )

args = parser.parse_args()
print(args)

post_data = {
  'username' : hostname,
  'content'  : stdin,
};

curl_res = requests.post(api_url, data=post_data)
if curl_res.status_code >= 400:
  print(curl_res.status_code)
  print(curl_res.text)
