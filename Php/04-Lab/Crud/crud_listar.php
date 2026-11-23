<?php
    echo "<link rel='stylesheet' type='text/css' href='style2.css'/>";
    include 'conexao.php';
	$listar=$cmd->query("select * from tbteste");
	$total_registros=$listar->rowCount();
    if ($total_registros > 0)
    {
        echo "<h1>Listar Registros</h1>";
        echo "<hr/>";
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
				
        while($linha=$listar->fetch(PDO::FETCH_ASSOC))
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
        echo "<a class='botao_menu' href='index.html'>Menu</a>";/*ou window.history.back()*/
	}
    else
    {
        echo "<script language=javascript>
                window.alert('Não existem registros para exibir!!!');
                location.href='index.html'; 
              </script>";
    }
?>