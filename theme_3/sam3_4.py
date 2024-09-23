sentence = input("Введите предложение: ")

print("Длина предложения:", len(sentence))

lower_sentence = sentence.lower()
print("В нижнем регистре:", lower_sentence)

vowels_count = sum(1 for char in lower_sentence if char in "aeiou")
print("Количество гласных:", vowels_count)

replaced_sentence = sentence.replace("ugly", "beauty")
print("После замены 'ugly' на 'beauty':", replaced_sentence)

starts_with_the = sentence.startswith("The")
ends_with_end = sentence.endswith("end")
print("Начинается с 'The':", starts_with_the)
print("Заканчивается на 'end':", ends_with_end)
