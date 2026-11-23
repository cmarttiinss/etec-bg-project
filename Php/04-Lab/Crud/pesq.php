<?php
    echo "<link rel='stylesheet' type='text/css' href='formata.css'/>";
   	include 'conexao.php';
	$nome=$_POST['txtnome'];
    $pesq=$cmd->query("select * from tbteste where nome_t like '$nome%'");
	$total_registros =$pesq->rowCount();
    if ($total_registros > 0)
     {
        echo "<table>";
        echo "<tr>
                <th colspan=6>
                    Dados Cadastrados
                </th>
              </tr>";
        echo "<tr>
                <th>Código</th>
                <th>Nome</th>
                <th>E-mail</th>
                <th>Senha</th>
                <th>Sexo</th>
                <th>Nascimento</th>
              </tr>";
				
        while($linha=$pesq->fetch(PDO::FETCH_ASSOC))
        {
            $vcodi=$linha['codi_t'];
            $vnome=$linha['nome_t'];
            $vemai=$linha['emai_t'];
            $vsenh=$linha['senh_t'];
			$vsexo=$linha['sexo_t'];
            $vdtna=$linha['dtna_t'];
            echo "<tr>
                    <td>$vcodi</td>
                    <td>$vnome</td>
                    <td>$vemai</td>
                    <td>$vsenh</td>
                    <td>$vsexo</td>
   		            <td>$vdtna</td>          
                  </tr>";
		}
	    echo "</table>";
        echo "<br/><br/>";
        echo "<a class='botao_menu' href='crud_pesq.html'>Nova Pesquisa</a>";
	}
    else
    {
        echo "<script language=javascript> window.alert('Não existem registros para exibir!!!'); location.href='crud_pesq.html'; </script>";
    }
?>