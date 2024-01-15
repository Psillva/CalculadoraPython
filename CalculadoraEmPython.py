#Código simulando uma+9  calculadora

#Solicitando o primeiro número ao usuário
numero1 = int(input("Digite o primeiro número: "))
print("Escola a operação que deseja realizar")
print("1 - Soma (+) \n2 - Divisão (/) \n3 - Multiplicação (x) \n4 - Subtração (-)")
#Armazenando a operação que será realizada
operacao = input("Operação: ")
#Solicitando o segundo número ao usuário
numero2 = int(input("Digite o segundo número: "))

#Codições
#Operação de Soma
if operacao == "+":
    somaDosNumeros = numero1 + numero2
    print(numero1, "+", numero2, "=", somaDosNumeros)
    #Operação de Divisão
if operacao == "/":
    divisaoDosNumeros = numero1 / numero2
    print(numero1, "/", numero2, "=", divisaoDosNumeros)
#Operação de Multiplicação    
if operacao == "x" or operacao == "X" or operacao == "*":
    multiplicaoDosNumeors = numero1 * numero2
    print(numero1, "x", numero2, "=", multiplicaoDosNumeors)
#Operação de Subtração
if operacao == "-":
       subtracaoDosNumero = numero1 - numero2
       print(numero1, "-", numero2, "=", subtracaoDosNumero) 
