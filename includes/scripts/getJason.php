<?php
$timestamp = time();
$timeString = $timestamp . "000000";
$command = "python includes/scripts/json_maker2.py" . " " . $timeString . " " . "1";
echo $command;
exec($command, $output, $ret_code);
echo "Exit Code: " . $ret_code;
echo implode($output);

?>