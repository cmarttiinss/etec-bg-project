# 🎭 Polimorfismo

## 📚 Índice
1. [O que é Polimorfismo](#o-que-é-polimorfismo)
2. [Tipos de Polimorfismo](#tipos-de-polimorfismo)
3. [Duck Typing](#duck-typing)
4. [Exemplos Práticos](#exemplos-práticos)
5. [Boas Práticas](#boas-práticas)

---

## 🎯 O que é Polimorfismo?

**Polimorfismo** significa **"muitas formas"**. 

> 🎭 É a capacidade de um método ou função responder de **formas diferentes** dependendo do contexto ou do tipo de objeto.

### Analogia

```
Gato, Cão e Pássaro são todos Animais
Todos entendem o comando: "fazer_som()"
Mas cada um responde diferente:
  🐱 Gato → "Miau!"
  🐕 Cão → "Au au!"
  🦅 Pássaro → "Piu piu!"
```

---

## 🔄 Tipos de Polimorfismo

### 1️⃣ Sobrescrita (Override)

Um método filha **redefine** um método da classe pai.

```python
class Animal:
    def fazer_som(self):
        return "Som genérico"

class Cachorro(Animal):
    def fazer_som(self):  # 🔄 Sobrescreve
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):  # 🔄 Sobrescreve
        return "Miau!"

# Uso
dog = Cachorro()
cat = Gato()

print(dog.fazer_som())  # Au au!
print(cat.fazer_som())  # Miau!
```

**Estrutura:**
```
Animal.fazer_som() → "Som genérico"
    ↑
    ├─ Cachorro.fazer_som() → "Au au!"
    │
    └─ Gato.fazer_som() → "Miau!"
```

---

### 2️⃣ Sobrecarga (Overload)

Mesmo método com **parâmetros diferentes**.

⚠️ **Python não suporta nativamente!** Mas pode simular:

```python
# ❌ Não funciona em Python
class Calculadora:
    def somar(self, a, b):
        return a + b
    
    def somar(self, a, b, c):  # ❌ Sobrescreve anterior!
        return a + b + c

calc = Calculadora()
# calc.somar(2, 3)  # ❌ Erro!
```

#### ✅ Solução: Argumentos Default

```python
class Calculadora:
    def somar(self, a, b, c=0):  # c opcional
        return a + b + c

calc = Calculadora()
print(calc.somar(2, 3))      # 5
print(calc.somar(2, 3, 4))   # 9
```

#### ✅ Solução: *args

```python
class Calculadora:
    def somar(self, *numeros):  # Qualquer quantidade
        return sum(numeros)

calc = Calculadora()
print(calc.somar(2, 3))        # 5
print(calc.somar(2, 3, 4, 5))  # 14
```

---

### 3️⃣ Duck Typing

"Se parece com pato, nada como pato e grasna como pato, **é um pato!**"

> 🦆 **Tipo não é importante, comportamento é!**

```python
# Sem herança explícita
class Pato:
    def fazer_som(self):
        return "Quack!"

class Pessoa:
    def fazer_som(self):
        return "Olá!"

class Máquina:
    def fazer_som(self):
        return "Beeep!"

# Todos funcionam com a mesma função
def fazer_barulho(ser):
    print(ser.fazer_som())

fazer_barulho(Pato())      # Quack!
fazer_barulho(Pessoa())    # Olá!
fazer_barulho(Máquina())   # Beeep!
```

**Vantagem:** Flexibilidade máxima!

---

### 4️⃣ Polimorfismo Paramétrico (Genéricos)

Mesmo código funciona com **tipos diferentes**.

```python
def imprimir_lista(lista):
    """Funciona com qualquer tipo de lista"""
    for item in lista:
        print(item)

# Funciona com inteiros
imprimir_lista([1, 2, 3])

# Funciona com strings
imprimir_lista(["a", "b", "c"])

# Funciona com objetos
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        return self.nome

pessoas = [Pessoa("João"), Pessoa("Maria")]
imprimir_lista(pessoas)
```

---

## 🦆 Duck Typing em Profundidade

### Exemplo: Sistema de Pagamentos

```python
# Nenhuma herança! Só "interfaces" implícitas

class CartaoCredito:
    def processar_pagamento(self, valor):
        return f"Pagamento de R${valor} no cartão"

class Boleto:
    def processar_pagamento(self, valor):
        return f"Boleto gerado para R${valor}"

class Criptomoeda:
    def processar_pagamento(self, valor):
        return f"Transferência de {valor} moedas"

# Função genérica que aceita qualquer método de pagamento
def realizar_compra(metodo_pagamento, valor):
    print(metodo_pagamento.processar_pagamento(valor))

# Uso - Polimorfismo puro!
realizar_compra(CartaoCredito(), 100)      # Cartão
realizar_compra(Boleto(), 100)             # Boleto
realizar_compra(Criptomoeda(), 100)        # Cripto
```

### Verificar Capacidade (Antes de Usar)

```python
def realizar_pagamento(metodo, valor):
    # Verificar se tem o método
    if hasattr(metodo, 'processar_pagamento'):
        print(metodo.processar_pagamento(valor))
    else:
        print("Método de pagamento inválido!")

# Uso
realizar_pagamento(CartaoCredito(), 50)
```

---

## 💻 Exemplos Práticos

### Exemplo 1: Sistema de Animais

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        """Será sobrescrito"""
        pass
    
    def mover(self):
        """Será sobrescrito"""
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return f"{self.nome}: Au au!"
    
    def mover(self):
        return f"{self.nome} está correndo"

class Gato(Animal):
    def fazer_som(self):
        return f"{self.nome}: Miau!"
    
    def mover(self):
        return f"{self.nome} está pulando"

class Passaro(Animal):
    def fazer_som(self):
        return f"{self.nome}: Piu piu!"
    
    def mover(self):
        return f"{self.nome} está voando"

# Polimorfismo em ação!
animais = [
    Cachorro("Rex"),
    Gato("Whiskers"),
    Passaro("Tweety")
]

# Mesmo método, respostas diferentes
for animal in animais:
    print(animal.fazer_som())   # Diferentes sons!
    print(animal.mover())       # Diferentes movimentos!
    print()
```

**Saída:**
```
Rex: Au au!
Rex está correndo

Whiskers: Miau!
Whiskers está pulando

Tweety: Piu piu!
Tweety está voando
```

---

### Exemplo 2: Formas com Cálculo de Área

```python
import math

class Forma:
    def calcular_area(self):
        pass
    
    def calcular_perimetro(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2
    
    def calcular_perimetro(self):
        return 4 * self.lado

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return (self.base * self.altura) / 2
    
    def calcular_perimetro(self):
        return self.base + self.altura + math.sqrt(self.base**2 + self.altura**2)

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * (self.raio ** 2)
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

# Polimorfismo
formas = [
    Quadrado(5),
    Triangulo(3, 4),
    Circulo(2)
]

# Mesma função, comportamentos diferentes
def exibir_metricas(forma):
    print(f"Área: {forma.calcular_area():.2f}")
    print(f"Perímetro: {forma.calcular_perimetro():.2f}\n")

for forma in formas:
    exibir_metricas(forma)
```

---

### Exemplo 3: Sistemas de Notificação

```python
class Notificador:
    def enviar(self, mensagem):
        pass

class Email(Notificador):
    def enviar(self, mensagem):
        return f"📧 Email: {mensagem}"

class SMS(Notificador):
    def enviar(self, mensagem):
        return f"📱 SMS: {mensagem}"

class Telegram(Notificador):
    def enviar(self, mensagem):
        return f"✈️ Telegram: {mensagem}"

class Discord(Notificador):
    def enviar(self, mensagem):
        return f"🎮 Discord: {mensagem}"

# Sistema genérico
class SistemaNotificacoes:
    def __init__(self):
        self.notificadores = []
    
    def adicionar(self, notificador):
        self.notificadores.append(notificador)
    
    def notificar_todos(self, mensagem):
        for notificador in self.notificadores:
            print(notificador.enviar(mensagem))

# Uso
sistema = SistemaNotificacoes()
sistema.adicionar(Email())
sistema.adicionar(SMS())
sistema.adicionar(Telegram())
sistema.adicionar(Discord())

sistema.notificar_todos("Pedido confirmado!")
```

**Saída:**
```
📧 Email: Pedido confirmado!
📱 SMS: Pedido confirmado!
✈️ Telegram: Pedido confirmado!
🎮 Discord: Pedido confirmado!
```

---

## ✅ Boas Práticas

| 🎯 Prática | ✅ Faça | ❌ Evite |
|---|---|---|
| **Consistência** | Sobrescreva com mesma assinatura | Mude parâmetros |
| **Documentação** | Documente comportamentos diferentes | Deixe implícito |
| **Duck Typing** | Use quando apropriado | Força herança desnecessária |
| **Interfaces** | Defina contrato claro | Comportamentos erráticos |
| **Testes** | Teste cada implementação | Teste só a base |
| **Clareza** | Código legível | Truques avançados |

---

## 🎭 Polimorfismo vs Herança

| Aspecto | 🎭 Polimorfismo | 🌳 Herança |
|---|---|---|
| **O que é** | Múltiplas formas | Compartilhamento |
| **Foco** | Comportamento | Estrutura |
| **Relação** | Horizontal (irmãs) | Vertical (pai-filho) |
| **Uso** | Flexibilidade | Reuso |
| **Exemplo** | Diferentes `fazer_som()` | Gato herda de Animal |

---

## 📊 Resumo Rápido

```python
# 1. Sobrescrita (Override)
class Animal:
    def fazer_som(self):
        return "Som"

class Cachorro(Animal):
    def fazer_som(self):  # Sobrescreve
        return "Au au!"

# 2. Sobrecarga (com *args)
def funcao(self, *args):
    # Funciona com qualquer quantidade de argumentos

# 3. Duck Typing
class A:
    def metodo(self):
        pass

class B:
    def metodo(self):  # Sem herança!
        pass

# 4. Genéricos
def processar(lista):
    for item in lista:
        print(item)  # Funciona com qualquer tipo
```

---

## 🚀 Conclusão

| 📌 | Descrição |
|:---:|---|
| 🎯 | Polimorfismo torna código **flexível e extensível** |
| 🔄 | Sobrescrita permite **customizar comportamentos** |
| 🦆 | Duck Typing oferece **máxima liberdade** |
| 🎭 | Comportamentos diferentes, **mesma interface** |

---

**Última atualização:** 📅 2026-06-16  
**Nível:** 🎓 Intermediário
