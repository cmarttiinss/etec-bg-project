import 'dart:io';
import 'personagem.dart';

class Mago extends Personagem {
  late int mana;

  // Precisa passar os atributos do construtor da classe Mãe
  // Super: Construtor da classe Mãe
  Mago(String nome) :super(nome, 100, 30, 20, 20);
   
  @override // reescrita opcional 
  void saudacao() {
    print('Olá, meu nome é $nome. Eu sou um mago!');
  }
  
  @override // reescrita obrigdatória porque é um método abstrato da classe mãe 
  void especial() {
    print('O mago conjura uma poderosa magia de ataque!'); // Não tem corpo
  }
} 