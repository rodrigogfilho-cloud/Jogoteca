
import os
import time
import random


def reset ():
    os.system("cls")

def escolher_palavra () -> str:
    """Escolhe e retorna uma palavra aleatória"""
    lista_palavras = ["GODOFREDO",
                      "ALEX",
                      "SENAI",
                      "BONITO",
                      "LEGAL",
                      "SESI"]
    palavra_aleatoria = random.choice(lista_palavras)
    #retorna a palavra para quem chamou a função
    return palavra_aleatoria
    
def desenhar_forca (erro:int):
    """"Imprime o desenho da forca dependendo da quantidade de erros"""
    reset()
    if erro == 0 :
        print("""
    __________
   |         !
   |
   |
   |
   |
   |    
""")
    
    elif erro == 1:
        print("""
    __________
   |         !
   |       (x x)
   |
   |
   |
   |    
""")
       
    elif erro == 2:
        print("""
    __________
   |         !
   |       (x x)
   |         |
   |
   |
   |
   |    
""")
      
    elif erro == 3:
        print("""
    __________
   |         !
   |       (x x)
   |         |-
   |
   |
   |    
""")
       
    elif erro == 4:
        print("""
    __________
   |         !
   |       (x x)
   |        -|-
   |
   |
   |    
""")
        
    elif erro == 5:
        print(r"""
    __________
   |         !
   |       (x x)
   |        -|-
   |          \
   |
   |    
""")
        
    elif erro == 6:
        print(r"""
    __________
   |         !
   |       (x x)
   |        -|-
   |        / \
   |
   |    
""")
      
        print("VOCÊ PERDEU !!!")

#desenhar_forca(1)
#reset()

def gerar_tracos (palavra:str)->list:
    """Gera e retorna uma lista contendo underlines na mesma quantidade de letras das palavras"""
    contador = 0 
    quantidade_de_letras = len(palavra)
    tracos = []
    while contador < quantidade_de_letras:
        contador += 1
        tracos.append("_")
    return tracos

"""lista_tracos = gerar_tracos("")"""
"""print(*lista_tracos)"""

def perguntar_letra () -> str:
    resposta = input("Digite uma letra: ").upper()
    while len(resposta) != 1:
        resposta = input("Eu disse UMA letra: ").upper()
    return resposta
""" letra = perguntar_letra()
    print(letra)"""

def jogar_forca():
    #Tela inicial

    print("""
         ██  ██████   ██████   ██████      
         ██ ██    ██ ██       ██    ██     
         ██ ██    ██ ██   ███ ██    ██     
    ██   ██ ██    ██ ██    ██ ██    ██     
     █████   ██████   ██████   ██████      
                                       
   ███████  ██████  ██████   ██████  █████  
   ██      ██    ██ ██   ██ ██      ██   ██ 
   █████   ██    ██ ██████  ██      ███████ 
   ██      ██    ██ ██   ██ ██      ██   ██ 
   ██       ██████  ██   ██  ██████ ██   ██ 

           Bem-vindo ao jogo""")

if __name__ == "__main__":
    jogar_forca()
