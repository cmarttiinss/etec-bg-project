ValorProduto =float(input(" Digite o valor do produto: "))
QuantidadeProduto =float(input(" Digite a quantidade do produto: "))

def calculo_produtos(valor, produto):
    return(valor * produto)

print(f" O valor total da sua compra é: {calculo_produtos(ValorProduto, QuantidadeProduto)}" )