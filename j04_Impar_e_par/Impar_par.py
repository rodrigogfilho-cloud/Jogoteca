import random

numerodocomputer = random.randrange(11)

impar = input("Você escolhe impar ou par? ").upper()

if impar == "IMPAR":
       print("então eu sou par")
elif impar == "PAR":
       print("então eu sou impar")
else:
        print("Não reconheço esse palavra")
        exit()

numero = int(input("Escolha um número de 0 a 10: "))
resultado = numero + numerodocomputer
if numero > 10:
        print("Você não tem dedos o suficiente")
        exit()

if impar == "PAR":
    if resultado % 2 == 0 :
        print(f"{numero} + {numerodocomputer} = {resultado} que é par")
        print("Parabéns!!! Você era par e ganhou.")
    else:
           print(f"{numero} + {numerodocomputer} = {resultado} que é impar")
           print("Você perdeu BOBOCA!")
if impar == "IMPAR":
    if resultado % 2 == 1 :
            print(f"{numero} + {numerodocomputer} = {resultado} é ímpar")
            print("Parabéns!!! Você era impar e ganhou.")
    else:
              print(f"{numero} + {numerodocomputer} = {resultado} que é par")
              print("Você perdeu BOBOCA!")