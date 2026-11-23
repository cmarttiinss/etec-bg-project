<?php
    $servidor="localhost";
	$banco="dbteste";
	$usuario="root";
	$senha="12345678";
	$cmd=new PDO("mysql:host=$servidor;port=3306;dbname=$banco",$usuario,$senha);
?>
