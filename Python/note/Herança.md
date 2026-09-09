# 🌳 Herança

## 📚 Índice
1. [O que é Herança](#o-que-é-herança)
2. [Tipos de Herança](#tipos-de-herança)
3. [Sintaxe e Conceitos](#sintaxe-e-conceitos)
4. [Super()](#super)
5. [Exemplos Práticos](#exemplos-práticos)
6. [Boas Práticas](#boas-práticas)

---

## 🎯 O que é Herança?

**Herança** é um mecanismo da POO que permite que uma classe **herde características (atributos e métodos)** de outra classe.

### 🎓 Analogia

```
Ser Vivo (Classe Pai)
    ↓ herda
Animal (Classe Filha)
    ↓ herda
Mamífero (Classe Filha)
    ↓ herda
Cachorro (Classe Filha)
```

### 🔑 Conceitos

| Termo | 📝 Definição |
|---|---|
| **Classe Pai / Superclasse** | Classe que será herdada |
| **Classe Filha / Subclasse** | Classe que herda |
| **Herança** | Ato de compartilhar características |
| **Sobrescrita** | Redefinir método da classe pai |

---

## 🌳 Tipos de Herança

### 1️⃣ Herança Simples

Uma classe filha herda de **uma** classe pai.

```python
class Animal:  # Classe Pai
    def fazer_som(self):
        return "Som genérico"

class Gato(Animal):  # Classe Filha herda de Animal
    def fazer_som(self):
        return "Miau!"

gato = Gato()
print(gato.fazer_som())  # Miau!
```

**Estrutura:**
```
    Animal
      ↑
      |
     Gato
```

---

### 2️⃣ Herança Multinível

Cadeia de herança: Avó → Mãe → Filha

```python
class SerVivo:  # Classe Avó
    def respirar(self):
        return "Respirando..."

class Animal(SerVivo):  # Classe Mãe
    def fazer_som(self):
        return "Som"

class Cachorro(Animal):  # Classe Filha
    def fazer_som(self):
        return "Au au!"

dog = Cachorro()
print(dog.respirar())  # Respirando... (herança da avó)
print(dog.fazer_som())  # Au au!
```

**Estrutura:**
```
    SerVivo
      ↑
      |
    Animal
      ↑
      |
   Cachorro
```

---

### 3️⃣ Herança Múltipla

Uma classe filha herda de **múltiplas** classes pai.

```python
class Terrestre:
    def andar(self):
        return "Andando..."

class Aquático:
    def nadar(self):
        return "Nadando..."

class Anfíbio(Terrestre, Aquático):  # Herança de duas classes
    pass

sapo = Anfíbio()
print(sapo.andar())  # Andando...
print(sapo.nadar())  # Nadando...
```

**Estrutura:**
```
Terrestre    Aquático
     \        /
      \      /
       Anfíbio
```

⚠️ **Cuidado:** Pode ficar complexa. Use com moderação!

---

### 4️⃣ Herança Hierárquica

Múltiplas classes herdam da **mesma** classe pai.

```python
class Veiculo:  # Classe Pai
    def acelerar(self):
        return "Acelerando..."

class Carro(Veiculo):  # Filha 1
    pass

class Moto(Veiculo):  # Filha 2
    pass

class Bicicleta(Veiculo):  # Filha 3
    pass
```

**Estrutura:**
```
         Veiculo
       /    |    \
    Carro  Moto  Bicicleta
```

---

## 🔧 Sintaxe e Conceitos

### Sintaxe Básica

```python
class ClassePai:
    def metodo_pai(self):
        return "Do pai"

class ClasseFilha(ClassePai):  # ← Herança
    def metodo_filho(self):
        return "Do filho"

filha = ClasseFilha()
print(filha.metodo_pai())   # ✅ Do pai (herdado)
print(filha.metodo_filho()) # ✅ Do filho (próprio)
```

### Verificar Herança

```python
class Animal:
    pass

class Cachorro(Animal):
    pass

dog = Cachorro()

# Verificar se é instância
print(isinstance(dog, Cachorro))  # True
print(isinstance(dog, Animal))    # True

# Verificar classe
print(Cachorro.__bases__)  # (<class 'Animal'>,)

# Verificar MRO (Method Resolution Order)
print(Cachorro.mro())  # [Cachorro, Animal, object]
```

---

## 🔄 Super()

O método `super()` acessa métodos e atributos da **classe pai**.

### Quando Usar?

✅ Para chamar método da classe pai  
✅ Para evitar duplicação de código  
✅ Para estender funcionalidade

### Exemplos

```python
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def descrever(self):
        return f"{self.marca} {self.modelo}"

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)  # Chama __init__ do pai
        self.portas = portas
    
    def descrever(self):
        desc_pai = super().descrever()  # Chama método do pai
        return f"{desc_pai} com {self.portas} portas"

carro = Carro("Toyota", "Corolla", 4)
print(carro.descrever())
# Toyota Corolla com 4 portas
```

### Herança Múltipla com Super()

```python
class Caminhao(Veiculo, Pesado):  # Múltiplas heranças
    def __init__(self, marca, modelo, carga_maxima):
        super().__init__(marca, modelo)
        Pesado.__init__(self, carga_maxima)
        # ou: super().__init__(carga_maxima) dependendo do MRO
```

---

## 💻 Exemplos Práticos

### Exemplo 1: Sistema de Funcionários

```python
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self._salario = salario  # Protegido
    
    def obter_salario(self):
        return self._salario
    
    def trabalhar(self):
        return f"{self.nome} está trabalhando..."

class Gerente(Funcionario):  # Herança simples
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento
    
    def supervisionar(self):
        return f"Gerente {self.nome} supervisionando {self.departamento}"

class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem
    
    def programar(self):
        return f"{self.nome} programando em {self.linguagem}"

# Uso
func = Funcionario("João", 3000)
print(func.trabalhar())  # João está trabalhando...

gerente = Gerente("Maria", 5000, "TI")
print(gerente.supervisionar())  # Gerente Maria supervisionando TI
print(gerente.trabalhar())  # Maria está trabalhando... (herdado)

dev = Desenvolvedor("Pedro", 4000, "Python")
print(dev.programar())  # Pedro programando em Python
```

---

### Exemplo 2: Formas Geométricas

```python
import math

class Forma:  # Classe Pai
    def __init__(self, cor):
        self.cor = cor
    
    def descrever(self):
        return f"Forma de cor {self.cor}"

class Retangulo(Forma):  # Filha 1
    def __init__(self, cor, largura, altura):
        super().__init__(cor)
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura
    
    def descrever(self):
        area = self.calcular_area()
        return f"{super().descrever()} - Retângulo {self.largura}x{self.altura}, área={area}"

class Circulo(Forma):  # Filha 2
    def __init__(self, cor, raio):
        super().__init__(cor)
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * (self.raio ** 2)
    
    def descrever(self):
        area = self.calcular_area()
        return f"{super().descrever()} - Círculo raio={self.raio}, área={area:.2f}"

# Uso
formas = [
    Retangulo("vermelho", 5, 3),
    Circulo("azul", 4)
]

for forma in formas:
    print(forma.descrever())
    print(f"Área: {forma.calcular_area():.2f}\n")
```

**Saída:**
```
Forma de cor vermelho - Retângulo 5x3, área=15
Área: 15.00

Forma de cor azul - Círculo raio=4, área=50.27
Área: 50.27
```

---

### Exemplo 3: Veículos (Multinível)

```python
class Veiculo:
    def __init__(self, marca, velocidade_max):
        self.marca = marca
        self.velocidade_max = velocidade_max
    
    def acelerar(self):
        return f"Acelerando até {self.velocidade_max} km/h"

class VeiculoTerrestre(Veiculo):
    def __init__(self, marca, velocidade_max, rodas):
        super().__init__(marca, velocidade_max)
        self.rodas = rodas

class Carro(VeiculoTerrestre):
    def __init__(self, marca, velocidade_max, rodas, portas):
        super().__init__(marca, velocidade_max, rodas)
        self.portas = portas
    
    def descrever(self):
        return f"{self.marca} com {self.portas} portas e {self.rodas} rodas"

# Uso
carro = Carro("Honda", 200, 4, 4)
print(carro.descrever())  # Honda com 4 portas e 4 rodas
print(carro.acelerar())   # Acelerando até 200 km/h
```

---

## ✅ Boas Práticas

| 🎯 Prática | ✅ Faça | ❌ Evite |
|---|---|---|
| **Profundidade** | Máx 3-4 níveis | Hierarquias muito profundas |
| **Responsabilidade** | Cada classe tem seu papel | Classes genéricas demais |
| **Documentação** | Documente o motivo da herança | Deixe implícito |
| **Composição** | Às vezes melhor que herança | Herança para tudo |
| **Super()** | Use para chamar pai | Ignore o pai |
| **Testes** | Teste cada nível | Teste só no final |

---

## 🌳 Quando Usar Herança vs Composição

### Herança (É um)
```python
# Cachorro IS-A (é um) Animal
class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):  # ✅ Herança apropriada
    def fazer_som(self):
        return "Au au!"
```

### Composição (Tem um)
```python
# Carro HAS-A (tem um) Motor
class Motor:
    def ligar(self):
        return "Motor ligado"

class Carro:
    def __init__(self):
        self.motor = Motor()  # ✅ Composição apropriada
    
    def ligar(self):
        return self.motor.ligar()
```

---

## 📊 Resumo Rápido

```python
# Herança Simples
class Pai:
    pass

class Filho(Pai):
    pass

# Super()
class Filho(Pai):
    def __init__(self):
        super().__init__()

# Verificar Herança
isinstance(objeto, Classe)  # True/False
Classe.__bases__            # Classes pai

# MRO (Ordem de resolução)
Classe.mro()  # Ordem de busca
```

---

**Última atualização:** 📅 2026-06-16  
**Nível:** 🎓 Intermediário
