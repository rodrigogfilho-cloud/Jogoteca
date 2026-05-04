import random

computador = random.choice(["CARA","COROA"])

jogada = input("""
               
    _________    ____  ___       ____  __  __   __________  ____  ____  ___ 
  / ____/   |  / __ \/   |     / __ \/ / / /  / ____/ __ \/ __ \/ __ \/   |
 / /   / /| | / /_/ / /| |    / / / / / / /  / /   / / / / /_/ / / / / /| |
/ /___/ ___ |/ _, _/ ___ |   / /_/ / /_/ /  / /___/ /_/ / _, _/ /_/ / ___ |
\____/_/  |_/_/ |_/_/  |_|   \____/\____/   \____/\____/_/ |_|\____/_/  |_|

               JOGADAS: 
               - Cara
               - Coroa  
               
                Faça a sua jogada: """).upper()

if jogada == "CARA" and computador == "CARA":
    print(f"Caiu {jogada} seu lindo")
    print("Parabéns! Você ganhou.")
elif jogada == "COROA" and computador == "COROA":
    print(f"Caiu {jogada} seu lindo")
    print("Parabéns! Você ganhou.")
elif jogada == "COROA" and computador == "CARA":
    print(f"Caiu {computador} seu otário")
    print("Você PERDEU BABACA.")
elif jogada == "CARA" and computador == "COROA":
    print(f"Caiu {computador} seu otário")

    print("Você PERDEU BABACA")
else:
    print("Seu energúmeno! Essa palavra não está no jogo!!!")
