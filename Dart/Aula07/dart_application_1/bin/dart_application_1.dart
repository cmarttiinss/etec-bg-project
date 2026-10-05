import 'carro.dart';

void main (List<String> arguments) {
  // instanciem uma classe carro
  Carro c1 = Carro(); // c1 é nome da instância ou objeto 
  // atribua um modelo
  c1.modelo = "Fusca";
  c1.veloMax = 100;  

  // acelere sem ligar o carro
  c1.acelerar(50);
  // ligue
  c1.ligar();
  //acelere sem passar a velocidade maxima 
  c1.acelerar(100);
  print("Velocidade atual: ${c1.veloAtual}");
  //acelere ultrapassando a velo max 
  c1.acelerar(50);
  print("Velocidade maxima ultrapassada: ${c1.veloAtual}");
  
  // freie sem chegar ao zero
  c1.frear(50);
  print("Velocidade atual: ${c1.veloAtual}");
  
  // freie ultrapassando o zero 
  c1.frear(100);
  print("Velocidade atual: ${c1.veloAtual}");  

}