a = float(input("Digite a primeira estatura: "))
b = float(input("Digite a segunda estatura: "))
c = float(input("Digite a terceira estatura: "))

if a == b or a == c or b == c:
    print("Há, pelo menos, 2 pessoas com a mesma estatura")

elif a > b and a > c:
    print("Maior estatura:", a)

elif b > a and b > c:
    print("Maior estatura:", b)

else:
    print("Maior estatura:", c)
