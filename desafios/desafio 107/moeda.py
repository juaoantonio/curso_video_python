def aumentar(num, porcentagem):
    """
    -> Calcula o valor acrescido de uma determinada porcentagem
    :param num: numero que será acrescido da porcentagem
    :param porcentagem: valor da porcentagem a ser calculada
    :return: o resultado do cálculo
    """
    resultado = num + (num * (porcentagem / 100))
    return resultado


def diminuir(num, porcentagem):
    """
    -> Calcula o valor reduzido de uma determinada porcentagem
    :param num: numero que será acrescido da porcentagem
    :param porcentagem: valor da porcentagem a ser calculada
    :return: o resultado do cálculo
    """
    resultado = num - (num * (porcentagem / 100))
    return resultado


def dobro(num):
    """
    -> Calcula o dobro de um determinado número
    :param num: número alvo da multiplicação por 2
    :return: o resultado
    """
    resultado = num * 2
    return resultado


def metade(num):
    """
    -> Calcula a metade de um determinado número
    :param num: número alvo da divisão por 2
    :return: o resultado
    """
    resultado = num / 2
    return resultado
