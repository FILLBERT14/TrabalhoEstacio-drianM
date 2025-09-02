saida = ''
def adicao(valor_adicao1, valor_adicao2):
	 return valor_adicao1 + valor_adicao2

def subtracao(valor_subtracao1, valor_subtracao2) :
  return  valor_subtracao1 - valor_subtracao2

def multiplicacao(valor_multiplicacao1, valor_multiplicacao2):
  return valor_multiplicacao1 * valor_multiplicacao2 

def divisao(valor_divisao1 , valor_divisao2):
	  if valor_divisao1 == 0:
	     print("Não foi possivel dividir por 0")
	  elif valor_divisao2 ==0:
	  	  print("Não foi possivel dividir por 0")
	  else:
	  		  return valor_divisao1 / valor_divisao2

def calculadora(numero1 , numero2 , operador):
	  if operador == "+":
	    resultado = adicao(numero1 , numero2)  
	    
	  elif operador == "-":
	    resultado = subtracao(numero1,numero2)
	    
	  elif operador == "*":
	    resultado = multiplicacao(numero1,numero2)
	    
	  elif operador == "/":
	    resultado = divisao(numero1 , numero2)
	  return resultado
	  
while saida != 'n':	  
	 num1 = int(input("digite um numero \n"))
	 operador =(input("escolha o operador \n"))
	 num2 = int(input("digite um numero \n"))
	  
	 resultado = calculadora(num1 , num2 , operador)
	 print('Resultado da operação :' ,resultado)
	 saida = input("Voce deseja continuar a esxecução do programa? se Sim digite 's', caso não digite 'n' \n")
print("programa Encerrado")	 
	  
