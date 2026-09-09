# 📚 JavaScript - Aula 1: Fundamentos e Conceitos Iniciais

![JavaScript Logo](https://www.vectorlogo.zone/logos/javascript/javascript-icon.svg)

---

## 🎯 Objetivo da Aula

Compreender os fundamentos do JavaScript, uma linguagem de programação versátil utilizada principalmente para desenvolvimento web, entendendo sua natureza, estruturas básicas e formas de implementação.

---

## 📖 1. O que é JavaScript?

### 🔍 Definição Técnica

JavaScript é uma **linguagem de programação interpretada** (não compilada), o que significa que o código é executado diretamente pelo navegador ou ambiente JavaScript sem necessidade de criar um arquivo executável (.exe) para funcionar.

| Característica | Descrição |
|---|---|
| **Tipo** | Linguagem Interpretada |
| **Arquivo Executável** | ❌ Não gera .exe |
| **Execução** | Em tempo real (runtime) |
| **Uso Principal** | Desenvolvimento Web (Frontend) |
| **Ambiente** | Navegadores, Node.js, servidores |

### 📝 Resumo do Tópico

> JavaScript é uma linguagem interpretada que funciona diretamente no navegador, sem necessidade de compilação. É a linguagem padrão para adicionar interatividade a páginas web e é executada pelo mecanismo JavaScript do navegador.

---

## 📦 2. Estruturas e Componentes Fundamentais

### 2.1 Variáveis 🔤

As variáveis são containers para armazenar dados que podem ser utilizados e modificados durante a execução do programa.

```javascript
let nome = "João";
var idade = 25;
const email = "joao@email.com";
```

| Tipo | Escopo | Reatribuição | Reescrita |
|---|---|---|---|
| `let` | Bloco (Block Scope) | ✅ Sim | ❌ Não |
| `var` | Função (Function Scope) | ✅ Sim | ✅ Sim |
| `const` | Bloco (Block Scope) | ❌ Não | ❌ Não |

### 2.2 Vetores (Arrays) 📊

Estruturas que armazenam múltiplos valores em uma única variável.

```javascript
let frutas = ["maçã", "banana", "laranja"];
let numeros = [1, 2, 3, 4, 5];
let misto = [1, "texto", true, null];
```

### 2.3 Estruturas de Dados (Objetos) 🏗️

```javascript
let pessoa = {
  nome: "Maria",
  idade: 30,
  profissao: "Desenvolvedora"
};
```

### 📝 Resumo do Tópico

> As variáveis, vetores e objetos são os componentes fundamentais para armazenar e organizar dados em JavaScript. Cada um deles tem um propósito específico: variáveis para dados simples, vetores para coleções ordenadas e objetos para dados estruturados.

---

## ⚙️ 3. Estruturas Condicionais

### 3.1 If (Se) 🔀

Executa um bloco de código apenas se uma condição for verdadeira.

```javascript
if (idade >= 18) {
  console.log("Maior de idade");
} else {
  console.log("Menor de idade");
}
```

### 3.2 Switch (Seletor) 🎚️

Seleciona um entre múltiplos blocos de código para executar.

```javascript
switch (dia) {
  case 1:
    console.log("Segunda");
    break;
  case 2:
    console.log("Terça");
    break;
  default:
    console.log("Dia inválido");
}
```

| Estrutura | Melhor Para | Exemplo |
|---|---|---|
| **if/else** | 2-3 condições | Verificar idade, permissões |
| **switch** | Múltiplas opções fixas | Seleção de menu, dia da semana |

### 📝 Resumo do Tópico

> As estruturas condicionais permitem controlar o fluxo do programa, executando diferentes blocos de código baseado em condições. `if/else` é ideal para comparações simples, enquanto `switch` é mais eficiente para múltiplas opções.

---

## 🔁 4. Estruturas de Repetição

### 4.1 For (Para) 📌

Repete um bloco de código um número específico de vezes.

```javascript
for (let i = 0; i < 5; i++) {
  console.log("Iteração: " + i);
}
```

**Sintaxe:**
```
for (inicialização; condição; incremento)
```

### 4.2 While (Enquanto) ⏰

Repete um bloco enquanto uma condição for verdadeira.

```javascript
let contador = 0;
while (contador < 5) {
  console.log("Contador: " + contador);
  contador++;
}
```

| Loop | Uso | Quando Usar |
|---|---|---|
| **for** | Iterações conhecidas | Percorrer arrays, números fixos |
| **while** | Condição dinâmica | Dados desconhecidos, validação |
| **do...while** | Pelo menos uma execução | Menus, validação de entrada |

### 📝 Resumo do Tópico

> As estruturas de repetição automatizam tarefas repetitivas. `for` é ideal quando sabemos quantas vezes repetir, e `while` é flexível para condições dinâmicas que podem variar durante a execução.

---

## 🔧 5. Funções

### Definição e Propósito 📌

Funções são blocos de código reutilizáveis que executam uma tarefa específica.

```javascript
function saudacao(nome) {
  return "Olá, " + nome + "!";
}

console.log(saudacao("João")); // Olá, João!
```

### Sintaxe Básica

```javascript
function nome(parâmetro1, parâmetro2) {
  // Corpo da função
  return resultado;
}
```

### Funções Modernas (Arrow Functions)

```javascript
const soma = (a, b) => {
  return a + b;
};

const multiplicar = (a, b) => a * b;
```

### 📝 Resumo do Tópico

> Funções encapsulam lógica reutilizável, tornando o código mais organizado e fácil de manter. Podem receber parâmetros e retornar valores, sendo fundamentais para programação modular.

---

## 🌐 6. DOM (Document Object Model) 🏛️

### O que é DOM? 🔍

O DOM é uma hierarquia de objetos que representa a estrutura de um documento HTML. JavaScript pode acessar e modificar qualquer elemento da página através do DOM.

```javascript
// Acessar elementos
document.getElementById("meuId");
document.querySelector(".minhClasse");
document.querySelectorAll("p");

// Modificar conteúdo
element.textContent = "Novo texto";
element.innerHTML = "<strong>HTML</strong>";
```

### Hierarquia do DOM 🔗

```
Document
  ├── html
  │   ├── head
  │   └── body
  │       ├── div
  │       ├── p
  │       └── button
```

### 📝 Resumo do Tópico

> O DOM é a interface entre JavaScript e HTML. Permite que o JavaScript acesse, modifique e manipule elementos da página de forma dinâmica, criando interatividade.

---

## ⚠️ 7. Case Sensitivity (Sensibilidade a Maiúsculas e Minúsculas)

JavaScript **diferencia maiúsculas de minúsculas** em:
- ✅ Nomes de variáveis
- ✅ Nomes de funções
- ✅ Nomes de métodos e propriedades

```javascript
let nome = "João";
let Nome = "Maria";      // Variável diferente!
let NOME = "Pedro";      // Outra variável diferente!

console.log(nome);  // "João"
console.log(Nome);  // "Maria"
console.log(NOME);  // "Pedro"
```

| Exemplo | Diferente? |
|---|---|
| `myVar` vs `myvar` | ✅ SIM |
| `getElementById` vs `getElementByid` | ✅ SIM |
| `function test()` vs `function TEST()` | ✅ SIM |

### 📝 Resumo do Tópico

> A sensibilidade a maiúsculas é uma característica fundamental do JavaScript. Um pequeno erro de digitação em maiúsculas/minúsculas pode causar erros. Mantenha consistência ao nomear variáveis e funções.

---

## 💾 8. Onde Colocar o Código JavaScript

### 8.1 Inline (Dentro do HTML) 📝

#### Na seção `<head>`

```html
<!DOCTYPE html>
<html>
<head>
  <script>
    console.log("Script na HEAD");
  </script>
</head>
<body>
  <h1>Página</h1>
</body>
</html>
```

#### Na seção `<body>`

```html
<body>
  <h1>Página</h1>
  
  <script>
    console.log("Script no BODY");
  </script>
</body>
</html>
```

| Local | Vantagens | Desvantagens |
|---|---|---|
| **HEAD** | Carrega primeiro | Bloqueia renderização |
| **BODY (final)** | Não bloqueia renderização | Pode causar erros de elemento não encontrado |

### 8.2 Arquivo Externo 🔗

#### Criar arquivo `.js`

**arquivo.js:**
```javascript
function saudacao() {
  alert("Olá!");
}
```

#### Importar no HTML

```html
<!DOCTYPE html>
<html>
<head>
  <title>Minha Página</title>
</head>
<body>
  <h1>Bem-vindo</h1>
  
  <!-- Importar arquivo JavaScript -->
  <script src="arquivo.js"></script>
</body>
</html>
```

### ✅ Boas Práticas

```html
<!-- ✅ RECOMENDADO: No final do BODY -->
<body>
  <h1>Conteúdo da página</h1>
  
  <script src="script.js"></script>
</body>
```

### 📝 Resumo do Tópico

> JavaScript pode ser inserido diretamente no HTML (inline) ou em arquivos separados (.js). A melhor prática é colocar `<script>` no final do `<body>` para não bloquear o carregamento da página, mantendo scripts externos em arquivos `.js` para melhor organização.

---

## 📋 Comparação de Métodos

| Aspecto | Inline HEAD | Inline BODY | Arquivo Externo |
|---|---|---|---|
| **Organização** | ❌ Ruim | ⚠️ Médio | ✅ Excelente |
| **Reutilização** | ❌ Não | ❌ Não | ✅ Sim |
| **Performance** | ⚠️ Bloqueia | ✅ Não bloqueia | ✅ Não bloqueia |
| **Manutenção** | ❌ Difícil | ⚠️ Médio | ✅ Fácil |
| **Cache** | ❌ Não | ❌ Não | ✅ Sim |

---

## 🎓 Conclusão

JavaScript é a linguagem fundamental para desenvolvimento web interativo. Compreender seus conceitos básicos — variáveis, estruturas de controle, repetição, funções e DOM — é essencial para criar páginas web dinâmicas e responsivas.

### 📌 Pontos-Chave Principais

- ✅ JavaScript é interpretado, não compilado
- ✅ Use estruturas de dados apropriadas (variáveis, vetores, objetos)
- ✅ Controle o fluxo com condicionais e loops
- ✅ Encapsule lógica em funções
- ✅ Manipule o HTML através do DOM
- ✅ Cuidado com case sensitivity
- ✅ Organize scripts em arquivos externos

---

## 📚 Referências e Recursos

| Recurso | Link |
|---|---|
| MDN Web Docs | https://developer.mozilla.org/pt-BR/docs/Web/JavaScript |
| W3Schools | https://www.w3schools.com/js/ |
| ECMAScript Standard | https://www.ecma-international.org/ |

---

**Criado em:** 2026  
**Disciplina:** JavaScript - ETEC Basilides  
**Status:** ✅ Completo e Atualizado
