<?php
$resultado = "";

if (isset($_POST['calcular'])) {

    $numero1 = $_POST['num1'];
    $numero2 = $_POST['num2'];
    $operacao = $_POST['operacao'];

    switch ($operacao) {

        case "somar":
            $resultado = $numero1 + $numero2;
            break;

        case "subtrair":
            $resultado = $numero1 - $numero2;
            break;

        case "multiplicar":
            $resultado = $numero1 * $numero2;
            break;

        case "dividir":
            if ($numero2 != 0) {
                $resultado = $numero1 / $numero2;
            } else {
                $resultado = "Não é possível dividir por zero!";
            }
            break;
    }
}
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Calculadora PHP</title>
    <style>
        body {
            background-color: #142D4E;
            font-family: Arial, sans-serif;
            text-align: center;
            color: #000;
        }

        .calculadora {
            background-color: #fff;
            width: 300px;
            margin: 100px auto;
            padding: 25px;
            border-radius: 8px;
        }

        h2 {
            color: #142D4E;
        }

        input, select, button {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            box-sizing: border-box;
        }

        button {
            background-color: #142D4E;
            color: #fff;
            border: none;
            cursor: pointer;
        }

        button:hover {
            background-color: #000;
        }

        h3 {
            color: #142D4E;
        }
    </style>
</head>
<body>
    <div class="calculadora">
        <h2>Calculadora PHP</h2>
        <form method="POST">
            <input type="number" step="any" name="num1"
                placeholder="Primeiro número" required>

            <select name="operacao">
                <option value="somar">Adição (+)</option>
                <option value="subtrair">Subtração (-)</option>
                <option value="multiplicar">Multiplicação (*)</option>
                <option value="dividir">Divisão (/)</option>
            </select>

            <input type="number" step="any" name="num2"
                placeholder="Segundo número" required>

            <button type="submit" name="calcular">
                Calcular
            </button>
        </form>
        <?php
        if ($resultado !== "") {
            echo "<h3>Resultado: " . htmlspecialchars((string)$resultado) . "</h3>";
        }
        ?>
    </div>
</body>
</html>
