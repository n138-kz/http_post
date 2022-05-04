<?php
/*
* refs docs: https://www.google.com/recaptcha/admin
*/
$rtoken = 'xxxxxxxxx' // submit from client
$remote = '192.168.0.10' // client ip address ( -> $_SERVER['REMOTE_ADDR'] )
$post_data = [
  'secret'  => 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
  'response'=> $rtoken,
  'remoteip'=> $remote,
];
$curl_req = curl_init('https://www.google.com/recaptcha/api/siteverify');
curl_setopt($curl_req,CURLOPT_POST, TRUE);
curl_setopt($curl_req,CURLOPT_POSTFIELDS, http_build_query($post_data));
curl_setopt($curl_req,CURLOPT_SSL_VERIFYPEER, FALSE);  // オレオレ証明書対策
curl_setopt($curl_req,CURLOPT_SSL_VERIFYHOST, FALSE);  //
curl_setopt($curl_req,CURLOPT_RETURNTRANSFER, TRUE);
curl_setopt($curl_req,CURLOPT_COOKIEJAR,      'cookie');
curl_setopt($curl_req,CURLOPT_COOKIEFILE,     'tmp');
curl_setopt($curl_req,CURLOPT_FOLLOWLOCATION, TRUE); // Locationヘッダを追跡
$curl_res=curl_exec($curl_req);

$curl_res=json_decode($curl_res, TRUE);
if (!isset($curl_res['success']) || $curl_res['success'] != TRUE || $curl_res['score'] < 0.3) {
  // validation fail

  if (isset($curl_res['success']) && trim($curl_res['success']) != TRUE) {
    // result description -> $result
    foreach ($curl_res['error-codes'] as $key => $val) {
      if ($key>1) { $result.=', '; }
      $result.=$val;
    }
    $result.=' ';
  }
} else {
  // validation ok
}
