#2. Faça um programa que leia um numero inteiro entre 0 e 100 e escreva o seu valor por extenso.

#Fazendo por tuplas
extenso_unidade=("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove")
extenso_dezena_dez=("dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove")
extenso_dezena_outras_exatas=("erro","erro","vinte", "trinta", "quarenta", "cinquenta", "sesenta", "setenta", "oitenta", "noventa", "cem")
extenso_dezena_outras_mais=("erro", "erro", "vinte e ", "trinta e ", "quarenta e ", "cinquenta e ", "sessenta e ", "setenta e ", "oitenta e ", "noventa e ")

while True: #Não digitar um número fora desse intervalo
    numero= float(input('Digite um número entre 0 a 100: '))
    if numero>= 0 and numero <= 100:
        break
    print("Número inválido, tente novamente.", end=" ") #O end é para ele não pular linha no loop
lista=[1,2,3,4,5,6,7,8,9,10]
if numero<10:
    numero_int=int(numero) #Tupla não reconhece tipo float
    extenso=extenso_unidade[numero_int]
elif numero>=10 and numero<20:
    numero=numero-10
    numero_int=int(numero) 
    extenso=extenso_dezena_dez[numero_int]
elif numero/10 in lista:
    numero=numero/10
    numero_int=int(numero) 
    extenso=extenso_dezena_outras_exatas[numero_int]
else:
    numero_para_dezena=numero/10
    numero_para_unidade=numero%10
    numero_para_dezena_int=int(numero_para_dezena)
    numero_para_unidade_int=int(numero_para_unidade)
    
    extenso=extenso_dezena_outras_mais[numero_para_dezena_int] + extenso_unidade[numero_para_unidade_int]
    
print("Seu número é {}.".format(extenso))

    