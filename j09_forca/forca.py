
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
    palavra_aleatoria = random.choice(lista_palavras).upper()
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
    resposta = input("""
                     Digite uma letra: """).upper()
    while len(resposta) != 1:
        resposta = input("""
                     Eu disse UMA letra: """).upper()
    return resposta
""" letra = perguntar_letra()
    print(letra)"""

def jogar_forca():
    #Tela inicial
    reset()
    print("""\033[35m
         ██  ██████   ██████   ██████      
         ██ ██    ██ ██       ██    ██     
         ██ ██    ██ ██   ███ ██    ██     
    ██   ██ ██    ██ ██    ██ ██    ██     
     █████   ██████   ██████   ██████      
                                       
   ███████  ██████  ██████   ██████  █████  
   ██      ██    ██ ██   ██ ██      ██   ██ 
   █████   ██    ██ ██████  ██      ███████ 
   ██      ██    ██ ██   ██ ██      ██   ██ 
   ██       ██████  ██   ██  ██████ ██   ██ \033[m

           \033[1;4;38mBem-vindo ao jogo\033[m
          
          """)
    
    time.sleep(1)
    input("Pressione ENTER para me vender sua alma ...")
    erro = 0
    #escolher palavra
    palavra_escolhida = escolher_palavra()
    tracos = gerar_tracos(palavra_escolhida)
    tentativas = []

    while True:
        reset()
        #desenhar forca
        desenhar_forca(erro)
        #gerar os traços (tracos)
        print(*tracos)
        print("Tentativas: ", *tentativas)

        if "_" not in tracos:
            print("Dessa vez você se livrou... mas na próxima eu te pego 👿")
            break
        #perguntar letra
        letra_escolhida = perguntar_letra()
        
        if letra_escolhida not in palavra_escolhida:
            erro += 1
            tentativas.append(letra_escolhida)
            if erro == 7:
                reset()
                print(r"""
                           ,--.
                          {    }
                          K,   }
                         /  `Y`
                    _   /   /
                   {_'-K.__/
                     `/-.__L._
                     /  ' /`\_}
                    /  ' /     
            ____   /  ' /
     ,-'~~~~    ~~/  ' /_
   ,'             ``~~~%%',
  (                     %  Y
 {                      %% I
{      -                 %  `.
|       ',                %  )
|        |   ,..__      __. Y
|    .,_./  Y ' / ^Y   J   )|
\           |' /   |   |   ||
 \          L_/    . _ (_,.'(
  \,   ,      ^^""' / |      )
    \_  \          /,L]     /
      '-_`-,       ` `   ./`
         `-(_            )
             ^^\..___,.--`
""")
                print("""
                  
Agora sua alma me pertence !!!
        \033[1;4;38mHAHAHAHAHA\033[m
                  
                  """)
                print(f"""  
    A palavra era \033[1;4;38m{palavra_escolhida}

""")
                break
        if letra_escolhida in palavra_escolhida:
            indice = 0
            for letra in palavra_escolhida:
                if letra == letra_escolhida:
                    tracos [indice] = letra_escolhida
                indice += 1
                       
                
#JOGO
if __name__ == "__main__":
    jogar_forca()