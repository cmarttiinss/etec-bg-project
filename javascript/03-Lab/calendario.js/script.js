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

const diasSemana = [
"Domingo",
"Segunda-feira",
"Terça-feira",
"Quarta-feira",
"Quinta-feira",
"Sexta-feira",
"Sábado"
];

let intervalo = null;

function exibirDataHora() {
const agora = new Date();

const dia = String(agora.getDate()).padStart(2, "0");
const mes = String(agora.getMonth() + 1).padStart(2, "0");
const ano = agora.getFullYear();

const hora = String(agora.getHours()).padStart(2, "0");
const minuto = String(agora.getMinutes()).padStart(2, "0");
const segundo = String(agora.getSeconds()).padStart(2, "0");

document.getElementById("dia").value = dia;
document.getElementById("mes").value = mes;
document.getElementById("ano").value = ano;

document.getElementById("nomeMes").value =
    meses[agora.getMonth()];

document.getElementById("hora").value = hora;
document.getElementById("minuto").value = minuto;
document.getElementById("segundo").value = segundo;

document.getElementById("diaSemana").value =
    diasSemana[agora.getDay()];


}

// Inicia o relógio
function iniciarRelogio() {

// Evita criar vários setInterval
if (intervalo !== null) {
    return;
}

exibirDataHora();

intervalo = setInterval(exibirDataHora, 1000);


}

// Para o relógio
function pararRelogio() {

if (intervalo !== null) {
    clearInterval(intervalo);
    intervalo = null;
}


}

// Limpa os campos
function limparCampos() {

pararRelogio();

document.querySelectorAll("input").forEach((campo) => {
    campo.value = "";
});


}

// Eventos dos botões
document
.getElementById("exibir")
.addEventListener("click", iniciarRelogio);

document
.getElementById("parar")
.addEventListener("click", pararRelogio);

document
.getElementById("limpar")
.addEventListener("click", limparCampos);