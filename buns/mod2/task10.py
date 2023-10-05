def new_nigga(words):
    to_word = ""
    for word in words:
            if len(word) > 0:
                to_word += word[-1]
    return to_word

words = map(str, input().split(' '))
result = new_nigga(words)
print(result)
