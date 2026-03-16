import random
primeiro = random.randrange(21)
segundo = random.randrange(21)
resultado = primeiro * segundo
pergunta = int(input(f" Quanto que é {primeiro} x {segundo}? "))
if pergunta == resultado:
    print(f" Parabéns! você está certo. O resultado é: {resultado}")
else:
    print(f"SEU BURRO! estude mais na próxima. O resultado é: {resultado}")