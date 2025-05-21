lista = []
lista2 = []

for i in range(1, 11):
    quadrado = i ** 2
    lista.append(i)
    lista2.append(quadrado)

soma = sum(lista2)

print(f"a lista {lista} ao quadrado é {lista2}")
print(f"Já a soma dos elementos da lista ao quadrado é {soma}")
