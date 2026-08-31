void main() {
  exemplo1();
  exemplo2();
  exemplo3();
}

void exemplo1(){
  // Dada a nota, imprima o conceito 
  // >= 9 -> MB  >= 7 -> B  >= 5 -> R  <5 -> I      

  double nota = 9;
if (nota >=11){
    print("Voce Tirou uma nota inexistente !!!");
  }
else if(nota >=9){
    print("Parabens, voce tirou a nota maxima 'MB' !!!");
  }
else if(nota >=7){
    print("Boa, Voce tirou nota 'B' !");
  }
else if (nota >=5){
    print("Voce Tirou a menor nota que tem, 'I' ");
  }
else{
  }
}

void exemplo2(){     
// and: &&
// dada a nota e faltas, imrpima: 
// aprovada: se nota >= 6 e faltas < 21 
// reprovado: caso contrário 

  double nota = 9;
  int faltas = 21;

if (nota >=9 && faltas <21){
    print('Voce foi Aprovado !!!');
  }
else{
    print ('Voce foi Reprovado !!!');
  }
}

void exemplo3(){
  // ou: || pipe 
  // uma pessoa pode entrar em uma festa se:
  // tiver for maior de idade
  // ou se for amigoDoDono 
  // declare as variáveis com tipo adequados
  // e imprima se pode ou não entrar na festa 

 int idade =18; 
 bool amigoDoDono = true;

  if(idade >= 18 || amigoDoDono == true ) {
    print ('Pessoa poderá entrar na festa');
  }else{ 
    print('Pessoa Não poderá entrar na festa');
  }
}

void exemplo4(){
  //dados 3 números inteiros diferentes, imprima o maior 
  int v1 = 65, v2 = 9, v3 = 15;
  //dica: meio trabalhoso 
  if (v1> v2 && v1 > v3){
    print('Maior: $v1');
  }
}