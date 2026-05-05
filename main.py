
from j01_mad_libs.mad_libs import madlib
from j02_adivinha_o_numerp.adivinhanumero import adivinhanumero
from j03_calculadora.calculadoravezes import calculadora
from j04_Impar_e_par.Impar_par import imparpar
from j05_cara_ou_coroa.caraoucoroa import caracoroa
from j06_dragao_shrek_burro.dragao_shrek_burro import shrek
from j07_maior_ou_menor.maior_menor import maiormenor
print("""\033[31m
          
 ▄▄▄██▀▀▀▒█████    ▄████  ▒█████  ▄▄▄█████▓▓█████  ▄████▄   ▄▄▄      
   ▒██  ▒██▒  ██▒ ██▒ ▀█▒▒██▒  ██▒▓  ██▒ ▓▒▓█   ▀ ▒██▀ ▀█  ▒████▄    
   ░██  ▒██░  ██▒▒██░▄▄▄░▒██░  ██▒▒ ▓██░ ▒░▒███   ▒▓█    ▄ ▒██  ▀█▄  
▓██▄██▓ ▒██   ██░░▓█  ██▓▒██   ██░░ ▓██▓ ░ ▒▓█  ▄ ▒▓▓▄ ▄██▒░██▄▄▄▄██ 
 ▓███▒  ░ ████▓▒░░▒▓███▀▒░ ████▓▒░  ▒██▒ ░ ░▒████▒▒ ▓███▀ ░ ▓█   ▓██▒
 ▒▓▒▒░  ░ ▒░▒░▒░  ░▒   ▒ ░ ▒░▒░▒░   ▒ ░░   ░░ ▒░ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░
 ▒ ░▒░    ░ ▒ ▒░   ░   ░   ░ ▒ ▒░     ░     ░ ░  ░  ░  ▒     ▒   ▒▒ ░
 ░ ░ ░  ░ ░ ░ ▒  ░ ░   ░ ░ ░ ░ ▒    ░         ░   ░          ░   ▒   
 ░   ░      ░ ░        ░     ░ ░              ░  ░░ ░            ░  ░
                                                  ░                  
              
                 \033[1;4;31mDeselvolvido por : Rodrigo Godoxz\033[m
------------------------------------------------------------------------- 
          """)
while True:
    print("""
                \033[36m (0) - \033[33m Sair
                \033[36m (1) - \033[33m Mad Libs
                \033[36m (2) - \033[33m Adivinha Número
                \033[36m (3) - \033[33m Calculadora
                \033[36m (4) - \033[33m Impar ou Par
                \033[36m (5) - \033[33m Cara ou Coroa
                \033[36m (6) - \033[33m Dragão, Shrek e o Burro
                \033[36m (7) - \033[33m Adivinha Número 2.0
        """)
    jogo = int(input("          Qual jogo você vai desejar jogar: " ))

    if jogo == 1:
        
        madlib()
    elif jogo == 2:
        
        adivinhanumero()
    elif jogo == 3:
        
        calculadora()
    elif jogo == 4:
        
        imparpar()
    elif jogo == 5:
        
        caracoroa()
    elif jogo == 6:
        shrek()
    elif jogo == 7:
        maiormenor()
    elif jogo == 0:
        print ("Até já...")
        break

