# Usage

## Discode_push_class.php

```php
function push2discord($endpoint, $content_author='Webhooks', $content_author_avatar='https://www.google.com/s2/favicons?size=256&domain=https://discord.com/', $content_color=0, $content_body=''){
  if ( is_empty( $endpoint ) ) { return false; }
  $content_color = is_numeric($content_color) ? $content_color : 0;
  $content_color = $content_color > 0 ? $content_color : 0;

  $payload = [];
  $payload += [
    'username' => $content_author,
    'content' => chr(0),
    'avatar_url' => $content_author_avatar,
    'embeds' => [],
  ];
  array_push($payload['embeds'], [
    'color' => $content_color,
    'timestamp' => date('c'),
    'footer' => [
      'text' => 'Auth-Google'
    ],
    'fields' => [
      [
        'inline' => false,
        'name' => '',
        'value' => $content_body
      ]
    ]
  ]);
  $payload_encoded = json_encode($payload);
  $curl_req = curl_init($endpoint);
  curl_setopt($curl_req,CURLOPT_POST, TRUE);
  curl_setopt($curl_req,CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
  curl_setopt($curl_req,CURLOPT_POSTFIELDS, $payload_encoded);
  curl_setopt($curl_req,CURLOPT_SSL_VERIFYPEER, TRUE);
  curl_setopt($curl_req,CURLOPT_SSL_VERIFYHOST, 2);
  curl_setopt($curl_req,CURLOPT_RETURNTRANSFER, TRUE);
  curl_setopt($curl_req,CURLOPT_FOLLOWLOCATION, TRUE);
  $curl_res=curl_exec($curl_req);
  $curl_res=json_decode($curl_res, TRUE);
  return $curl_res;
}
$config = [
  'external' => [
    'discord' => [
      'activate' => [
        'notice': false,
      ],
      'uri' => [
        'notice': "https://discord.com/api/webhooks/{server-id}/{channel-id}",
      ],
      'color' => [
        'notice': 32768,
      ],
      'authorname' => [
        'notice': "notice.authn.bot.n138.nws",
      ],
      'authoravatar' => [
        'notice': "https://www.google.com/s2/favicons?size=256&domain=https://discord.com/",
      ],
    ]
  ]
];
if ($config['external']['discord']['activate']['notice']) {
  push2discord(
    $config['external']['discord']['uri']['notice'],
    $config['external']['discord']['authorname']['notice'],
    $config['external']['discord']['authoravatar']['notice'],
    $config['external']['discord']['color']['notice'],
    'time: '      . chr(9) . time()                                   .       PHP_EOL.
    '```json' . PHP_EOL.
    json_encode([
      null,
    ], JSON_PRETTY_PRINT|JSON_UNESCAPED_SLASHES ) . PHP_EOL.
    '```' . PHP_EOL
  );
}
```
