lista_pares = []
lista_impares = []

for i in range(1, 11):
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)

lista_completa = sorted(lista_pares + lista_impares)


print(f"Pares: {lista_pares}")
print(f"Ímpares: {lista_impares}")
print(f"Lista completa: {lista_completa}")
