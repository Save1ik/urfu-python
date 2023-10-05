def count_gl_and_sogl(string):
    gl = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    gl_count = 0
    sogl_count = 0

    for char in string.lower():
        if char.isalpha() and char != ' ':
            if char in gl:
                gl_count += 1
            else:
                sogl_count += 1

    return gl_count, sogl_count

input_string = input("Введите строку: ")
gl, sogl = count_gl_and_sogl(input_string)
print(f"Количество гласных: {gl}", f"Количество согласных: {sogl}")
