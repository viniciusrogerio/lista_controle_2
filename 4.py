'''4. Faca um programa que solicite ao usuário 10 números inteiros e, ao final, informe a 
quantidade de números impares e pares lidos. Calcule também a soma dos números pares e a 
media dos números impares.'''

i=1
qtdpares=0
qtdimpares=0
somapares=0
mediaimpares=0

while(True):
	if i>10:
		break
	num=int(input(f'Digite o {i}° numero: '))
	if num % 2 == 0:
		qtdpares+=1
		somapares+=num
	else:
		qtdimpares+=1
		mediaimpares+=num
	i+=1
mediaimpares=mediaimpares/qtdimpares
print(f'Quantidade de numeros pares: {qtdpares}')
print(f'Quantidade de numeros impares: {qtdimpares}')
print(f'Soma dos pares: {somapares}')
print(f'Media dos impares: {mediaimpares}')