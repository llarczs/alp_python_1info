salario = float(input("Digite o salário: "))
cargo = input("Digite o cargo: ")

if cargo == "Programador de Sistemas":
    novo = salario + (salario * 0.30)
    print("Novo salário:", novo)

elif cargo == "Analista de Sistemas":
    novo = salario + (salario * 0.20)
    print("Novo salário:", novo)

elif cargo == "Analista de Banco de Dados":
    novo = salario + (salario * 0.15)
    print("Novo salário:", novo)

else:
    print("Cargo inválido")
