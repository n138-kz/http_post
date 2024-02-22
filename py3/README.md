# py3

## for Login notice program

1. Downloads a [Discode_push_fromSTDIN.py](Discode_push_fromSTDIN_v1.0.py)
2. Fix the `api_url` on [Discode_push_fromSTDIN.py](Discode_push_fromSTDIN_v1.0.py)
	- Issue the discord webhook uri. References manual url is [HERE(Intro to Webhooks)](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
3. Upload into `/usr/bin/`
4. Edit the `/etc/profile` (if use bash)

```diff
+ echo -e "<Login Notice> \nDate: \``date`\` \nUser: \`${USER}@${HOSTNAME}\` \nFrom: \``echo ${SSH_CLIENT} | awk '{print $1,$2}'`\` \nTerm: \`${TERM} ${SSH_TTY}\` \n----- \n`who | grep -v ':' | grep -v grep`" | /usr/bin/python /usr/bin/Discode_push_fromSTDIN.py
```
