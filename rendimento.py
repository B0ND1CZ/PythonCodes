print("Qual seu rendimento anual?")

rendimento = float( input() )

if (rendimento <= 28000):
    print("Você está isento")
    porcentagem = 0 
elif(rendimento > 28000 and rendimento <= 35000):
    print("Você vai pagar 10%")
    porcentagem = 10
else:
    print("você vai pagar 25%")
    porcentagem = 25

if(porcentagem > 0 ):
     imposto_pagar = rendimento * (porcentagem / 100)
     print("Você vai pagar ", imposto_pagar)
4504