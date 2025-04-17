# Example

## Discord(with file)

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

## Discord(without file)

```sh
discord_webhook_url='https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
curl \
 -X POST \
 -d 'content=Test: file and text send to discord' \
 ${discord_webhook_url}
```

CUSTOM: [curlでリクエストボディに改行を含める方法|悪魔のオコトバ](https://akumachan.github.io/%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%97%E3%83%88/curl%E3%81%A7%E3%83%AA%E3%82%AF%E3%82%A8%E3%82%B9%E3%83%88%E3%83%9C%E3%83%87%E3%82%A3%E3%81%AB%E6%94%B9%E8%A1%8C%E3%82%92%E5%90%AB%E3%82%81%E3%82%8B%E6%96%B9%E6%B3%95/)

## Login notice to Discord(with embed)

```sh
export discord_webhook_url=https://discord.com/api/webhooks/990898252293505064/t73ECWZv8LR7S0jk6PgRANudk10Yd1RVkuTBy4uBqKSf3b68SGmR-Jn0nC6-1h8eVewO
export discord_avatar_url=https://hangstuck.com/wp-content/uploads/2020/08/bash-official-icon-512x512-1.png

runtime=$(date +%s)
discord_embed_json='{"username":"'${HOSTNAME%%.*}'","avatar_url":"'${discord_avatar_url}'","content":"","embeds":[{"title": "Login Notice","fields": [{"name": "Date","value": "<t:'"${runtime}"':R>\n<t:'"${runtime}"':F>"},{"name": "User","value": "`'${USER}'@'${HOSTNAME}'`"},{"name": "From","value": "`'$(echo ${SSH_CLIENT}|awk '{print $1,":",$2}')'`"},{"name": "Term","value": "`'${TERM}'` `'${SSH_TTY}'`"}],"color": "'$((16#c0c0c0))'","footer": {"text": "'${HOSTNAME}'","icon_url": "'${discord_avatar_url}'"},"timestamp": "'$(date --utc '+%Y-%m-%dT%H:%M:%S.000Z')'"}]}'
test -d /tmp/discord_embed_json || mkdir /tmp/discord_embed_json
echo ${discord_embed_json}>/tmp/discord_embed_json/${HOSTNAME%%.*}_${runtime}.json
curl -s -X POST -H 'Content-Type: application/json' -d @/tmp/discord_embed_json/${HOSTNAME%%.*}_${runtime}.json ${discord_webhook_url}'?wait=true'>/tmp/discord_embed_json/${HOSTNAME%%.*}_${runtime}.log
cat /tmp/discord_embed_json/${HOSTNAME%%.*}_${runtime}.log | jq > /tmp/discord_embed_json/${HOSTNAME%%.*}_${runtime}.log.json
```

