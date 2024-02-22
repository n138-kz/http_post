<?php
require_once('Discode_push_class.php');
$webhook = new discord();
$webhook->endpoint = 'https://discord.com/api/webhooks/xxxxx/xxxxxxxxxx';
$webhook->setValue('content', 'test');
$webhook_res = $webhook->exec_curl();
$webhook_res_mesg = $webhook->get_resultMesg($webhook_res);

if ($webhook_res['success'] != TRUE || $webhook_res['score'] < 0.3) {
  http_response_code(400);die();
}
