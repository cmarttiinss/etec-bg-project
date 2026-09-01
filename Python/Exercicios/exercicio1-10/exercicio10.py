Nota = float(input("Informe sua nota: "))

print(f"{'Você foi aprovado :D' if Nota >= 7 else 'Recuperação :(' if Nota >= 5 else 'Você Reprovado.'}")