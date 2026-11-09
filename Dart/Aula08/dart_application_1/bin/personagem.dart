// Classe abstrata: não pode ser instanciada 
// Serve para ser o molde das suas classes filhas 
import 'dart:io';

abstract class Personagem {
  late String nome;
  late int vida;
  late int forca;
  late int defesa;
  late int ataque;

  Personagem(this.nome, this.vida, this.forca, this.defesa, this.ataque);

  @override
  String toString() {
   return 'Personagem: $nome, Vida: $vida, Força: $forca, Defesa: $defesa, Ataque: $ataque';
  }

  void saudacao() {
    print('Olá, meu nome é $nome.');
  }

  //Méodo abstrato: precisa ser reescrito nas classes filhas !!!
  void especial() {
    print('O personagem realiza um $ataque especial!'); // Não tem corpo, apenas a assinatura do método
  } 
}