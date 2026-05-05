def maiormenor ():
    import random
    numero_aleatorio = random.randrange(101)
    vida = 3
    print("""\033[35m

                                                                    
                                                                    
    ▄████▄ ████▄  ██ ██  ██ ██ ███  ██ ██  ██ ▄████▄   ████▄   ▄██▄  
    ██▄▄██ ██  ██ ██ ██▄▄██ ██ ██ ▀▄██ ██████ ██▄▄██    ▄██▀  ██  ██ 
    ██  ██ ████▀  ██  ▀██▀  ██ ██   ██ ██  ██ ██  ██   ███▄▄ ▄ ▀██▀  
    \033[m
                                            
    Você deve adivinhar o número em que estou pensando...    
    """)
    dica = print(f"\033[33mDica :\033[m \033[4mo número divido por 5 é ... {round(numero_aleatorio/5,2)}\033[m")
    while vida > 0:
        
        meu_numero = int(input("Escolha um número: "))
        if meu_numero > numero_aleatorio:
            print("Chute um número menor.")
        elif meu_numero < numero_aleatorio:
            print("Chute um número maior.")
        elif meu_numero == numero_aleatorio:
            print("Parabéns! Você acertou.")
            break
        vida = vida - 1
    while vida == 0:
        print(f"Sinto muito! Mas você perdeu, o número era {numero_aleatorio}")
        vida += 1
    