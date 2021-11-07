frase = str(input('Digite uma frase: ')).lower().strip()

print(f"A letra 'a' aparece {frase.count('a')} vezes")
print(f"A primeira posição em que aparece é no caractere de número {frase.find('a') + 1}")
print(f"A última posição em que aparece é no caractere de número {frase.rfind('a') + 1}")
