# 🔄 Programação Estruturada e Orientada a Objetos

## 📚 Índice
1. [Visão Geral](#visão-geral)
2. [Programação Estruturada](#programação-estruturada)
3. [Programação Orientada a Objetos](#programação-orientada-a-objetos)
4. [Comparação](#comparação)
5. [Exemplos Práticos](#exemplos-práticos)

---

## 🎯 Visão Geral

A programação em Python permite dois paradigmas principais:
- **Estruturada (Procedural)**: Foco em funções e procedimentos
- **Orientada a Objetos (POO)**: Foco em objetos e classes

---

## 📋 Programação Estruturada

### O que é?
Abordagem que organiza o programa em **funções e procedimentos**, processando dados de forma linear.

### Características Principais

| 🔑 Característica | 📝 Descrição |
|---|---|
| **Funções** | Blocos de código reutilizáveis |
| **Variáveis Globais** | Dados compartilhados entre funções |
| **Fluxo Linear** | Execução sequencial do código |
| **Modularidade** | Divisão em módulos independentes |
| **Simplicidade** | Fácil de entender e implementar |

### Vantagens ✅
- ✅ Simples e direta
- ✅ Boa para programas pequenos
- ✅ Fácil depuração
- ✅ Baixa curva de aprendizado

### Desvantagens ❌
- ❌ Difícil para projetos grandes
- ❌ Código pode ficar desorganizado
- ❌ Reuso limitado
- ❌ Dados vulneráveis

### 💻 Exemplo Prático

```python
# Programação Estruturada

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obeso"

# Uso
peso = 70
altura = 1.75
imc = calcular_imc(peso, altura)
resultado = classificar_imc(imc)
print(f"IMC: {imc:.2f} - {resultado}")
```

---

## 🏛️ Programação Orientada a Objetos (POO)

### O que é?
Paradigma que organiza o programa em **objetos**, que contêm dados (atributos) e comportamentos (métodos).

### Conceitos Fundamentais

| 🔑 Conceito | 📝 Descrição | 🎯 Objetivo |
|---|---|---|
| **Classe** | Template para criar objetos | Definir estrutura |
| **Objeto** | Instância de uma classe | Dados específicos |
| **Atributo** | Dados do objeto | Armazenar informações |
| **Método** | Função dentro de um objeto | Comportamento |
| **Encapsulamento** | Proteger dados internos | Segurança |
| **Herança** | Compartilhar entre classes | Reuso |
| **Polimorfismo** | Múltiplas formas | Flexibilidade |

### Os 3 Pilares da POO

#### 1️⃣ Encapsulamento
```python
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Privado
    
    def depositar(self, valor):
        self.__saldo += valor
```

#### 2️⃣ Herança
```python
class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"
```

#### 3️⃣ Polimorfismo
```python
animais = [Cachorro(), Gato(), Pássaro()]
for animal in animais:
    print(animal.fazer_som())  # Diferentes respostas
```

### Vantagens ✅
- ✅ Organização excepcional
- ✅ Escalável para projetos grandes
- ✅ Máximo reuso de código
- ✅ Fácil manutenção
- ✅ Protege dados sensíveis

### Desvantagens ❌
- ❌ Maior complexidade inicial
- ❌ Curva de aprendizado maior
- ❌ Pode ser excessiva para programas simples

---

## 📊 Comparação Detalhada

| Aspecto | 📋 Estruturada | 🏛️ Orientada |
|---|---|---|
| **Foco** | Funções | Objetos |
| **Organização** | Modular | Hierárquica |
| **Dados** | Separados | Encapsulados |
| **Segurança** | Baixa | Alta |
| **Reuso** | Limitado | Máximo |
| **Escalabilidade** | Pequena | Grande |
| **Aprendizado** | Fácil | Moderado |
| **Projetos** | Simples | Complexos |
| **Exemplo** | Scripts, Utilitários | Sistemas, Aplicações |

---

## 💻 Exemplos Práticos Completos

### Exemplo 1: Cálculo de Notas

#### ❌ Abordagem Estruturada
```python
# Funções separadas
def adicionar_nota(notas, valor):
    notas.append(valor)

def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_aprovacao(media):
    return media >= 7

# Uso
notas_joao = [7.5, 8.0, 9.0]
media_joao = calcular_media(notas_joao)
aprovado = verificar_aprovacao(media_joao)
```

#### ✅ Abordagem Orientada
```python
# Classe que encapsula tudo
class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
    
    def adicionar_nota(self, valor):
        self.notas.append(valor)
    
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
    def esta_aprovado(self):
        return self.calcular_media() >= 7

# Uso
aluno = Aluno("João")
aluno.adicionar_nota(7.5)
aluno.adicionar_nota(8.0)
aluno.adicionar_nota(9.0)
print(f"Média: {aluno.calcular_media()}")
print(f"Aprovado: {aluno.esta_aprovado()}")
```

---

### Exemplo 2: Gerenciar Funcionários

#### ❌ Abordagem Estruturada
```python
funcionarios = []

def add_funcionario(nome, cargo, salario):
    funcionarios.append({
        'nome': nome,
        'cargo': cargo,
        'salario': salario
    })

def calcular_folha():
    return sum(f['salario'] for f in funcionarios)

# Problema: Sem proteção dos dados!
funcionarios[0]['salario'] = 100  # ❌ Fácil modificar
```

#### ✅ Abordagem Orientada
```python
class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario  # Privado
    
    def obter_salario(self):
        return self.__salario
    
    def aumentar_salario(self, percentual):
        self.__salario *= (1 + percentual / 100)

class Empresa:
    def __init__(self):
        self.funcionarios = []
    
    def adicionar(self, funcionario):
        self.funcionarios.append(funcionario)
    
    def calcular_folha(self):
        return sum(f.obter_salario() for f in self.funcionarios)

# Uso
empresa = Empresa()
func = Funcionario("Maria", "Dev", 5000)
empresa.adicionar(func)
# func.__salario = 100  # ❌ Erro! Não consegue acessar
```

---

## 🎓 Quando Usar Cada Uma?

### Use Programação Estruturada Para:
- 📝 Scripts simples
- 🔧 Utilitários e ferramentas
- 📊 Processamento de dados básico
- 🎯 Protótipos rápidos

### Use Programação Orientada Para:
- 🏗️ Aplicações grandes
- 🔄 Código com muita reutilização
- 🛡️ Dados sensíveis (segurança)
- 👥 Trabalho em equipe
- 🚀 Projetos de longo prazo

---

## 🚀 Conclusão

| 📌 | Estruturada | Orientada |
|:---:|---|---|
| **Comece com** | ✅ (Aprenda primeiro) | (Depois) |
| **Para projetos pequenos** | ✅ (Preferida) | (Overkill) |
| **Para projetos médios/grandes** | ❌ (Inadequada) | ✅ (Essencial) |
| **Profissional** | ✅ (Base) | ✅ (Preferida) |

**Python permite os dois! Escolha conforme a necessidade.** 🎯

---

**Última atualização:** 📅 2026-06-16  
**Nível:** 🎓 Iniciante a Intermediário
