const botao =document.getElementById("resultad");
const imagem = document.getElementById("imagem_signo");

botao.addEventListener("click", function(){
    const dia = parseInt(document.getElementById("data_nasc").value);
    const mes = parseInt(document.getElementById("data_mes").value);
    const ano = parseInt(document.getElementById("data_ano").value);

    const campoMes = document.getElementById("nome_mes");
    const campoDiaSemana = document.getElementById("dia_semana");
    const campoSignoMes = document.getElementById("signoimg");
    const campoIdade = document.getElementById("idade");

    campoMes.value = "";
    campoDiaSemana.value = "";
    campoSignoMes.value = "";
    campoIdade.value = "";

    const hoje = new Date();
    const anoAtual = hoje.getFullYear();

if (IsNaN(dia) || IsNaN(mes) || IsNaN(ano)) {
    alert("Preencher todos os campos de forma correta");
    return;
}
if (ano > anoatual) {
    alert("O ano de nascimento não pode ser maior que o ano atual.");
    return;
}
if (ano < 1){
    alert("Digite um ano de nascimento válido.");
    return;
}
if ( mes < 1 || mes > 12){
    alert("Digite um mes de nascimento válido, dentre 1 e 12.");
    return;
}
if (dia < 1 || dia > 31){
    alert("Digite um dia válido, dentre 1 e 31.")
}

const nascimento = new Date(ano, mes - 1, dia);

if (
    nascimento.getDate() !== dia ||
    nascimento.getMonth() !== mes -1 ||
    nascimento.getYear() !== ano 
) {
    alert("A data que foi infomada não é existente");
    return;
}

let idade = anoAtual - ano; 

if (
    hoje.getMonth() < mes - 1 ||
    (hoje.getMonth() === mes - 1 && hoje.getDate() <dia)
 ) {
    idade--;
 }
 
 if (idade < 0) {
    alert("Erro! A idade calculada não pode ser negativa")
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

 const Dias = [
    "Domingo",
    "Segunda-Feira",
    "Terça-Feira",
    "Quarta-Feira",
    "Quinta-Feira",
    "Sexta-Feira",
    "Sábado"
 ];

 let signo;

 if((mes === 12 && dia >=22 ) || (mes === 1 && dia <=20)){
    signo ="Capricornio";
    imagem.src =""
}else if ((mes === 1 && dia >= 21) || (mes === 2 && dia <= 19)){
    signo ="Aquario";
    imagem.src=""
}else if ((mes === 2 && dia >= 20) || (mes === 3 && dia <= 20 )){
    signo ="Peixes";
    imagem.src="" 
}else if ((mes === 3 && dia >= 21) || (mes === 4 && dia <= 20 )){
    signo ="";
    imagem.src=""
}else if ((mes === 4 && dia >= 21) || (mes === 5 && dia <= 20 )){
    signo ="";
    imagem.src=""
}else if ((mes === 3 && dia >= 21) || (mes === 4 && dia <= 20 )){
    signo ="";
    imagem.src=""
}else if ((mes === 3 && dia >= 21) || (mes === 4 && <= 20 )){
    signo ="";
    imagem.src=""
}else if ((mes === 3 && dia >= 21) || (mes === 4 && <= 20 )){
    signo ="";
    imagem.src=""
}else if ((mes === 3 && dia >= 21) || (mes === 4 && <= 20 )){
    signo ="";
    imagem.src=""
}else if ((mes === 3 && dia >= 21) || (mes === 4 && <= 20 )){
    signo ="";
    imagem.src=""
}else if ((mes === 3 && dia >= 21) || (mes === 4 && <= 20 )){
    signo ="";
    imagem.src=""
}else if ((mes === 3 && dia >= 21) || (mes === 4 && <= 20 )){
    signo ="";
    imagem.src=""



    
})

