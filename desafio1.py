h1 = int(input("Informe a primeira hora: "))
m1 = int(input("Informe o primeiro minuto: "))
h2 = int(input("Informe a segunda hora: "))
m2 = int(input("Informe o segundo minuto: "))

somahoras = h1 + h2
somaminutos = m1 + m2

if somaminutos >= 60:
    somahoras = somahoras + 1
    somaminutos = somaminutos - 60

if somahoras > 24:
    somahoras = somahoras - 24

if somahoras > 12:
    somahoras = somahoras - 12

print (f"a soma é {somahoras} : {somaminutos}")