<?php
$timestamp = time();
$timeString = $timestamp . "000000";
$command = "python3 includes/scripts/json_maker2.py" . " " . $timeString . " " . "1";
#echo $command;
exec($command, $output);
#echo "Exit Code: " . $ret_code;
echo "'" . $output . "'";
?>