# Example

## Discord

```sh
if [ ! -f /tmp/test.json ]; then echo '{"body": "test", "time":'$(date +%s)'}' > /tmp/test.json; fi
discord_webhook_url='https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
curl \
 -X POST \
 -H 'Content-Type:multipart/form-data' \
 -F 'file=@/tmp/test.json' \
 -F 'content=Test: file and text send to discord.' \
 ${discord_webhook_url}
```

MUST: `Content-Type` = `multipart/form-data`  
CUSTOM: `username`, `avater_url`, `title`, Anything else follow view [official page](https://discord.com/developers/docs/resources/webhook).

![image](https://github.com/user-attachments/assets/fb9e3e7b-2cd5-480b-bfc7-c549070995e9)
