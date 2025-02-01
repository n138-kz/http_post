# Usage

## Discode_push_class.php

```php
require_once('Discode_push_class.php');
$webhook = new discord();
$webhook->endpoint = 'https://discord.com/api/webhooks/xxxxx/xxxxxxxxxx';
$webhook->setValue('content', 'test');
$webhook_res = $webhook->exec_curl();
$webhook_res_mesg = $webhook->get_resultMesg($webhook_res);

if ($webhook_res['success'] != TRUE || $webhook_res['score'] < 0.3) {
  http_response_code(400);die();
}
```

## Google_reCAPTCHA_v3_validate_class.php

```php
require_once('Google_reCAPTCHA_v3.php');
$google = new google();
$google->setKey_private('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx');
$google->setKey_public($_POST['token-of-client']);
$google->setip_remotehost($_SERVER['REMOTE_ADDR']);
$google_res = $google->exec_curl();
$google_res_mesg = $google->get_resultMesg($google_res);

if ($google_res['success'] != TRUE || $google_res['score'] < 0.3) {
  http_response_code(400);die();
}
```
