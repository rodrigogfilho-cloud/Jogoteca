def adivinhanumero():
    import random

    numero_aleatorio = random.randrange(11)
    numero_aleatorio2 = random.randrange(21)
    numero_aleatorio3 = random.randrange(51)
    numero_aleatorio4 = random.randrange(201)
    numero_aleatorio67 = random.randrange(67, 68)


    dificuldade = int(input("""
                        
                                                                                                            
                                                                                                                                    
    ,---.  ,------.  ,--.,--.   ,--.,--.,--.  ,--.,--.  ,--.  ,---.      ,--.  ,--.,--. ,--.,--.   ,--.,------.,------.  ,-----.  
    /  O  \ |  .-.  \ |  | \  `.'  / |  ||  ,'.|  ||  '--'  | /  O  \     |  ,'.|  ||  | |  ||   `.'   ||  .---'|  .--. ''  .-.  ' 
    |  .-.  ||  |  \  :|  |  \     /  |  ||  |' '  ||  .--.  ||  .-.  |    |  |' '  ||  | |  ||  |'.'|  ||  `--, |  '--'.'|  | |  | 
    |  | |  ||  '--'  /|  |   \   /   |  ||  | `   ||  |  |  ||  | |  |    |  | `   |'  '-'  '|  |   |  ||  `---.|  |\  \ '  '-'  ' 
    `--' `--'`-------' `--'    `-'    `--'`--'  `--'`--'  `--'`--' `--'    `--'  `--' `-----' `--'   `--'`------'`--' '--' `-----'  
                                                                                                                                    
                                            ,------.  ,------.  ,------.  
                                            '  .--.  ''  .--.  ''  .--.  ' 
                                            '--' _|  |'--' _|  |'--' _|  | 
                                                .--' _'   .--' _'   .--' _'  
                                                `---'     `---'     `---'     
                                                .---.     .---.     .---.     
                                                '---'     '---'     '---'                    
                        
                                    (1-NOOB, 2-MÉDIO, 3-PROFISSONAL OU 4-SENAI)
                                            QUAL DIFICULDADE VOCÊ DESEJA: """))

    if dificuldade == 1:
        print("""Você aparenta ser um NOOB por enquanto. Responda a pergunta à baixo.
            """)
        print(f"DICA: O dobro do seu número é {numero_aleatorio * 2}")
        numero1 = int(input("Chute um número de 0 a 10: "))
        if numero1 == numero_aleatorio:
            print(f"Parabéns!!! o número era {numero_aleatorio}")
        else:
            print(f"Você está errado! meu número não era {numero1}, era {numero_aleatorio}")
    elif dificuldade == 2:
        print("""Você aparenta estar no nível MÉDIO por agora. Responda a pergunta à baixo.
            """)
        print(f"DICA: O dobro do seu número é {numero_aleatorio2 * 2}")
        numero2 = int(input("Chute um número 0 a 20: "))
        if numero2 == numero_aleatorio2:
            print(f"Parabéns!!! o número era {numero_aleatorio2}")
        else:
            print(f"Você está errado! meu número não era {numero2}, era {numero_aleatorio2}")
    elif dificuldade == 3:
        print("""UAU! Você já está em um nível acima da maioria das pessoas, parabéns. Responda a pergunta à baixo.
            """)
        print(f"DICA: O dobro do seu número é {numero_aleatorio3 * 2}")
        numero3 = int(input("Chute um número 0 a 50: "))
        if numero3 == numero_aleatorio3:
            print(f"Parabéns!!! o número era {numero_aleatorio3}")
        else:
            print(f"Você está errado! meu número não era {numero3}, era {numero_aleatorio3}")
    elif dificuldade == 4:
        print("""UOUUUUU! VOCÊ ESTÁ NO NÍVEL MAIS MAIS DO MUNDO, O NÍVEL >>>SENAI<<<. Responda a pergunta à baixo.
            """)
        print(f"DICA: O dobro do seu número é {numero_aleatorio4 * 2}")
        numero4 = int(input("Chute um número 0 a 200: "))
        if numero4 == numero_aleatorio4:
            print(f"Parabéns!!! o número era {numero_aleatorio4}")
        else:
            print(f"Você está errado! meu número não era {numero4}, era {numero_aleatorio4}")
    elif dificuldade == 67:
        print("""UOUUUUUUUU VOCÊ DESCOBRIU O NÍVEL EXPERT MASTER ESPECIAL SUPER ULTRA BLASTER AURUDO AURA. Responda a pergunta à baixo.
            """)
        print(f"DICA: É O NÚMERO MAIS AURA DO MUNDO!!!")
        numero67 = int(input("Chute um número: "))
        if numero67 == numero_aleatorio67:
            print(f"""
                
            
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
                
                
                Parabéns!!! o número era {numero_aleatorio67}""")
        else:
            print(f"Você está errado! meu número não era {numero67}, era {numero_aleatorio67}")


    else:
        print("""        
            
            
                Sentimos muito!!!
            Mas por Hora este nível
                não EXISTE.
            
    MAS ESTAMOS TRABALHANDO MAIS RÁPIDO POSSÍVEL PARA DESENOLVER MAIS NÍVEIS.
            

            """)
