print('=' * 50)
print('AVALIADOR DE MÉDIA'.center(50, '-'))
print('=' * 50)

# Recebendo os valores e calculando a média

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))

media = (nota1 + nota2) / 2

print(f'A média do aluno é: {media}')

# Mensagem de acordo com cada resposta

if 0 <= media < 5:
	print('O aluno está reprovado!')
	
elif 5 <= media < 7:
	print('O aluno está de recuperação!')
	
elif 6.5 < media <= 10:
	print('O aluno foi aprovado!')

else:
	print('Nota inválida!')