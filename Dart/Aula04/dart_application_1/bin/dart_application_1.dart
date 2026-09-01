void main() { 
  exemplo1();
  exemplo2(); 
  exemplo3();

}

void exemplo1() {
  print('Inicio método 1');
  
  for (int i = 0; i < 10; i++){
    print('Valor de i? $i');
  }
    print('Fim método 1');
} 


void exemplo2() {
  //fatorial 
  int n = 6;
  //fat = 6 * 5 * 4 * 3 * 2 * 1 
  int fatorial = 1;
  print('Inicio método 2');
  for (int i = n; i >= 2; i--){
    fatorial = fatorial * i;
  }
    print('fatorial de $n é $fatorial');
}

void exemplo3(){
  for (int i = 100; i >=0; i--){
    print(i);
  }
}



