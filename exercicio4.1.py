soma=0
for i in range(1,6,1):
    notas=int(input("Informe as cinco notas: "))
    soma= soma + notas
media= soma/5
print(media)
if media>=7 and media<=10:
    print("Aprovado")
elif media<4:
    print("Reprovado")
elif media>= 4 and media<=7:
    print("Recuperação")
else:
    print("Número invalido.")