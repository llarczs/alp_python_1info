peso = float(input("digite seu peso (kg): "))
# Corrigida a linha da altura que estava quebrada incorretamente na imagem
altura = float(input("digite sua altura: "))

imc = peso / (altura ** 2)

print(f"IMC: {imc:.2f}")

if imc < 18.5:
    print("abaixo do peso")
elif imc < 25:
    print("peso normal")
elif imc < 30:
    print("sobrepeso")
elif imc < 35:
    print("obesidade grau 1")
elif imc < 40:
    print("obesidade grau 2")
else:
    print("obesidade grau 3")
