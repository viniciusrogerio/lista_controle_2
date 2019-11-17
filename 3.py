'''3. Faça uma função que dados dois número retorna o mínimo múltiplo comum (MMC)'''
def mmc(a,b):
	maior = max(a,b)
	while True:
	    if maior % a == 0 and maior % b == 0:
	        return maior
	    else:
	        maior += 1

		