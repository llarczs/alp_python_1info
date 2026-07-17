nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("aprovado")
elif media >= 4:  # Corrigido o erro de sintaxe '>=4=' que estava na imagem
    print("prova final")
else:
    print("reprovado")
