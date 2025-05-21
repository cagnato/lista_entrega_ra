# Criar tabuleiro 3x3
tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

jogador = "X"
jogadas = 0
vencedor = False

while jogadas < 9 and not vencedor:
    # Mostrar tabuleiro
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

    print("Vez do jogador:", jogador)

    linha = int(input("Digite a linha (0, 1 ou 2): "))
    coluna = int(input("Digite a coluna (0, 1 ou 2): "))

    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador
        jogadas += 1

        # Verificar linhas
        for i in range(3):
            if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
                vencedor = True

        # Verificar colunas
        for i in range(3):
            if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " ":
                vencedor = True

        # Verificar diagonais
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
            vencedor = True
        if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
            vencedor = True

        if vencedor:
            for linha in tabuleiro:
                print(" | ".join(linha))
                print("-" * 9)
            print("🎉 Jogador", jogador, "venceu!")
        elif jogadas == 9:
            for linha in tabuleiro:
                print(" | ".join(linha))
                print("-" * 9)
            print("🤝 Empate!")
        else:
            if jogador == "X":
                jogador = "O"
            else:
                jogador = "X"
    else:
        print("⚠️ Posição ocupada. Tente novamente.")
