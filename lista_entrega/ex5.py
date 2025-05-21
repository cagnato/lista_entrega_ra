lista = []

for i in range(3):
    palavra = input(f"Digite a {1+i}ª palavra: ")
    lista.append(palavra)

menorPalavra = min(lista, key = len)
maiorPalavra = max(lista, key = len)

print(f"A maior palavra da lista {lista} é {maiorPalavra}, já a menor palavra é {menorPalavra}: ")