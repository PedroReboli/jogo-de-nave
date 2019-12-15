import sys
import time
def criarjogo(x,y):
	#adicona 1 para nao bugar
	x += 1
	finalx = "0,"*x
	#multiplica as linhas pelas colunas
	final = finalx*y
	#remove o "," que fica no final
	final = final[:-1]
	exec("final = ["+final+"]")
	#adiciona o personagem
	final[1] = 1
	return final
	
	
#orda pode ter a extensao maior
ordaa = [2,0,0,0,2,0,2,0,2,
		 0,0,2,0,0,0,0,0,0,
		 2,0,2,0,2,0,2,0,0,
		 2,0,2,0,0,0,2,2,0,0]



base = [0,0,1,0,0,0,0,0,2,
		0,0,0,0,0,0,0,0,0,
		0,0,0,0,0,0,0,0,0,
		0,0,0,0,0,0,0,2,0,0]
		
x = 9
y = 4
linhasx =x
base = criarjogo(x,y)

help = """
[t] efetua tiro
[w] sobe o personagem
[s] desce o personagem
"""

def GPU(base):
	saida = "\n" * 40
	for x in range(0,len(base)):
		#  Substitui os valores por algo que de para entender
		h = str(base[x]).replace("0"," ").replace("1",">").replace("2","*").replace("4","-").replace("5","*").replace("6","()")
		if x % linhasx:
			saida += str(h)
						
		else:
			saida += str(h)
			saida += "\n"
	
	sys.stdout.write(saida)
	sys.stdout.flush()
def s(base,x):
	#scaneia a area do jogo para procurar o jogador
	while x < len(base):
		if base[x] == 1:
			#adiciona 9 para a area do jogo 
			#9 e a largura da tela
			base[x + 9] = 1
			#apaga o antigo personagem
			base[x] = 0
			return base
		x +=1


def w(base,x):
	#scaneia a area do jogo para procurar o jogador
	while x < len(base):
		if base[x] == 1:
			#diminue por 9 e adicona 1
			base[x - 9] = 1
			#apaga o antigo personagem
			base[x] = 0
			firt = True
			return base
		x +=1
		
def fren(base,x):
	#nao utilizado 
	#coloca o personagem para frente
	while x < len(base):
		if base[x] == 1:
			base[x + 1] = 1
			base[x] = 0
			firt = True
			for x in range(0,len(base)):
				if x % linhasx:
					sys.stdout.write(str(base[x]))
						
				else:
					sys.stdout.write(str(base[x]))
					sys.stdout.write("\n")
			
			
			
		x +=1
	return base
def tick(base,t,ordaa):
	x = 0
	while x < len(base):
		#deveria apagar a explosao
		if base[x] == 6:
			base[x] == 0
		#coloca os inimigos 1 casa a frente
		if base[x] == 2:
			h = x - 1
			if h % linhasx:
				#se uma casa a frente do inimigo for o personagem ele manda a base para ser processada e encerra o jogo
				if base[h] == 1:
					base[x - 1] = 2
					base[x] = 0
					GPU(base)
					exit()
				else:
				#detecta se o inimigo colidiu com o tiro (precisa de ajutes)
					if base[h-1] == 4:
						# cria explosao
						base[x] = 6
						# apaga o tiro
						base[h-1] = 0
					else:
						#move o inimigo para frente
						base[x - 1] = 2
						base[x] = 0
					
			else:
				#se o inimigo estiver no inicio apaga o inimigo
				base [x] = 0

		#move o tiro para frente
		if base[x] == 4:
			#detecta se a proxima casa e um inimigo
			if base[x+1] == 2:
				# cria explosao
				base[x] = 6
				#apaga o tiro
				base[x + 1] = 0
				#pula duas casas pois seria tiro + inimigo caso for 1 o tiro fica instantaneo
				x += 2
			else:
				#move o tiro para frente
				base[x + 1] = 4
				#apaga o tiro anterior
				base[x] = 0
				#move duas casas pois seria tiro antigo + tiro novo
				x += 2
		x +=1
		
		

	x = 0				
	#cria uma linha de onda
	#retorna base e a linha que ele esta
	base,g = orda(base,t,ordaa)
	#print base
	GPU(base)
	return base,g
	
def orda(base,h,ordaa):
	#adiciona inimigos nas linhas correspondentes
	# TODO Melhorar isso
	try:
		base[9] = ordaa[h]
		base[18] = ordaa[h+9]
		base[26] = ordaa[h+18]
		base[35] = ordaa[h+27]
	except:
		pass
	h += 1
	if h % 9:
		pass
	else:
		h = 0
	return base,h
	
def t(base,x):
	x = 0
	while x < len(base):
		#procura pelo personagem
		if base[x] == 1:
			#caso o nosso amiginho queira dar dois tiro sem esperar o tiro sair do lugar
			if base[x+1] == 4:
				base[x+2] = 4
			else:
				# apenas adiciona o tiro
				base[x+1] =4
			# retorna base
			return base
		x += 1

x = 0
h = 0
jogada = True
while True:	
	#time.sleep(0.5)
	if jogada == True:
		base,h = tick(base,h,ordaa)
		print help
	
	x = raw_input("mov :")
	jogada = False
	if x != "":
		#jogo nao fechar caso escreva uma letra errada
		try:
			comando = "base = "+x+"(base,0)"
			exec(comando)
			jogada = True
		except:
			jogada = False
	#time.sleep(0.5)
#print("--- %s seconds ---" % (time.time() - start_time))
