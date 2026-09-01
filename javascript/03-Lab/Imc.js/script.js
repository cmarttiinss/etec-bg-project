function calculadora() {

var peso = parseFloat(document.getElementById("peso").value);
var altura = parseFloat(document.getElementById("altu").value);
var genero = document.querySelector('input[name="genero"]:checked');

if (!genero || isNaN(peso) || isNaN(altura) || peso <= 0 || altura <= 0) {
    document.getElementById("Yimc").value = "Inserir valores válidos";
    document.getElementById("Yimc").style.color = "red";
    return;
}

var imc = peso / (altura * altura);
var classificacao = "";
var pesoIdeal = "";

if (genero.value === "Masculino") {

    if (imc > 39.9) {
        classificacao = "Obesidade Morbida";
    } else if (imc >= 30 && imc <= 39.9) {
        classificacao = "Obesidade Moderada";
    } else if (imc >= 25 && imc <= 29.9) {
        classificacao = "Obesidade Leve";
    } else if (imc >= 20 && imc <= 24.9) {
        classificacao = "Peso Normal";
    } else {
        classificacao = "Abaixo do Peso";
    }

    var pesoMin = 20 * (altura * altura);
    var pesoMax = 24.9 * (altura * altura);

    pesoIdeal =
        pesoMin.toFixed(1) +
        "kg até " +
        pesoMax.toFixed(1) +
        "kg";
}

if (genero.value === "Feminino") {

    if (imc > 38.9) {
        classificacao = "Obesidade Morbida";
    } else if (imc >= 29 && imc <= 38.9) {
        classificacao = "Obesidade Moderada";
    } else if (imc >= 24 && imc <= 28.9) {
        classificacao = "Obesidade Leve";
    } else if (imc >= 19 && imc <= 23.9) {
        classificacao = "Peso Normal";
    } else {
        classificacao = "Abaixo do Peso";
    }

    var pesoMin = 19 * (altura * altura);
    var pesoMax = 23.9 * (altura * altura);

    pesoIdeal =
        pesoMin.toFixed(1) +
        "kg até " +
        pesoMax.toFixed(1) +
        " kg";
}

document.getElementById("Yimc").value = imc.toFixed(2);
document.getElementById("TxtImc").value = classificacao;
document.getElementById("PesoId").value = pesoIdeal;

}