def aumentar(num, porcentagem, form_moeda: bool = False):
    """
    -> Calcula o valor acrescido de uma determinada porcentagem
    :param num: numero que será acrescido da porcentagem
    :param porcentagem: valor da porcentagem a ser calculada
    :param form_moeda: (opcional) formata o valor para tipo moeda
    :return: o resultado do cálculo
    """
    resultado = num + (num * (porcentagem / 100))
    if form_moeda:
        return formatacao(resultado)

    else:
        return resultado


def diminuir(num, porcentagem, form_moeda: bool = False):
    """
    -> Calcula o valor reduzido de uma determinada porcentagem
    :param num: numero que será acrescido da porcentagem
    :param porcentagem: valor da porcentagem a ser calculada
    :param form_moeda: (opcional) formata o valor para tipo moeda
    :return: o resultado do cálculo
    """
    resultado = num - (num * (porcentagem / 100))
    if form_moeda:
        return formatacao(resultado)

    else:
        return resultado


def dobro(num, form_moeda: bool = False):
    """
    -> Calcula o dobro de um determinado número
    :param num: número alvo da multiplicação por 2
    :param form_moeda: (opcional) formata o valor para tipo moeda
    :return: o resultado
    """
    resultado = num * 2
    if form_moeda:
        return formatacao(resultado)

    else:
        return resultado


def metade(num, form_moeda: bool = False):
    """
    -> Calcula a metade de um determinado número
    :param num: número alvo da divisão por 2
    :param form_moeda: (opcional) formata o valor para tipo moeda
    :return: o resultado
    """
    resultado = num / 2
    if form_moeda:
        return formatacao(resultado)

    else:
        return resultado
    

def formatacao(num: float, moeda: str = 'R$'):
    string_num = f'{moeda}{num:.2f}'.replace('.', ',')
    return string_num
