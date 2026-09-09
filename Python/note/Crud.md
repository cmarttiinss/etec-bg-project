# 🗄️ CRUD - Operações Básicas de Dados

## 📚 Índice
1. [O que é CRUD](#o-que-é-crud)
2. [As 4 Operações](#as-4-operações)
3. [Exemplos Práticos](#exemplos-práticos)
4. [CRUD em Diferentes Contextos](#crud-em-diferentes-contextos)
5. [Boas Práticas](#boas-práticas)

---

## 🎯 O que é CRUD?

**CRUD** é um acrônimo para as **4 operações fundamentais** no gerenciamento de dados:

| 🔤 | Operação | 📝 Descrição |
|:---:|---|---|
| **C** | **Create** | Criar/Inserir novos dados |
| **R** | **Read** | Ler/Recuperar dados existentes |
| **U** | **Update** | Atualizar/Modificar dados |
| **D** | **Delete** | Deletar/Remover dados |

---

## 🔧 As 4 Operações

### 1️⃣ CREATE (Criar)

**Objetivo:** Inserir novos dados no sistema.

#### Com Listas
```python
# Criar lista
tarefas = []

# Adicionar itens (Create)
tarefas.append("Estudar Python")
tarefas.append("Fazer exercícios")

print(tarefas)
# ['Estudar Python', 'Fazer exercícios']
```

#### Com Dicionários
```python
# Criar dicionário de usuário
usuario = {
    'id': 1,
    'nome': 'João',
    'email': 'joao@email.com',
    'idade': 25
}

print(usuario)
```

#### Com Banco de Dados (SQL)
```python
# INSERT - Inserir dados
cursor.execute('''
    INSERT INTO usuarios (nome, email, idade)
    VALUES (?, ?, ?)
''', ('João', 'joao@email.com', 25))

banco.commit()
```

---

### 2️⃣ READ (Ler)

**Objetivo:** Recuperar e acessar dados existentes.

#### Com Listas
```python
tarefas = ["Estudar", "Exercícios", "Praticar"]

# Ler por índice
print(tarefas[0])  # Estudar

# Ler todos
for tarefa in tarefas:
    print(tarefa)

# Ler com condicional
tarefas_importantes = [t for t in tarefas if len(t) > 5]
```

#### Com Dicionários
```python
usuario = {
    'nome': 'Maria',
    'email': 'maria@email.com',
    'idade': 30
}

# Ler valor específico
print(usuario['nome'])  # Maria
print(usuario.get('email'))  # maria@email.com

# Ler todas as chaves
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")
```

#### Com Banco de Dados (SQL)
```python
# SELECT - Buscar dados
cursor.execute('SELECT * FROM usuarios')
usuarios = cursor.fetchall()

# Buscar um
cursor.execute('SELECT * FROM usuarios WHERE id = ?', (1,))
usuario = cursor.fetchone()

for usuario in usuarios:
    print(usuario)
```

---

### 3️⃣ UPDATE (Atualizar)

**Objetivo:** Modificar dados existentes.

#### Com Listas
```python
tarefas = ["Estudar", "Exercícios", "Praticar"]

# Atualizar por índice
tarefas[0] = "Estudar Python"
print(tarefas)  # ['Estudar Python', 'Exercícios', 'Praticar']

# Atualizar com condição
for i, tarefa in enumerate(tarefas):
    if "Exerc" in tarefa:
        tarefas[i] = "Exercícios Avançados"
```

#### Com Dicionários
```python
usuario = {
    'nome': 'Pedro',
    'idade': 25,
    'cidade': 'São Paulo'
}

# Atualizar valor
usuario['idade'] = 26
usuario['cidade'] = 'Rio de Janeiro'

print(usuario)
# {'nome': 'Pedro', 'idade': 26, 'cidade': 'Rio de Janeiro'}
```

#### Com Banco de Dados (SQL)
```python
# UPDATE - Atualizar registro
cursor.execute('''
    UPDATE usuarios 
    SET idade = ?, cidade = ?
    WHERE id = ?
''', (26, 'Rio de Janeiro', 1))

banco.commit()
```

---

### 4️⃣ DELETE (Deletar)

**Objetivo:** Remover dados do sistema.

#### Com Listas
```python
tarefas = ["Estudar", "Exercícios", "Praticar"]

# Deletar por índice
del tarefas[0]
print(tarefas)  # ['Exercícios', 'Praticar']

# Deletar item específico
tarefas.remove("Exercícios")
print(tarefas)  # ['Praticar']

# Limpar lista
tarefas.clear()
print(tarefas)  # []
```

#### Com Dicionários
```python
usuario = {'nome': 'Ana', 'idade': 28, 'email': 'ana@email.com'}

# Deletar chave
del usuario['email']
print(usuario)  # {'nome': 'Ana', 'idade': 28}

# Usar pop()
idade = usuario.pop('idade', None)
print(usuario)  # {'nome': 'Ana'}
```

#### Com Banco de Dados (SQL)
```python
# DELETE - Remover registro
cursor.execute('DELETE FROM usuarios WHERE id = ?', (1,))

banco.commit()
```

---

## 💻 Exemplos Práticos Completos

### Exemplo 1: Sistema de Tarefas

```python
class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        self.id_counter = 1
    
    # CREATE
    def criar_tarefa(self, titulo, descricao):
        tarefa = {
            'id': self.id_counter,
            'titulo': titulo,
            'descricao': descricao,
            'concluida': False
        }
        self.tarefas.append(tarefa)
        self.id_counter += 1
        return tarefa
    
    # READ
    def listar_tarefas(self):
        return self.tarefas
    
    def obter_tarefa(self, id):
        for tarefa in self.tarefas:
            if tarefa['id'] == id:
                return tarefa
        return None
    
    # UPDATE
    def concluir_tarefa(self, id):
        tarefa = self.obter_tarefa(id)
        if tarefa:
            tarefa['concluida'] = True
            return True
        return False
    
    # DELETE
    def deletar_tarefa(self, id):
        self.tarefas = [t for t in self.tarefas if t['id'] != id]

# Uso
gerenciador = GerenciadorTarefas()

# CREATE
gerenciador.criar_tarefa("Estudar", "Aprender Python")
gerenciador.criar_tarefa("Exercício", "Fazer 10 exercícios")

# READ
print(gerenciador.listar_tarefas())

# UPDATE
gerenciador.concluir_tarefa(1)

# DELETE
gerenciador.deletar_tarefa(2)
```

---

### Exemplo 2: Gerenciador de Contatos

```python
class AgendaContatos:
    def __init__(self):
        self.contatos = {}
    
    # CREATE
    def adicionar_contato(self, nome, telefone, email):
        self.contatos[nome] = {
            'telefone': telefone,
            'email': email
        }
        print(f"✅ Contato {nome} adicionado!")
    
    # READ
    def buscar_contato(self, nome):
        return self.contatos.get(nome, "❌ Contato não encontrado")
    
    def listar_contatos(self):
        return self.contatos
    
    # UPDATE
    def atualizar_telefone(self, nome, novo_telefone):
        if nome in self.contatos:
            self.contatos[nome]['telefone'] = novo_telefone
            print(f"✅ Telefone atualizado!")
            return True
        return False
    
    # DELETE
    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"✅ Contato removido!")
            return True
        return False

# Uso
agenda = AgendaContatos()

# CREATE
agenda.adicionar_contato("Maria", "11987654321", "maria@email.com")
agenda.adicionar_contato("João", "11912345678", "joao@email.com")

# READ
print(agenda.buscar_contato("Maria"))

# UPDATE
agenda.atualizar_telefone("Maria", "11999999999")

# DELETE
agenda.remover_contato("João")

# READ ALL
print(agenda.listar_contatos())
```

---

## 🗄️ CRUD em Diferentes Contextos

### 1. Com Arquivos JSON

```python
import json

# CREATE
dados = {'usuarios': []}
dados['usuarios'].append({'id': 1, 'nome': 'João'})

with open('dados.json', 'w') as f:
    json.dump(dados, f)

# READ
with open('dados.json', 'r') as f:
    dados = json.load(f)

# UPDATE
dados['usuarios'][0]['nome'] = 'João Silva'

with open('dados.json', 'w') as f:
    json.dump(dados, f)

# DELETE
dados['usuarios'].pop(0)
```

### 2. Com Banco de Dados SQLite

```python
import sqlite3

# Conectar/Criar banco
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

# CREATE (tabela)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        email TEXT
    )
''')

# CREATE (dados)
cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)',
               ('Maria', 'maria@email.com'))

# READ
cursor.execute('SELECT * FROM usuarios')
print(cursor.fetchall())

# UPDATE
cursor.execute('UPDATE usuarios SET nome = ? WHERE id = ?',
               ('Maria Silva', 1))

# DELETE
cursor.execute('DELETE FROM usuarios WHERE id = ?', (1,))

conn.commit()
conn.close()
```

### 3. Com APIs REST

```python
import requests

# CREATE - POST
response = requests.post('https://api.exemplo.com/usuarios',
    json={'nome': 'João', 'email': 'joao@email.com'})

# READ - GET
response = requests.get('https://api.exemplo.com/usuarios')
usuarios = response.json()

# UPDATE - PUT
response = requests.put('https://api.exemplo.com/usuarios/1',
    json={'nome': 'João Silva'})

# DELETE - DELETE
response = requests.delete('https://api.exemplo.com/usuarios/1')
```

---

## ✅ Boas Práticas

| 🎯 Prática | ✅ Faça | ❌ Evite |
|---|---|---|
| **Validação** | Valide dados antes de criar | Aceitar dados sem verificar |
| **Segurança** | Use prepared statements | Concatenar strings SQL |
| **Tratamento de Erros** | Try/except para operações | Ignorar exceções |
| **Logging** | Registre operações | Não rastrear atividades |
| **Transações** | Use commit/rollback | Não controlar transações |
| **Backup** | Mantenha backups | Perder dados |

---

## 🚀 Resumo Rápido

```python
# CREATE - Criar
lista.append(item)
dicio['chave'] = valor
cursor.execute('INSERT INTO...')

# READ - Ler
lista[0]
dicio['chave']
cursor.execute('SELECT * FROM...')

# UPDATE - Atualizar
lista[0] = novo_valor
dicio['chave'] = novo_valor
cursor.execute('UPDATE...')

# DELETE - Deletar
del lista[0]
del dicio['chave']
cursor.execute('DELETE FROM...')
```

---

**Última atualização:** 📅 2026-06-16  
**Nível:** 🎓 Iniciante
