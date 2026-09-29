import 'conta_corrente.dart';

void main(List<String> arguments) {
  ContaCorrente conta1 = ContaCorrente();
  conta1.titular = "Cauã Martins do Nascimento";
  conta1.agencia = 1234;
  conta1.saldo = 1000;

  conta1.sacar(5000);
  print('Saldo atual: R\$ ${conta1.saldo}\n');

  ContaCorrente conta2 = ContaCorrente();
  conta2.titular = "Enzo Chaves";
  conta2.agencia = 12345;
  conta2.saldo = 2000;

  conta2.depositar(600);
  print('Saldo de ${conta2.titular} : ${conta2.saldo}'); // 2600
  conta2.sacar(1000); //certo
  conta2.sacar(7000); //Sem saldo
}