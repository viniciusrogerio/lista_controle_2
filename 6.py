'''6. Escreva uma função que dada uma matriz nxn de inteiros, encontre a frequência de cada 
inteiro na matriz.'''

def freq(a):
	for row in a:
		for i in row:
			f=sum(x.count(i) for x in a)
			print(f'Frequencia de {i}: {f}')