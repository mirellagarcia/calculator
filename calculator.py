print("Bem-vindo a calculadora da Mirella")
print("1- Somar")
print("2- Subtrair")
print("3- Multiplicação")
print("4- Divisão ")
print("5- Exponencial ")
menu = int(input("Digite o número referente a operação desejada: "))
numero1 = int(input("digite o valor 1: "))
numero2 = int(input("digite o valor 2: "))

def calculadora():
    if (menu == 1): 
      print("Soma: ",numero1+numero2)
    elif (menu == 2):
      print("Subtração: ",numero1-numero2)
    elif (menu == 3): 
      print("Multiplicação: ",numero1*numero2)
    elif (menu == 4):
      if int(numero2) == 0:
        print('não pode executar')
      else:
          print("Divisão: ",numero1/numero2)
    elif (menu == 5): 
      print("Exponencial: ",numero1**numero2)
    else:
      print("Tente novamente e insira uma operação valida")
calculadora()
