const botao = document.getElementById("resultad");
const imagem = document.getElementById("signoimga");

botao.addEventListener("click", function () {
    const dia = parseInt(document.getElementById("dianasc").value);
    const mes = parseInt(document.getElementById("mesnasc").value);
    const ano = parseInt(document.getElementById("anonasc").value);

    const campoMes = document.getElementById("nomemes");
    const campoDia = document.getElementById("diasemana");
    const campoSigno = document.getElementById("signoimg");
    const campoIdade = document.getElementById("idad");

    campoMes.value = "";
    campoDia.value = "";
    campoSigno.value = "";
    campoIdade.value = "";
    imagem.src = "";

    const hoje = new Date();
    const anoAtual = hoje.getFullYear();

    if (isNaN(dia) || isNaN(mes) || isNaN(ano)) {
        alert("Preencha todos os campos corretamente.");
        return;
    }

    if (ano > anoAtual) {
        alert("O ano de nascimento não pode ser maior que o ano atual.");
        return;
    }

    if (ano < 1) {
        alert("Digite um ano de nascimento válido.");
        return;
    }

    if (mes < 1 || mes > 12) {
        alert("O mês deve estar entre 1 e 12.");
        return;
    }

    if (dia < 1 || dia > 31) {
        alert("O dia deve estar entre 1 e 31.");
        return;
    }

    const nascimento = new Date(ano, mes - 1, dia);

    if (
        nascimento.getDate() !== dia ||
        nascimento.getMonth() !== mes - 1 ||
        nascimento.getFullYear() !== ano
    ) {
        alert("A data informada não existe.");
        return;
    }

    let idade = anoAtual - ano;

    if (
        hoje.getMonth() < mes - 1 ||
        (hoje.getMonth() === mes - 1 && hoje.getDate() < dia)
    ) {
        idade--;
    }

    if (idade < 0) {
        alert("Erro: a idade calculada não pode ser negativa.");
        return;
    }

    const meses = [
        "Janeiro",
        "Fevereiro",
        "Março",
        "Abril",
        "Maio",
        "Junho",
        "Julho",
        "Agosto",
        "Setembro",
        "Outubro",
        "Novembro",
        "Dezembro"
    ];

    const dias = [
        "Domingo",
        "Segunda-feira",
        "Terça-feira",
        "Quarta-feira",
        "Quinta-feira",
        "Sexta-feira",
        "Sábado"
    ];

    let signo;

    if ((mes === 3 && dia >= 21) || (mes === 4 && dia <= 19)) {
        signo = "Áries";
        imagem.src = "Imagens/aries.jpg";

    } else if ((mes === 4 && dia >= 20) || (mes === 5 && dia <= 20)) {
        signo = "Touro";
        imagem.src = "Imagens/taurus.jpg";

    } else if ((mes === 5 && dia >= 21) || (mes === 6 && dia <= 20)) {
        signo = "Gêmeos";
        imagem.src = "Imagens/gemini.jpg";

    } else if ((mes === 6 && dia >= 21) || (mes === 7 && dia <= 22)) {
        signo = "Câncer";
        imagem.src = "Imagens/cancer.jpg";

    } else if ((mes === 7 && dia >= 23) || (mes === 8 && dia <= 22)) {
        signo = "Leão";
        imagem.src = "Imagens/leo.jpg";

    } else if ((mes === 8 && dia >= 23) || (mes === 9 && dia <= 22)) {
        signo = "Virgem";
        imagem.src = "Imagens/virgo.jpg";

    } else if ((mes === 9 && dia >= 23) || (mes === 10 && dia <= 22)) {
        signo = "Libra";
        imagem.src = "Imagens/libra.jpg";

    } else if ((mes === 10 && dia >= 23) || (mes === 11 && dia <= 21)) {
        signo = "Escorpião";
        imagem.src = "Imagens/scorpio.jpg";

    } else if ((mes === 11 && dia >= 22) || (mes === 12 && dia <= 21)) {
        signo = "Sagitário";
        imagem.src = "Imagens/sagittarius.jpg";

    } else if ((mes === 12 && dia >= 22) || (mes === 1 && dia <= 19)) {
        signo = "Capricórnio";
        imagem.src = "Imagens/Capricorn.jpg";

    } else if ((mes === 1 && dia >= 20) || (mes === 2 && dia <= 18)) {
        signo = "Aquário";
        imagem.src = "Imagens/Aquarius.jpg";

    } else {
        signo = "Peixes";
        imagem.src = "Imagens/pisces.jpg";
    }

    campoMes.value = meses[mes - 1];
    campoDia.value = dias[nascimento.getDay()];
    campoSigno.value = signo;
    campoIdade.value = idade + " anos";
});

