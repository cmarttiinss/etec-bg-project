while True:
    #Nome do cliente e Quantidade do Produto
    cliente = input("Digite o nome do cliente: ")
    qtd_produto = int(input("Digite o quantos produtos serão comprados: "))

    total = 0 #guarda o valor da compra feita pelo usuario 

    #Loop para cada produto 
    for i in range(qtd_produto):
        print(f"\nProduto {i+1}")

        nome_produto = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade do produto: "))

        subtotal = preco * quantidade
        print(f"Subtotal: R$ {subtotal:.2f}")

        total += subtotal #soma no total 

    #4 e 5. aplicação do desconto 
    if total >= 500:
        desconto = total * 0.10
    elif total >= 200:
        desconto = total * 0.05
    else:
        desconto = 0

    total_final = total - desconto

    #6. Mostrar resultados 
    print(f"\nCliente: {cliente}")
    print(f"\nTotal: R$ {total:.2f}")
    print(f"\nDesconto: R$ {desconto:.2f}")
    print(f"\nTotal final: R$ {total_final:.2f}")

    #7. Perguntar se deseja nova venda 
    continuar = input("\nDeseja fazer outra venda? (S/N): ").upper()

    #8. Repetir até digitar N 
    if continuar == "N":
        break