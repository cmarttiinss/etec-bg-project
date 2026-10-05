class Carro {
  // atributos: características 
  late String modelo;
  int veloAtual = 60;
  late int veloMax;
  bool ligado = false;
  // métodos
  void ligar() {
    ligado = true;
  }

  // frear: diminui a velocidade do carro
  void frear(int qtd) {
    veloAtual -= qtd;
    veloAtual = veloAtual < 0 ? 0 : veloAtual;
  }

  //carro deve estar ligado
  // acelerar: aumenta a velocidade do carro
  void acelerar(int qtd) {
    if (ligado) {
      veloAtual += qtd;
      veloAtual = veloAtual > veloMax ? veloMax : veloAtual;
    } 
    else {
      print("Carro desligado, não é possível acelerar");
    }
  }

  
}