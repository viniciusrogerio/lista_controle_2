'''1. A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o
salario e numero de filhos. Faça um programa que leia o salario e o numero de filhos de n
habitantes. O final da leitura de dados se dará com a entrada de um salario negativo. Mostre na 
saída:
a. media de salario da população;
b. media de numero de filhos;
c. maior salario;
d. percentual de pessoas com salario mínimo'''

i=1
sal=999
mediasal=0
mediafilhos=0
maiorsal=0
pessoas_salmin=0

while sal!=-1:
	sal=int(input(f'Digite o salario do habitante {i}: '))
	if sal==-1:
		break
	else:
		mediasal+=sal
		if sal>=maiorsal:
			maiorsal=sal
		if sal>=1000:
			pessoas_salmin+=1
		numfilhos=int(input('digite o num de filhos: '))
		mediafilhos+=numfilhos
	i+=1

i-=1
print(habit)
print()
print(f'maior salario: {maiorsal}')
print(f'media salarios: {mediasal/i}')
print(f'media filhos: {mediafilhos/i}')
print(f'perc pessoas sal min: {pessoas_salmin/i*100}%')