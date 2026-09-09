# 📊 Tabelas em HTML - Guia Completo

---

## 📌 Introdução às Tabelas

### O que são Tabelas?

Tabelas em HTML são estruturas usadas para organizar e apresentar dados de forma ordenada em linhas e colunas. Elas são ideais para exibir informações tabulares como relatórios, dados financeiros, cronogramas e listas de produtos.

### 📝 Resumo Introdutório
> Tabelas HTML organizam dados em formato de grade (linhas × colunas), permitindo uma visualização clara e estruturada. Embora poderosas, exigem cuidado especial com responsividade em dispositivos móveis.

| Aspecto | Descrição |
|---------|-----------|
| **Uso Principal** | Exibição de dados estruturados |
| **Tags Base** | `<table>`, `<tr>`, `<td>`, `<th>` |
| **Responsividade** | Limitada - requer técnicas CSS |
| **Acessibilidade** | Excelente com estrutura semântica |

---

## 🔧 Estrutura Básica das Tabelas

### Componentes Fundamentais

#### 1️⃣ Tag `<table>`
Delimita toda a tabela. Nenhuma tabela funciona sem ela.

```html
<table>
    <!-- Conteúdo aqui -->
</table>
```

#### 2️⃣ Tag `<tr>` (Table Row - Linha)
Define uma linha na tabela. Cada `<tr>` representa uma linha horizontal.

#### 3️⃣ Tag `<td>` (Table Data - Célula de Dados)
Define uma célula de dados dentro da linha. Contém o conteúdo principal.

#### 4️⃣ Tag `<th>` (Table Header - Cabeçalho)
Define uma célula de cabeçalho. Funciona como `<td>`, mas o conteúdo fica **em negrito** e é semanticamente identificado como cabeçalho.

### 📝 Resumo da Estrutura
> A estrutura básica segue a hierarquia: **Tabela > Linhas > Células**. Use `<th>` para cabeçalhos e `<td>` para dados convencionais.

---

## 💡 Exemplo Prático Básico

```html
<table>
    <tr>
        <th>Produto</th>
        <th>Preço</th>
        <th>Quantidade</th>
    </tr>
    
    <tr>
        <td>Notebook</td>
        <td>R$ 2.500</td>
        <td>5</td>
    </tr>
    
    <tr>
        <td>Mouse</td>
        <td>R$ 50</td>
        <td>20</td>
    </tr>
    
    <tr>
        <td>Teclado</td>
        <td>R$ 150</td>
        <td>12</td>
    </tr>
</table>
```

### Resultado Visual

| Produto | Preço | Quantidade |
|---------|-------|-----------|
| Notebook | R$ 2.500 | 5 |
| Mouse | R$ 50 | 20 |
| Teclado | R$ 150 | 12 |

---

## 🎨 Estilizando Tabelas com CSS

### ⚠️ Importante!
Por padrão, tabelas HTML **não possuem bordas visíveis**. É necessário adicionar CSS para estilização.

### Exemplo de CSS Básico

```css
table {
    border-collapse: collapse;
    width: 100%;
    margin: 20px 0;
    font-family: Arial, sans-serif;
}

th, td {
    border: 1px solid #333;
    padding: 12px;
    text-align: left;
}

th {
    background-color: #4CAF50;
    color: white;
    font-weight: bold;
}

tr:nth-child(even) {
    background-color: #f9f9f9;
}

tr:hover {
    background-color: #e8f5e9;
}
```

### 📝 Resumo de Estilos
> `border-collapse` remove bordas duplas, `padding` adiciona espaçamento, cores de fundo melhoram legibilidade e `hover` torna a tabela interativa.

| Propriedade | Função |
|-------------|--------|
| `border-collapse` | Remove espaço entre bordas |
| `padding` | Espaçamento interno da célula |
| `background-color` | Cor de fundo |
| `nth-child(even)` | Alterna cores em linhas pares |
| `hover` | Efeito ao passar o mouse |

---

## 🏗️ Estrutura Semântica Avançada

Para tabelas mais complexas e acessíveis, use elementos semânticos:

```html
<table>
    <thead>
        <tr>
            <th>Mês</th>
            <th>Receita</th>
            <th>Despesa</th>
            <th>Lucro</th>
        </tr>
    </thead>
    
    <tbody>
        <tr>
            <td>Janeiro</td>
            <td>R$ 5.000</td>
            <td>R$ 2.000</td>
            <td>R$ 3.000</td>
        </tr>
        <tr>
            <td>Fevereiro</td>
            <td>R$ 6.000</td>
            <td>R$ 2.500</td>
            <td>R$ 3.500</td>
        </tr>
    </tbody>
    
    <tfoot>
        <tr>
            <th>Total</th>
            <td>R$ 11.000</td>
            <td>R$ 4.500</td>
            <td>R$ 6.500</td>
        </tr>
    </tfoot>
</table>
```

### Componentes Avançados

| Tag | Descrição |
|-----|-----------|
| `<thead>` | ✅ Agrupa cabeçalhos (aparece no topo) |
| `<tbody>` | 📝 Agrupa dados principais |
| `<tfoot>` | 🔢 Agrupa totalizações ou rodapé |
| `<caption>` | 📌 Título/legenda da tabela |

### 📝 Resumo da Estrutura Semântica
> Use `<thead>`, `<tbody>` e `<tfoot>` para melhor organização e acessibilidade. Melhora a interpretação por leitores de tela e facilita a manutenção.

---

## 🎯 Atributos Importantes

### Colspan e Rowspan

#### ➡️ **colspan** - Mescla colunas
```html
<tr>
    <td colspan="2">Ocupa 2 colunas</td>
    <td>Coluna 3</td>
</tr>
```

#### ⬇️ **rowspan** - Mescla linhas
```html
<tr>
    <td rowspan="2">Ocupa 2 linhas</td>
    <td>Coluna 2</td>
</tr>
<tr>
    <td>Coluna 2 (nova linha)</td>
</tr>
```

### Exemplo Prático - Horário Escolar

```html
<table border="1">
    <tr>
        <th>Horário</th>
        <th>Segunda</th>
        <th>Terça</th>
        <th>Quarta</th>
    </tr>
    <tr>
        <td>08:00 - 09:00</td>
        <td colspan="3" style="text-align: center;">Português</td>
    </tr>
    <tr>
        <td>09:00 - 10:00</td>
        <td>Matemática</td>
        <td rowspan="2">Educação Física</td>
        <td>História</td>
    </tr>
    <tr>
        <td>10:00 - 11:00</td>
        <td>Ciências</td>
        <td>Geografia</td>
    </tr>
</table>
```

### 📝 Resumo de Atributos
> `colspan` estende a célula horizontalmente, `rowspan` estende verticalmente. Úteis para tabelas complexas e layouts especiais.

---

## 📱 Responsividade em Tabelas

### ⚠️ O Desafio
Tabelas tradicionais não redimensionam bem em telas pequenas. Soluções:

### ✅ Solução 1: Overflow Horizontal
```css
.table-container {
    overflow-x: auto;
    margin: 20px 0;
}

table {
    min-width: 100%;
    border-collapse: collapse;
}
```

### ✅ Solução 2: Stack em Mobile (CSS)
```css
@media (max-width: 768px) {
    table, thead, tbody, th, td, tr {
        display: block;
    }
    
    th {
        position: absolute;
        top: -9999px;
        left: -9999px;
    }
    
    td {
        position: relative;
        padding-left: 50%;
    }
    
    td:before {
        content: attr(data-label);
        position: absolute;
        left: 6px;
        font-weight: bold;
    }
}
```

### HTML com atributo data-label
```html
<td data-label="Produto">Notebook</td>
<td data-label="Preço">R$ 2.500</td>
```

### 📝 Resumo de Responsividade
> Para dispositivos móveis, use scroll horizontal ou converta para exibição em bloco com labels dos dados. Considere alternativas como cards para melhor UX.

---

## 🚫 Limitações e Boas Práticas

| ❌ Não Faça | ✅ Faça |
|------------|--------|
| Use tabelas para layout de página | Use tabelas apenas para dados tabulares |
| Tabelas aninhadas (tabelas dentro de tabelas) | Estruture dados com thead, tbody, tfoot |
| Ignore responsividade | Implemente soluções mobile-friendly |
| Deixe sem bordas e espaçamento | Estilize com CSS adequadamente |
| Tabelas muito largas sem scroll | Use scroll horizontal ou paginar dados |
| Ignore acessibilidade | Use `<th>`, `<caption>` e atributos `scope` |

### Acessibilidade Melhorada

```html
<table>
    <caption>Vendas do Primeiro Trimestre</caption>
    <thead>
        <tr>
            <th scope="col">Produto</th>
            <th scope="col">Jan</th>
            <th scope="col">Fev</th>
            <th scope="col">Mar</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th scope="row">Produto A</th>
            <td>100</td>
            <td>150</td>
            <td>200</td>
        </tr>
    </tbody>
</table>
```

### 📝 Resumo de Boas Práticas
> Tabelas devem ser semânticas, responsivas e acessíveis. Use-as apenas para dados tabulares, nunca para layout. Sempre adicione cabeçalhos e legendas claros.

---

## 🎓 Comparação: Quando Usar Tabelas

| Situação | Usar Tabela? | Alternativa |
|----------|-------------|------------|
| Comparação de dados | ✅ Sim | - |
| Relatórios financeiros | ✅ Sim | - |
| Cronograma/Horário | ✅ Sim | - |
| Layout de página | ❌ Não | Flexbox / Grid |
| Menu de navegação | ❌ Não | Nav semântica |
| Galeria de imagens | ❌ Não | CSS Grid / Flexbox |
| Formulário | ❌ Não | Elementos semânticos |

---

## 📚 Exemplo Completo Profissional

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tabelas Profissionais</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding: 20px;
            background-color: #f5f5f5;
        }
        
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        h1 {
            color: #333;
            margin-bottom: 10px;
            border-bottom: 3px solid #4CAF50;
            padding-bottom: 10px;
        }
        
        .table-wrapper {
            overflow-x: auto;
            margin: 30px 0;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            background: white;
        }
        
        thead {
            background-color: #4CAF50;
            color: white;
        }
        
        th {
            padding: 15px;
            text-align: left;
            font-weight: 600;
            border: 1px solid #ddd;
        }
        
        td {
            padding: 12px 15px;
            border: 1px solid #ddd;
        }
        
        tbody tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        
        tbody tr:hover {
            background-color: #e8f5e9;
            transition: 0.3s ease;
        }
        
        tfoot {
            background-color: #f0f0f0;
            font-weight: 600;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Relatório de Vendas</h1>
        
        <div class="table-wrapper">
            <table>
                <caption>Vendas por Categoria - Q1 2024</caption>
                <thead>
                    <tr>
                        <th scope="col">Categoria</th>
                        <th scope="col">Janeiro</th>
                        <th scope="col">Fevereiro</th>
                        <th scope="col">Março</th>
                        <th scope="col">Total</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th scope="row">Eletrônicos</th>
                        <td>R$ 15.000</td>
                        <td>R$ 18.000</td>
                        <td>R$ 22.000</td>
                        <td>R$ 55.000</td>
                    </tr>
                    <tr>
                        <th scope="row">Roupas</th>
                        <td>R$ 8.000</td>
                        <td>R$ 9.500</td>
                        <td>R$ 11.000</td>
                        <td>R$ 28.500</td>
                    </tr>
                    <tr>
                        <th scope="row">Livros</th>
                        <td>R$ 5.000</td>
                        <td>R$ 6.200</td>
                        <td>R$ 7.800</td>
                        <td>R$ 19.000</td>
                    </tr>
                </tbody>
                <tfoot>
                    <tr>
                        <th scope="row">TOTAL GERAL</th>
                        <td>R$ 28.000</td>
                        <td>R$ 33.700</td>
                        <td>R$ 40.800</td>
                        <td><strong>R$ 102.500</strong></td>
                    </tr>
                </tfoot>
            </table>
        </div>
    </div>
</body>
</html>
```

---

## 🎯 Checklist Final

✅ **Ao criar uma tabela, sempre verifique:**

- [ ] Tabela é a melhor forma de apresentar esses dados?
- [ ] Todos os cabeçalhos estão em `<th>`?
- [ ] Estrutura semântica com `<thead>`, `<tbody>`, `<tfoot>`?
- [ ] CSS aplicado para bordas e espaçamento?
- [ ] Tabela é responsiva em dispositivos móveis?
- [ ] Atributos `scope` para acessibilidade?
- [ ] `<caption>` ou título descritivo?
- [ ] Contrastes de cor adequados (WCAG)?
- [ ] Testado em leitores de tela?

---

## 📖 Referências Úteis

- 🔗 [MDN Web Docs - HTML Table Element](https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element/table)
- 🔗 [W3C - HTML Tables](https://www.w3.org/WAI/tutorials/tables/)
- 🔗 [CSS-Tricks - Responsive Tables](https://css-tricks.com/responsive-data-tables/)

---

**Última atualização:** 2024
**Profissional:** Guia Completo de Tabelas em HTML
