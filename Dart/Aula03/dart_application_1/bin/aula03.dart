void main (List<String>arguments){
  exemplo1();
  exemplo2();
  exemplo3();
  exemplo4();
}
    
void exemplo1 (){
    //Switch case: casi especifico de condicional
    //sempre verifica apenas UMA variavel 
    // sempre verifica a mesma variavel 
    //sempre usa igualdade

String estado = 'SP';
    switch (estado){
    case 'sp':
        print('São Paulo');
        break;
    case 'rj':
        print('Rio de Janeiro');
        break;
    case 'es':
        print('Espiríto Santo');
        break;  
    }
}
    
void exemplo2 (){
    //dado o número do mes, imprima seu nome
    //exemplo: mes = 2 => Fevereiro
    //caso não exista o mes, imprima Mes Inválido
    String mes = '5';
    switch(mes){
        case '1':
            print('Janeiro');
            break;
        case '2':
            print('Fevereiro');
            break;
        case '3':
            print('Março');
            break;
        case '4':
            print('Abril');
            break;
        case '5':
            print('Maio');
            break;
        case '6':
            print('Junho');
            break;
        case '7':
            print('Julho');
            break;
        case '8':
            print('Agosto');
            break;
        case '9':
            print('Setembro');
            break;
        case '10':
            print('Outubro');
            break;
        case '11':
            print('Novembro');
            break;
        case '12':
            print('Dezembro');
            break;
        default:
            print('Mês inválido');
    }
}
    void exemplo3 (){
      //operador ternário
      int nota = 7;
      if(nota >=7){
        print('Aprovado');
      }else{
        print('Reprovado');
      }

      //equivalente com ternário 
      nota >= 7 ? print('Aprovado 2') : print('Reprovado');
      //condição ? valorSeVdd : valorSeFalso
      }

      void exemplo4 (){
        //dada a variável login do tipo string
        //mova 'logado' se senhas iguais, 'se senhas iguais
        //senao mova 'invalido', se senhas diferentes
      }

  