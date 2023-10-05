def check_barcode(barcode):
    odd_sum = 0
    even_sum = 0

    for i in range(0, len(barcode), 2):
        odd_sum += int(barcode[i])

    for i in range(1, len(barcode), 2):
        even_sum += 3 * int(barcode[i])
    
    total_sum = odd_sum + even_sum

    if total_sum % 10 == 0:
        return "yes"
    else:
        return "no"

input_barcode = input("Введите штрих-код: ")
result = check_barcode(input_barcode)
print(result)
