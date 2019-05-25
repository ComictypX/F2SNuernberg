<?php
$timestamp = time();
$timeString = $timestamp . "000000";
$command = "python3 /var/www/html/scripts/json_maker2.py" . " " . $timeString . " " . "1 2>&1";
#$command = "php includes/scripts/test.php 2>&1";

#echo $command;
$output = shell_exec($command);
error_log(print_r($output, TRUE));
echo $output;
#echo json_encode($output, JSON_PRETTY_PRINT);
?>