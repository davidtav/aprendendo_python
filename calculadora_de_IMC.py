print("""Óla, vamos medir seu IMC !
insira seu peso""")
peso=int(input())
print("insira sua altura")
altura=float(input())
imc=peso/altura**2
if(imc<18.5):
    print("Você está abaixo do seu peso ideal, se alimente melhor")
elif(imc>=18.5 and imc<25):
    print("Você esta no seu peso ideal, Parabens!")
elif(imc>=25 and imc<30):
    print("tome cuidado, voce está acima do seu peso considerado ideal")
elif(imc>30):
    print("Você está acima do seu peso ideal, procure um nutricionsta !")
print("Espero ter ajudado, tenha um bom dia")