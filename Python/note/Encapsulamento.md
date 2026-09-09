# 🔐 Encapsulamento

## 📚 Índice
1. [O que é Encapsulamento](#o-que-é-encapsulamento)
2. [Níveis de Acesso](#níveis-de-acesso)
3. [Por que Encapsular](#por-que-encapsular)
4. [Exemplos Práticos](#exemplos-práticos)
5. [Getters e Setters](#getters-e-setters)
6. [Boas Práticas](#boas-práticas)

---

## 🎯 O que é Encapsulamento?

**Encapsulamento** é um dos pilares da Programação Orientada a Objetos (POO) que envolve:

> 🔒 **Agrupar dados (atributos) com métodos que os manipulam, controlando o acesso externo.**

É como colocar seus dados em uma cápsula protegida, controlando quem pode ver e modificar.

---

## 🔐 Níveis de Acesso

Python oferece três níveis de privacidade para atributos e métodos:

| 🔑 Nível | 📌 Símbolo | 🌍 Visibilidade | ✅ Uso |
|---|:---:|---|---|
| **Público** | Sem prefixo | Acessível de qualquer lugar | `self.nome` |
| **Protegido** | `_` (underscore) | Apenas na classe e subclasses | `self._dados` |
| **Privado** | `__` (double underscore) | Apenas dentro da classe | `self.__senha` |

---

### 1️⃣ Atributo Público

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome  # ✅ Público

pessoa = Pessoa("João")
print(pessoa.nome)  # ✅ Funciona
pessoa.nome = "Maria"  # ✅ Pode modificar
```

**Quando usar:** Dados que não precisam de proteção.

---

### 2️⃣ Atributo Protegido

```python
class Veiculo:
    def __init__(self, velocidade):
        self._velocidade = velocidade  # 🔒 Protegido

veiculo = Veiculo(100)
print(veiculo._velocidade)  # ⚠️ Funciona, mas não é recomendado
```

**Quando usar:** Dados que subclasses podem acessar.

**Convenção:** Use quando pretende herança.

---

### 3️⃣ Atributo Privado

```python
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # 🔐 Privado

conta = ContaBancaria(1000)
print(conta.__saldo)  # ❌ AttributeError!
```

**Quando usar:** Dados sensíveis que não devem ser acessados diretamente.

**Benefício:** Proteção máxima.

---

## 💡 Por que Encapsular?

| 🎯 Razão | 📝 Explicação | 💻 Exemplo |
|---|---|---|
| **Proteção** | Evita modificações indevidas | Saldo bancário não pode ser alterado diretamente |
| **Validação** | Controla dados de entrada | Apenas números positivos em saldo |
| **Consistência** | Mantém integridade dos dados | Atualizar saldo = registrar transação |
| **Flexibilidade** | Permite mudanças internas | Mudar implementação sem quebrar código |
| **Segurança** | Protege dados sensíveis | Senha não exposta |

---

## 💻 Exemplos Práticos

### Exemplo 1: Conta Bancária (Básico)

#### ❌ Sem Encapsulamento
```python
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo  # ❌ Sem proteção!

conta = ContaBancaria("João", 1000)
conta.saldo = -5000  # ❌ Valor inválido aceito!
print(conta.saldo)  # -5000 (Problema!)
```

#### ✅ Com Encapsulamento
```python
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # 🔐 Privado
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"✅ Depósito de R${valor} realizado!")
        else:
            print("❌ Valor deve ser positivo!")
    
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"✅ Saque de R${valor} realizado!")
        else:
            print("❌ Saldo insuficiente!")
    
    def obter_saldo(self):
        return self.__saldo

# Uso
conta = ContaBancaria("João", 1000)
conta.depositar(500)      # ✅ 1500
conta.sacar(200)          # ✅ 1300
print(conta.obter_saldo())  # 1300
# conta.__saldo = -5000   # ❌ Erro!
```

---

### Exemplo 2: Estudante (Com Validação)

```python
class Estudante:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula
        self.__notas = []
    
    # Getters (Leitura)
    def obter_nome(self):
        return self.__nome
    
    def obter_matricula(self):
        return self.__matricula
    
    def obter_media(self):
        if not self.__notas:
            return 0
        return sum(self.__notas) / len(self.__notas)
    
    # Setters (Escrita com validação)
    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.__notas.append(nota)
            print(f"✅ Nota {nota} adicionada!")
        else:
            print("❌ Nota deve estar entre 0 e 10!")
    
    def esta_aprovado(self):
        return self.obter_media() >= 7
    
    def exibir_resumo(self):
        status = "✅ Aprovado" if self.esta_aprovado() else "❌ Reprovado"
        print(f"Aluno: {self.__nome}")
        print(f"Matrícula: {self.__matricula}")
        print(f"Média: {self.obter_media():.2f}")
        print(f"Status: {status}")

# Uso
aluno = Estudante("Maria", "2024001")
aluno.adicionar_nota(8.5)
aluno.adicionar_nota(9.0)
aluno.adicionar_nota(7.5)
aluno.exibir_resumo()
```

**Saída:**
```
✅ Nota 8.5 adicionada!
✅ Nota 9.0 adicionada!
✅ Nota 7.5 adicionada!
Aluno: Maria
Matrícula: 2024001
Média: 8.33
Status: ✅ Aprovado
```

---

### Exemplo 3: Produto (Ecommerce)

```python
class Produto:
    def __init__(self, nome, preco, estoque):
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque
    
    # Getters
    def obter_nome(self):
        return self.__nome
    
    def obter_preco(self):
        return self.__preco
    
    def obter_estoque(self):
        return self.__estoque
    
    # Setters com validação
    def definir_preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
            return True
        return False
    
    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.__estoque += quantidade
            return True
        return False
    
    def remover_estoque(self, quantidade):
        if 0 < quantidade <= self.__estoque:
            self.__estoque -= quantidade
            return True
        return False
    
    def exibir_informacoes(self):
        print(f"Produto: {self.__nome}")
        print(f"Preço: R${self.__preco:.2f}")
        print(f"Estoque: {self.__estoque} unidades")

# Uso
produto = Produto("Notebook", 3500.00, 10)
produto.exibir_informacoes()
produto.remover_estoque(3)
produto.definir_preco(3200.00)
produto.exibir_informacoes()
```

---

## 📌 Getters e Setters

### O que são?

- **Getter**: Método que **lê** o valor de um atributo privado
- **Setter**: Método que **modifica** o valor de um atributo privado (com validação)

### Exemplo Completo

```python
class Temperatura:
    def __init__(self, celsius):
        self.__celsius = celsius
    
    # ✅ GETTER - Ler valor
    def obter_celsius(self):
        """Retorna a temperatura em Celsius"""
        return self.__celsius
    
    def obter_fahrenheit(self):
        """Retorna a temperatura em Fahrenheit"""
        return (self.__celsius * 9/5) + 32
    
    # ✅ SETTER - Modificar com validação
    def definir_celsius(self, valor):
        """Define a temperatura (mínimo -273.15°C)"""
        if valor >= -273.15:
            self.__celsius = valor
            return True
        else:
            print("❌ Temperatura abaixo do zero absoluto!")
            return False

# Uso
temp = Temperatura(25)
print(f"Celsius: {temp.obter_celsius()}°C")
print(f"Fahrenheit: {temp.obter_fahrenheit()}°F")

temp.definir_celsius(30)
print(f"Nova temperatura: {temp.obter_celsius()}°C")

temp.definir_celsius(-300)  # ❌ Erro!
```

### Usando @property (Python Avançado)

```python
class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco
    
    @property
    def preco(self):
        """Getter - Acesso como atributo"""
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        """Setter - Modificação como atributo"""
        if valor > 0:
            self.__preco = valor
        else:
            raise ValueError("Preço deve ser positivo!")

# Uso (mais limpo)
produto = Produto("Livro", 50.00)
print(produto.preco)  # 50.0
produto.preco = 45.00  # Usa setter automaticamente
```

---

## ✅ Boas Práticas

| 🎯 Prática | ✅ Faça | ❌ Evite |
|---|---|---|
| **Privado por padrão** | Comece com `__` | Expor tudo publicamente |
| **Validação** | Verificar dados em setters | Aceitar qualquer valor |
| **Documentação** | Documente getters/setters | Código sem explicação |
| **Nomes claros** | `obter_saldo()`, `definir_preco()` | `get_a()`, `set_x()` |
| **Lógica de negócio** | Coloque na classe | Deixe externa |
| **Herança** | Use `_` para subclasses | `__` para herança |

---

## 🚀 Comparação: Sem vs Com Encapsulamento

```python
# ❌ SEM ENCAPSULAMENTO
class ContaSem:
    def __init__(self, saldo):
        self.saldo = saldo

conta1 = ContaSem(1000)
conta1.saldo = -999999  # ❌ Erro de lógica aceito!


# ✅ COM ENCAPSULAMENTO
class ContaCom:
    def __init__(self, saldo):
        self.__saldo = saldo
    
    def obter_saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

conta2 = ContaCom(1000)
conta2.depositar(-999999)  # ❌ Método valida!
```

---

## 📊 Resumo Rápido

| Elemento | 🔓 Público | 🔒 Protegido | 🔐 Privado |
|---|---|---|---|
| **Sintaxe** | `self.nome` | `self._nome` | `self.__nome` |
| **Acesso Externo** | ✅ Sim | ⚠️ Não (convenção) | ❌ Não |
| **Uso** | Geral | Subclasses | Segurança |
| **Validação** | Não | Opcional | Sim |

---

**Última atualização:** 📅 2026-06-16  
**Nível:** 🎓 Intermediário
