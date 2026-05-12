def geniusus ():
    import os
    import time
    import random

    def reset ():
        os.system("color 07")
        os.system("cls")

    reset()
    def mudar_cor(cor):
        codigo_cor = dicionario_de_cores [cor] 
        os.system(f"color {codigo_cor}")          
        time.sleep(1)
        reset()

    dicionario_de_cores = {"LILAS":"D0",
                        "AZUL":"90",
                        "AMARELO":"60",
                        "VERMELHO":"C0",
                        "ROXO" : "50",}

    lista_sequencia = []

    print("""██████  ███████ ███    ███       ██    ██ ██ ███    ██ ██████   ██████     
██   ██ ██      ████  ████       ██    ██ ██ ████   ██ ██   ██ ██    ██   
██████  █████   ██ ████ ██ █████ ██    ██ ██ ██ ██  ██ ██   ██ ██    ██    
██   ██ ██      ██  ██  ██        ██  ██  ██ ██  ██ ██ ██   ██ ██    ██   
██████  ███████ ██      ██         ████   ██ ██   ████ ██████   ██████   
                                                                                                                                        
 █████   ██████       ██████  ███████ ███    ██ ██ ██    ██ ███████ 
██   ██ ██    ██     ██       ██      ████   ██ ██ ██    ██ ██      
███████ ██    ██     ██   ███ █████   ██ ██  ██ ██ ██    ██ ███████ 
██   ██ ██    ██     ██    ██ ██      ██  ██ ██ ██ ██    ██      ██ 
██   ██  ██████       ██████  ███████ ██   ████ ██  ██████  ███████
        """)

    input("                 Pressione ENTER para começar...")
    reset()


    lista_cores = ["VERMELHO", "AZUL", "LILAS", "ROXO", "ROXO"]
    #Fases
    fase = 1
    while True:
        
        
        #Escolho uma cor aleatória

        cor_aleatoria = random.choice(lista_cores)

        #Insiro cor aleatória dentro da lista de sequência que vai guardar todas as cores

        lista_sequencia.append (cor_aleatoria)

        #Percorro à lista e utilizo a função "mudar_cor" para exibir as cores

        for color in lista_sequencia:
            mudar_cor(color)

        #Menu de cores

        print("""
                        V-VERMELHO
                        A-AZUL
                        L-LILAS
                        R-ROXO
                        Y-AMARELO (YELLOW)
        """)
        resposta = input("Digite a sequência correta: ").upper()

        dicionario_abreviacoes = {"V" : "VERMELHO",
                                "A" : "AZUL",
                                "L" : "LILAS",
                                "R" : "ROXO",
                                "Y" : "AMARELO"}
        
        #transformando a resposta em uma lista
        lista_respostas = []

        for letra in resposta:
            cor = dicionario_abreviacoes.get(letra)
            lista_respostas.append(cor)
        if lista_respostas != lista_sequencia:
            print("Você errou PANACA!")
            print(f"A sequência era: ")
            print(*lista_sequencia)
            time.sleep(3)
            reset()
            break
        else:
            print("""Você acertou!!!
                """)
            print(f"""Vamos para o nível {fase}😏
                """)
            time.sleep(1.5)
            input("Aperte ENTER quando estiver pronto...")
            reset()
        fase = fase+1