class Produto:
    """Representa um produto com nome e preço."""
 
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco
 
    def exibir(self, indice: int = None) -> None:
        """Exibe os dados do produto formatados."""
        prefixo = f"[{indice}] " if indice is not None else "    "
        print(f"{prefixo}{self.nome:<25}  R$ {self.preco:>8.2f}")
 
 
# Estrutura de dados 
produtos: list[Produto] = []
 
 
# Funções auxiliares 
def separador(char: str = "─", largura: int = 45) -> None:
    print(char * largura)
 
 
def titulo(texto: str) -> None:
    separador("═")
    print(f"  {texto}")
    separador("═")
 
 
def pausar() -> None:
    input("\n  Pressione ENTER para continuar...")
 
 
# Opção 1: Cadastrar produto
def cadastrar_produto() -> None:
    titulo("CADASTRAR PRODUTO")
 
    nome = input("  Nome do produto: ").strip()
    if not nome:
        print(" Nome não pode ser vazio. ")
        pausar()
        return
 
    try:
        preco = float(input("  Preço (R$): ").replace(",", "."))
        if preco < 0:
            raise ValueError("Preço não pode ser negativo.")
    except ValueError as erro:
        print(f"  ⚠  Entrada inválida: {erro}")
        pausar()
        return
 
    produto = Produto(nome, preco)
    produtos.append(produto)
    print(f"\n  ✔  Produto '{nome}' cadastrado com sucesso!")
    pausar()
 
 
# Opção 2: Listar produtos
def listar_produtos() -> None:
    titulo("PRODUTOS CADASTRADOS")
 
    if not produtos:
        print("  Nenhum produto cadastrado ainda.")
        pausar()
        return
 
    separador()
    print(f"  {'Nº':<4}  {'Nome':<25}  {'Preço':>10}")
    separador()
    for i, p in enumerate(produtos):
        p.exibir(i)
    separador()
    print(f"  Total de produtos: {len(produtos)}")
    pausar()
 
 
# Opção 3: Comprar produto
def comprar_produto() -> None:
    titulo("COMPRAR PRODUTO")
 
    if not produtos:
        print("  Nenhum produto disponível. Cadastre produtos primeiro.")
        pausar()
        return
 
    # Exibe mini-listagem
    separador()
    for i, p in enumerate(produtos):
        p.exibir(i)
    separador()
 
    try:
        indice = int(input("  Número do produto: "))
        if indice < 0 or indice >= len(produtos):
            raise IndexError("Índice fora do intervalo.")
    except ValueError:
        print("  ⚠  Digite um número inteiro válido.")
        pausar()
        return
    except IndexError as erro:
        print(f"  ⚠  Produto não encontrado: {erro}")
        pausar()
        return
 
    try:
        quantidade = int(input("  Quantidade: "))
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero.")
    except ValueError as erro:
        print(f"  ⚠  Entrada inválida: {erro}")
        pausar()
        return
 
    produto_escolhido = produtos[indice]
    total = produto_escolhido.preco * quantidade
 
    separador()
    print(f"  Produto   : {produto_escolhido.nome}")
    print(f"  Quantidade: {quantidade}")
    print(f"  Preço unit: R$ {produto_escolhido.preco:.2f}")
    separador()
    print(f"  TOTAL     : R$ {total:.2f}")
 
    # Expressão relacional e lógica
    if total >= 100:
        print("  Desconto disponível!")
    else:
        print("  Sem desconto (compras a partir de R$ 100,00).")
 
    separador()
    pausar()

    
def exibir_menu() -> None:
    print("      SISTEMA DE CADASTRO E COMPRA")
    print("  1 - Cadastrar produto")
    print("  2 - Listar produtos")
    print("  3 - Comprar produto")
    print("  4 - Sair")
    separador()
 
 
def main() -> None:
    while True:
        exibir_menu()
 
        opcao = input("  Escolha uma opção: ").strip()
 
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            comprar_produto()
        elif opcao == "4":
            separador("═")
            print(" Obrigado por usar o sistema. Até logo!")
            separador("═")
            break
        else:
            print(" Opção inválida. Digite um número entre 1 e 4.")
            pausar()
 
 
# Ponto de entrada 
if __name__ == "__main__":
    main()