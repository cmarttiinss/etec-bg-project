<?php
	include 'conexao.php'; 
	$vnome=$_POST['txtnome'];
	$vemai=$_POST['txtemail'];
    $vsenh=$_POST['txtsenha'];
	$vsexo=$_POST['txtsexo'];
	$vdtna=$_POST['txtdata'];
	$cadastrar=$cmd->query("insert into tbteste(nome_t,emai_t,senh_t,sexo_t,dtna_t) values('$vnome','$vemai','$vsenh','$vsexo','$vdtna')");
	echo "<script language='JavaScript'>
            alert('Dados cadastrados com sucesso!!! ');
            location.href='crud_cada.html';
          </script>";
?>	
