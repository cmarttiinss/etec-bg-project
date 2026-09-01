function calculo(operacao) {
    const campo1 = document.getElementById("valorA");
    const campo2 = document.getElementById("valorB");
    const campo3 = document.getElementById("valorC");

    const delta = document.getElementById("resudelta");
    const raizA = document.getElementById("raiz1");
    const raizB = document.getElementById("raiz2");

    const valor1texto = campo1.value.trim();
    const valor2texto = campo2.value.trim();
    const valor3texto = campo3.value.trim();

    if (valor1texto === "" || isNaN(valor1texto)) {
        alert("Digite um número válido no campo A");
        campo1.value = "";
        campo1.focus();
        return;
    }

    if (parseFloat(valor1texto) === 0) {
        alert("O valor de A não pode ser zero para uma equação do 2º grau.");
        campo1.value = "";
        campo1.focus();
        return;
    }

    if (valor2texto === "" || isNaN(valor2texto)) {
        alert("Digite um número válido no campo B");
        campo2.value = "";
        campo2.focus();
        return;
    }

    if (valor3texto === "" || isNaN(valor3texto)) {
        alert("Digite um número válido no campo C");
        campo3.value = "";
        campo3.focus();
        return;
    }

    const valor1 = parseFloat(valor1texto);
    const valor2 = parseFloat(valor2texto);
    const valor3 = parseFloat(valor3texto);

    switch (operacao) {
        case "calc":
            const resultadoDelta = valor2 ** 2 - 4 * valor1 * valor3;
            delta.value = resultadoDelta.toFixed(2);

            if (resultadoDelta < 0) {
                alert("Delta é negativo. A equação não possui raízes reais.");
                raizA.value = "";
                raizB.value = "";
                return;
            }

            if (resultadoDelta === 0) {
                const raiz = -valor2 / (2 * valor1);
                raizA.value = raiz.toFixed(2);
                raizB.value = raiz.toFixed(2);
                alert("O valor de delta é igual a 0.");
                return;
            }

            const resultadoRaiz1 = (-valor2 + Math.sqrt(resultadoDelta)) / (2 * valor1);
            const resultadoRaiz2 = (-valor2 - Math.sqrt(resultadoDelta)) / (2 * valor1);

            raizA.value = resultadoRaiz1.toFixed(2);
            raizB.value = resultadoRaiz2.toFixed(2);

            break;

        default:
            return;
    }
}

function limpar() {
    document.getElementById("valorA").focus();
}

const fazercalc = document.querySelectorAll("[data-operacao]");

fazercalc.forEach(function (botao) {
    botao.addEventListener("click", function () {
        const operacao = botao.dataset.operacao;
        calculo(operacao);
    });
});

// Atualizado ID sem acentuação
const baskara = document.getElementById("equacao");

baskara.addEventListener("reset", function () {
    setTimeout(function () {
        limpar();
    }, 0);
});