void main() {
  Exercicio01();
  Exercicio02();
  Exercicio03();
  Exercicio04();
  Exercicio05();
}

void Exercicio01() {
  Map<String, String> Estados = {
    'ES': "Espírito Santo",
    'MG': "Minas Gerais",
    'RJ': "Rio de Janeiro",
    'SP': "São Paulo",
  };
}

void Exercicio02() {
  Map<String, String> Estados = {
    'ES': "Espírito Santo",
    'MG': "Minas Gerais",
    'RJ': "Rio de Janeiro",
    'SP': "São Paulo",
  };

  print(Estados['ES']);
}

void Exercicio03() {
  Map<String, String> Estados = {
    'ES': "Espírito Santo",
    'MG': "Minas Gerais",
    'RJ': "Rio de Janeiro",
    'SP': "São Paulo",
  };

  Estados['BA'] = "Bahia";
  Estados['PR'] = "Paraná";

  print(Estados);
}

void Exercicio04() {
  Map<String, String> Estados = {
    'ES': "Espírito Santo",
    'MG': "Minas Gerais",
    'RJ': "Rio de Janeiro",
    'SP': "São Paulo",
  };
  for (var sigla in Estados.keys)
  print("${Estados[sigla]}");
}

void Exercicio05() {
  Map<String, String> filme= {
    'titulo': "Batman Dark Knight", 
    'Data de Lançamento': "18/07/2008",
    'Direção': "Christopher Nolan",
    'Genero': "Ação/Suspense",
  };
  
  print('${filme['titulo']} - Data de Lançamento ${filme['Data de Lançamento']} - Direção ${filme['Direção']} - Genero ${filme['Genero']}');
}




