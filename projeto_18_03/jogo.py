import random

nivel = int(input("Escolha o nível:\n[1] Fácil,\n[2] Médio,\n[3] Difícil"))
intervalo = {1:20, 2:50, 3:100}
numero_secreto = random.randint(1,intervalo)

tentativa = {1:10, 2:7, 3:5}
Pontos: 1000
print("Bem-vindo ao jogo de adivinhação!")
print(f"Tente adivinhar um número entre 1 e {intervalo}. Você tem {tentativa} tentativas.")

for tentativa in range(1, max_tentativas + 1):
    palpite = int(input(f"Tentativa {tentativa}: Digite seu palpite: "))

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativa} tentativa(s).")
        break
    elif palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    else:
        print("Muito alto! Tente novamente.")

else:
    print(f"Fim do jogo! O número era {numero_secreto}.")