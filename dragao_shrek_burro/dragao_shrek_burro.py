import random

nome_aleatorio = random.choice(["DRAGÃO","SHREK","BURRO"])

escolha = input("""

ESCOLHA UMA DAS OPÇÕES:

- Dragão                      
- Shrek
- Burro

                Digite aqui : """).upper()


if escolha == "DRAGÃO":
    print("""Agora minha vez...
          
          """)
          

elif escolha == "SHREK":
    print("""Agora minha vez...
          
          """)

elif escolha == "BURRO":
    print("""Agora minha vez...
          
          """)
else:
    print("Não entendi")

if escolha == nome_aleatorio:
     

     print(f"Vocês escolheram o {escolha}. Vocês empataram.")
     exit()

   

if escolha == "DRAGÃO" and nome_aleatorio == "SHREK":
    print(f"{escolha} é mais forte que {nome_aleatorio}")
    print("Você ganhou!!!")
elif escolha == "DRAGÃO" and nome_aleatorio == "BURRO":
    print(f"{nome_aleatorio} é mais forte que {escolha}")
    print("Você perdeu BABACA")
elif escolha == "SHREK" and nome_aleatorio == "BURRO":
    print(f"{escolha} é mais forte que {nome_aleatorio}")
    print("Você ganhou!!!")
elif escolha == "SHREK" and nome_aleatorio == "DRAGÃO":
    print(f"{nome_aleatorio} é mais forte que {escolha}")
    print("Você perdeu BABACA")
elif escolha == "BURRO" and nome_aleatorio == "DRAGÃO":
    print(f"{escolha} é mais forte que {nome_aleatorio}")
    print("Você ganhou!!!")
elif escolha == "BURRO" and nome_aleatorio == "SHREK":
    print(f"{nome_aleatorio} é mais forte que {escolha}")
    print("Você perdeu BABACA")