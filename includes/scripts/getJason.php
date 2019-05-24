<?php
$timestamp = time();
$timeString = $timestamp . "000000";
$command = "python includes/scripts/json_maker2.py" . " " . $timeString . " " . "1"

$output = shell_exec($command);
echo $output;
?>