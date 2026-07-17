print("=== BLACK FRIDAY ===")
valor = float(input("digite o valor da compra: ")) # Linha corrigida e unificada

print("\nForma de pagamento: ")
print("1 - a vista (15% de desconto)")
print("2 - cartão de débito (10% de desconto)")
print("3 - cartão de crédito (5% de desconto)")

# Adicionada a leitura do código que estava faltando no código original da foto
codigo = int(input("Escolha a opção de pagamento: ")) 

if codigo == 1:
    desconto = valor * 0.15
elif codigo == 2:
    desconto = valor * 0.10
elif codigo == 3:
    desconto = valor * 0.05
else:
    print("código inválido!")
    exit()

valor_final = valor - desconto

print(f"desconto: R$ {desconto:.2f}")
print(f"valor final a pagar: R$ {valor_final:.2f}")
