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

```php
{
	$url = 'https://discordapp.com/api/oauth2/token';
	$data = [
		'client_id'=>$config['external']['discord']['bot']['client_id'],
		'client_secret'=>$config['external']['discord']['bot']['client_secret'],
		'grant_type'=>'authorization_code',
		'code'=>$credential,
		'redirect_uri'=>$_SERVER['REQUEST_SCHEME'].'://'.$_SERVER['HTTP_HOST'].'/'.basename(dirname(__DIR__)).'/',
	];
	$options = [ 'content-type: application/x-www-form-urlencoded' ];
	$curl_req = curl_init();
	curl_setopt($curl_req, CURLOPT_URL, $url);
	curl_setopt($curl_req, CURLOPT_POST, TRUE);
	curl_setopt($curl_req, CURLOPT_POSTFIELDS, http_build_query($data));
	curl_setopt($curl_req, CURLOPT_HTTPHEADER, $options);
	curl_setopt($curl_req, CURLOPT_RETURNTRANSFER, TRUE);
	curl_setopt($curl_req, CURLOPT_FOLLOWLOCATION, TRUE);
	$curl_res=curl_exec($curl_req);
	$curl_res=json_decode($curl_res, TRUE);
	error_log(json_encode($curl_res));
}
```


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
