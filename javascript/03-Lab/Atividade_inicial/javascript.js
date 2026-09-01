function calculo() {
    var vpeso=document.getElementById("peso").value;
    var valtu=document.getElementById("altu").value;
    var vresu=vpeso/(valtu*valtu);
    document.getElementById("resu").value=vresu.toFixed(2);
}