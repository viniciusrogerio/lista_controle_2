'''9. Faça uma função que dado um texto retorne um dicionário (ou outra estrutura de dados) com 
cada palavra encontrada no texto e sua quantidade.'''

def contapalavras(texto):
	a=list(set('[~!@#`°=£¢€¥,<>÷×^¶©®™$.-/?%^&*()_+{}":;\']+$').intersection(texto))
	for char in texto:
		if char in a:
			texto=texto.replace(char,' ')
	texto=texto.lower()
	texto=texto.split(' ')
	dic={}
	for palavra in texto:
		if palavra in dic:
			dic[palavra]+=1
		else:
			dic[palavra]=1
	return dic
