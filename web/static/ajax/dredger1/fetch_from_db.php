<?php 
    $hostname_connection = "localhost"; 
    $database_connection = "dredger"; 
    $username_connection = "root"; 
    $password_connection = "aaggss"; 
    $connection = mysql_connect($hostname_connection, $username_connection, $password_connection) or trigger_error(mysql_error(),E_USER_ERROR); 
    mysql_select_db($database_connection,$connection) or die( mysql_error("could not connect to database! " ) ) ; 
?>

<?php 
    $display = sprintf("select * from db order by time desc limit 1"); 
    $result=mysql_query($display,$connection) or die(mysql_error()); 
    if($result == FALSE) 
      { die(mysql_error()); }
?>

<?php

    $rows = mysql_fetch_assoc($result);
    $return_data=array('time' => $rows['time'],
        'consumption'  => $rows['consumption']);
    header('Content-Type: application/json');
    echo json_encode($return_data);
    exit();
  ?>


