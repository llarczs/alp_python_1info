n1 = float(input("digite o primeiro número positivo: "))
n2 = float(input("digite o segundo número positivo: "))

print("\nMENU")
print("1 - média ponderada(pesos 2 e 3)")
print("2 - quadrado da soma dos 2 números")
print("3 - o cubo do menor número")

opcao = int(input("escolha uma opção: "))

if opcao == 1:
    media = (n1 * 2 + n2 * 3) / 5
    print("média ponderada: ", media)
elif opcao == 2:
    # Corrigida a quebra de linha incorreta que estava no operador **
    resultado = (n1 + n2) ** 2
    print("o quadrado da soma: ", resultado)
elif opcao == 3:
    menor = min(n1, n2)
    resultado = menor ** 3
    print("cubo do menor número: ", resultado)
else:
    print("opção inválida")
