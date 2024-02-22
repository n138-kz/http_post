<?php
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
