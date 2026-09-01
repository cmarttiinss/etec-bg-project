soma = 0
tentativas = 0
while tentativas < 5:
    cal = float(input("Digite um numero: "))
    tentativas += 1
    soma += cal
print(f"O marrento total é de {soma} marrentos.")