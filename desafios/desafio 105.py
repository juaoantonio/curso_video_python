def notas_alunos(*n, sit=False):
    """
    -> Função que analisa notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos (aceita mais de um parâmetro)
    :param sit: (opcional) indica se deve ou não adicionar a situação da turma
    :return: um dicionário com o menor e maior valores informados, a média da notas e a situação da turma
    """
    dados = {}
    notas = []
    for nota in n:
        notas.append(nota)

    dados['total'] = len(notas)
    dados['maior'] = max(notas)
    dados['menor'] = min(notas)
    dados['media'] = sum(notas) / len(notas)

    if sit:
        if 0 <= dados['media'] < 5:
            dados['situação'] = 'RUIM'
        elif 5 <= dados['media'] < 7:
            dados['situação'] = 'RAZOÁVEL'
        elif 7 <= dados['media'] <= 10:
            dados['situação'] = 'BOA'
        else:
            dados['situação'] = 'NOTAS INVÁLIDAS'
    return dados


print(notas_alunos(5, 7.5, 6, 8, 9.9, sit=True))
help(notas_alunos)
