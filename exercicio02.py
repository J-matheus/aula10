import random

secreto= random.randint(1,100)
tentativas=0

print("Bem vindo ao game")
print("Como vai a sua sorte ? bora testar ela")

while True:
    chute=int(input("teste sua sorte, informe um número: "))
    tentativas+=1

    if chute<secreto:
        print("tente um numero maior.")
    elif chute>secreto:
        print("tente um numero menor.")
    else:
        print("Parabéns! Você sua sorte é gigantesca.")
