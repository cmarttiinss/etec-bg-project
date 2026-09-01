function Somar(){
    var num1=parseFloat(document.formularioSoma.tnum1.value);
    var num2=parseFloat(document.formularioSoma.tnum2.value);

    if(isNaN(num1) || isNaN(num2)){
        alert("Digite valores válidos.");
        return;
    }

    document.formularioSoma.tresu.value=num1+num2;
}

function Limpar(){
    document.formularioSoma.tnum1.focus();
}

function calculo(){
    var peso=parseFloat(document.getElementById("peso").value);
    var altura=parseFloat(document.getElementById("altu").value);

    if(isNaN(peso) || isNaN(altura)){
        alert("Preencha os campos corretamente.");
        return;
    }

    var imc=peso/(altura*altura);
    document.getElementById("resu").value=imc.toFixed(2);
}

function Exibe_Resposta(x,y){
    if(document.getElementById(x).className.indexOf("exibida")==-1){
        document.getElementById(x).className=
        document.getElementById(x).className.replace("escondida","exibida");

        document.getElementById(y).className=
        document.getElementById(y).className.replace("seta_final","seta_inicial");
    }else{
        document.getElementById(x).className=
        document.getElementById(x).className.replace("exibida","escondida");

        document.getElementById(y).className=
        document.getElementById(y).className.replace("seta_inicial","seta_final");
    }
}

function Troca_cor(){
    document.bgColor=document.getElementById("cor").value;
}