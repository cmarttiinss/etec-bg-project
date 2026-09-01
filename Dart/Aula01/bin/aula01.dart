void main() {
exemplo1();
exemplo2();
exemplo3();
}

void exemplo2() {
  // Troca de valores
  int v1 = 9; 
  int v2 = 6;

  v1 = v2 + v2;
  v2 = v1 - v2;
  v1 = v1 - v2;

  print('Olá $v1 $v2 \n');
}

void exemplo3() {
  int valor = 1; 
  
  int n100 = 0;
  int n50 = 0;
  int n20 =0; 
  int n10 =0; 
  int n5 =0;
  int n2 =0;

  n100 = (valor / 100).toInt();
  valor = valor % 100; 

  n50 = (valor / 50).toInt();
  valor = valor % 50;

  n20 = (valor / 20).toInt();
  valor = valor % 20;

  n10 = (valor / 10).toInt();
  valor = valor % 10;

  n5 = (valor / 5).toInt();
  valor = valor % 5;

  n2 = (valor / 2).toInt();
  valor = valor % 2;

  print('Notas de 100: $n100');
  print('Notas de 50: $n50');
  print('Notas de 20: $n20');
  print('Notas de 10: $n10');
  print('Notas de 5: $n5');
  print('Notas de 2: $n2');
  print('Valor restante: $valor \n');

} 

void exemplo1(){
  String nome = 'zinho';
  int matricula = 12345;
  double salario = 10000;
  bool aprovado = true;

  print(nome);
  print(matricula);
  print(salario);
  print("$aprovado \n");
}
