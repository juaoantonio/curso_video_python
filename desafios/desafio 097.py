def escreva(msg):
    print('~' * (len(msg) + 4))
    print(str(msg).upper().center(len(msg) + 4))
    print('~' * (len(msg) + 4))


escreva('Olá, Mundo!')
escreva('Coé')
escreva('Paralelepípedo')