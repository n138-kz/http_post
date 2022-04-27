$post_data = [
  'username' => 'override username',
  'title'    => 'Title',
  'content'  => 'Content',
];
$curl_req = curl_init('https://discord.com/api/webhooks/xxxxx/xxxxxxxxxx');
curl_setopt($curl_req,CURLOPT_POST, TRUE);
curl_setopt($curl_req,CURLOPT_POSTFIELDS, http_build_query($post_data));
curl_setopt($curl_req,CURLOPT_SSL_VERIFYPEER, FALSE);  // オレオレ証明書対策
curl_setopt($curl_req,CURLOPT_SSL_VERIFYHOST, FALSE);  //
curl_setopt($curl_req,CURLOPT_RETURNTRANSFER, TRUE);
curl_setopt($curl_req,CURLOPT_COOKIEJAR,      'cookie');
curl_setopt($curl_req,CURLOPT_COOKIEFILE,     'tmp');
curl_setopt($curl_req,CURLOPT_FOLLOWLOCATION, TRUE); // Locationヘッダを追跡
$curl_res=curl_exec($curl_req);
