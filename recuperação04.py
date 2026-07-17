print("=== calculadora de números reais ===")
print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")

opcao = int(input("escolha a operação: "))

n1 = float(input("digite o primeiro número: "))
n2 = float(input("digite o segundo número: "))

if opcao == 1:
    resultado = n1 + n2
elif opcao == 2:
    resultado = n1 - n2
elif opcao == 3:
    resultado = n1 * n2
elif opcao == 4:
    if n2 != 0:
        resultado = n1 / n2
    else:
        print("Não é possível dividir por zero")
        exit()
else:
    print("opção inválida.")
    exit()

print("resultado: ", resultado)
