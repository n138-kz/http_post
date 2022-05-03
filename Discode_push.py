import requests
import json
# refs docs: https://birdie0.github.io/discord-webhooks-guide/discord_webhook.html

api_url = 'https://discord.com/api/webhooks/xxxxx/xxxxxxxxxx'
post_data = {
  'username' : 'override username',
  'title'    : 'Title',
  'content'  : 'test',
};

curl_res = requests.post(api_url, data=post_data)
print(curl_res.status_code) # HTTPのステータスコード取得
print(curl_res.text)        # レスポンスのHTMLを文字列で取得
