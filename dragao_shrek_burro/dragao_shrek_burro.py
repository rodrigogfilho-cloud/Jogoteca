import random

nome_aleatorio = random.choice(["DRAGÃO","SHREK","BURRO"])

escolha = input("""

ESCOLHA UMA DAS OPÇÕES:

- Dragão                      
- Shrek
- Burro

                Digite aqui : """).upper()


if escolha == "DRAGÃO" and nome_aleatorio == "SHREK":
    print(f"{escolha} é mais forte do que o {nome_aleatorio}")
    print("Você ganhou")

if escolha == "SHREK" and nome_aleatorio == "BURRO":
    print(f"{escolha} é mais forte do que o {nome_aleatorio}")
    print("Você ganhou")

if escolha == "BURRO" and nome_aleatorio == "DRAGÃO":
    print(f"{escolha} é mais forte do que o {nome_aleatorio}")
    print("Você ganhou")

if escolha == "DRAGÃO" and nome_aleatorio == "DRAGÃO":
    print(f"Ambos são o {escolha}, vocês tem a mesma força")
    print("Vocês empataram")

if escolha == "SHREK" and nome_aleatorio == "SHREK":
    print(f"Ambos são o {escolha}, vocês tem a mesma força")
    print("Vocês empataram")

if escolha == "BURRO" and nome_aleatorio == "BURRO":
    print(f"Ambos são o {escolha}, vocês tem a mesma força")
    print("Vocês empataram")

else:
             print("Sinto muito! Mas esse personagem/nome não está inserido ao jogo")

