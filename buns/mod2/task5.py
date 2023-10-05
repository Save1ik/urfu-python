def shift_alphabet(i, n):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    index = alphabet.index(i)
    shifted_index = (index + n) % len(alphabet)
    shifted_char = alphabet[shifted_index]
    return shifted_char


char = input("Введите символ латинского алфавита: ")
num = int(input("Введите целое число: "))

shifted_char = shift_alphabet(char, num)
print(f"Смещенный символ: {shifted_char}")
