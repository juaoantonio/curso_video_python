def escreva(msg, espacamento=0):
    if espacamento == 0:
        print('~' * (len(msg) + 4))
        print(str(msg).upper().center(len(msg) + 4))
        print('~' * (len(msg) + 4))

    else:
        print('~' * (espacamento))
        print(str(msg).upper().center(espacamento))
        print('~' * (espacamento))
