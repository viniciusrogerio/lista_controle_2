'''5. Dados n e dois números inteiros positivos i e j diferentes de 0, faça uma função para imprimir 
em ordem crescente os primeiros naturais até n que são múltiplos de i ou de j e não de ambos
simultaneamente.  '''

def imprime(n,i,j):
	k = 1
	while(k<=n):
		if (k % j == 0 or k % i == 0) and not (k % j == 0 and k% i ==0):
			print(k,end=' ')
		k+=1
		
imprime(20,2,3)
		