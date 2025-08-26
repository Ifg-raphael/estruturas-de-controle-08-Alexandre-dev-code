# Sua solução aqui
altura = float(input())
genero = input()

if "M" in genero:
    peso = (72.7 * altura) - 58

if "F" in genero:
    peso = (62.1 * altura) - 44.7

print(f"{peso:.2f}")