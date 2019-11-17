#7. Faça uma calculadora que forneça as seguintes opções para o usuário. Cada opção deve usar
#como operando um número lido do teclado e o valor atual da memória. Por exemplo, se o estado atual da
#memória é 5, e o usuário escolhe somar, ele deve informar um novo número (por exemplo, 3). Após a conclusão
#da soma, o novo estado da memória passa a ser 8. Estado da memória: 0 Opções:
#(1) Somar (2) Subtrair (3) Multiplicar (4) Dividir (5) Limpar memória (6) Sair do programa Qual opção você deseja?
print("Bem vindo(a) a calculadora!")
memoria=0
while True:
    operacao=int(input(
          "\n Estado de memória: {}"
          "\n Opções:\n (1) Somar"
          "\n (2) Subtrair"
          "\n (3) Multiplicar"
          "\n (4) Dividir"
          "\n (5) Limpar memória"
          "\n (6) Sair do programa"
          "\n Qual opção você deseja? ".format(memoria)))
    if operacao==1:
        numero=float(input("Você selecionou 1. Somar.\nSomar {} com que número? ".format(memoria)))
        memoria=memoria+numero 
    elif operacao==2:
        numero=float(input("Você selecionou 2. Subtrair.\nSubtrair {} com que número? ".format(memoria)))
        memoria=memoria-numero
    elif operacao==3:
        numero=float(input("Você selecionou 3. Multiplicar.\nMultiplicar {} com que número? ".format(memoria)))
        memoria_casas=memoria*numero
        memoria=round(memoria_casas,2)
    elif operacao==4:
        numero=float(input("Você selecionou 4. Dividir.\nDividir {} com que número? ".format(memoria)))
        while True:
            if numero==0:
                numero=float(input("Não é possível dividir {} por 0. Insira outro número: ".format(memoria)))
            else:
                memoria_casas=memoria/numero
                memoria=round(memoria_casas,2)
                break
    elif operacao==5:
        certeza=int(input("Você selecionou 5. Limpar memória. Tem certeza? Selecione 1 para 'Sim' e 2 para 'Não': "))
        if certeza==1:
            memoria=memoria-memoria
            print("Sua memória foi limpa.")
    elif operacao==6:
        print("Você saiu da calculadora. Sua memória final é {}.". format(memoria))
        break
    else:
        print("Operação inválida, tente novamente.", end=" ")

      