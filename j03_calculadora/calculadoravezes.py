def calculadora ():  
    import random
    primeiro = random.randrange(101)
    segundo = random.randrange(101)


    resultado = primeiro * segundo
    resultado1 = primeiro / segundo
    resultado2 = primeiro - segundo
    resultado3 = primeiro + segundo

    sixseven = "67"
    multiplicação = "*"
    divisão = "/"
    subtração = "-"
    adição = "+"
    print("""\033[36m                                                                                   
██▄  ▄██ ██████  ▄████  ▄████▄     ▄█████ ▄████▄ ██     ▄█████ ██  ██ ██     ▄████▄ ████▄  ▄████▄ █████▄  ▄████▄     ▄██▀▀▀ ██████
██ ▀▀ ██ ██▄▄   ██  ▄▄▄ ██▄▄██     ██     ██▄▄██ ██     ██     ██  ██ ██     ██▄▄██ ██  ██ ██  ██ ██▄▄██▄ ██▄▄██     ██▄▄▄    ▄██▀
██    ██ ██▄▄▄▄  ▀███▀  ██  ██     ▀█████ ██  ██ ██████ ▀█████ ▀████▀ ██████ ██  ██ ████▀  ▀████▀ ██   ██ ██  ██     ▀█▄▄█▀  ██▀                                                                                                                                  
\033[m
""")
    conta = input("""Escolha a operação que você deseja: 
                        
                        Multiplicação *
                        Divisão /
                        Subtração -
                        Adição +
            
                        Operação: """)


    if conta == multiplicação:
        resposta = int(input(f"Quanto que é {primeiro} x {segundo} ? "))
        if resposta == resultado:
            print (f"Parabéns! A resposta era {resultado}")
        else:

            print(f"Sinto muito. Mas você errou. A resposta certa é {resultado}")


    if conta == divisão:
        resposta1 = int(input(f"Quanto que é {primeiro} : {segundo} ? "))
        if resposta1 == resultado1:
            print (f"Parabéns! A resposta era {resultado1}")
        else:


            print(f"Sinto muito. Mas você errou. A resposta certa é {resultado1}")


    if conta == subtração:
        resposta2 = int(input(f"Quanto que é {primeiro} - {segundo} ? "))
        if resposta2 == resultado2:
            print (f"Parabéns! A resposta era {resultado2}")
        else:
                print(f"Sinto muito. Mas você errou. A resposta certa é {resultado2}")


    if conta == adição:
        resposta3 = int(input(f"Quanto que é {primeiro} + {segundo} ? "))
        if resposta3 == resultado3:
            print (f"Parabéns! A resposta era {resultado3}")
        else:
            
                print(f"Sinto muito. Mas você errou. A resposta certa é {resultado3}")

    if conta == sixseven:
        print("""

                            ████████  ██████████
                            ███▒▒▒▒███▒███▒▒▒▒███
                            ▒███   ▒▒▒ ▒▒▒    ███ 
                            ▒█████████       ███  
                            ▒███▒▒▒▒███     ███   
                            ▒███   ▒███    ███    
                            ▒▒████████    ███     
                            ▒▒▒▒▒▒▒▒    ▒▒▒      
                        
                        
        ███████╗██╗██╗  ██╗    ███████╗███████╗██╗   ██╗███████╗███╗   ██╗
        ██╔════╝██║╚██╗██╔╝    ██╔════╝██╔════╝██║   ██║██╔════╝████╗  ██║
        ███████╗██║ ╚███╔╝     ███████╗█████╗  ██║   ██║█████╗  ██╔██╗ ██║
        ╚════██║██║ ██╔██╗     ╚════██║██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║
        ███████║██║██╔╝ ██╗    ███████║███████╗ ╚████╔╝ ███████╗██║ ╚████║
        ╚══════╝╚═╝╚═╝  ╚═╝    ╚══════╝╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝



    """)