def valor_da_multa (velocidade_do_carro , velocidade_limite, taxa_sobre_velocidade):
	valor_multa = (velocidade_do_carro - velocidade_limite ) *taxa_sobre_velocidade
	   
	return valor_multa

velocidade_do_carro = 90
velocidade_limite = 80
taxa_sobre_velocidade = 7

if velocidade_do_carro >velocidade_limite :
	 print("voce foi multado por ultrapassar a velocidade limite da via ")
	 print(f" A multa ficou em {valor_da_multa(velocidade_do_carro,velocidade_limite, taxa_sobre_velocidade)}")
else :
	print(f"Sem multa ")
