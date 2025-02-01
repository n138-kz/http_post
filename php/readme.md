# Usage

## [Discode_push_class.php](Discode_push_class.php)

```php
require_once('Discode_push_class.php');
$webhook = new discord();
$webhook->endpoint = 'https://discord.com/api/webhooks/server_id/channel_id';
$webhook->setValue('content', 'test');
$webhook_res = $webhook->exec_curl();
$webhook_res_mesg = $webhook->get_resultMesg($webhook_res);

if ($webhook_res['success'] != TRUE || $webhook_res['score'] < 0.3) {
  http_response_code(400);die();
}
```

<details>

  ![image](https://github.com/user-attachments/assets/a2b49710-9dd7-4f43-8915-48431e09d2dd)

  ```json
    {
      "Content-Type": "multipart/form-data",
      "content": "test",
      "file": "GiIPzXBbkAA5yCR.png (type: 'image/png'; size: 923410 bytes)"
    }
  ```
  
</details>


## [Google_reCAPTCHA_v3_validate_class.php](Google_reCAPTCHA_v3_validate_class.php)

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
