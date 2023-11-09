text = input("Введите текст: ")
text = text.lower()

punctuation = [".", ",", "!", "?"]

for i in punctuation:
    while i in text:
       text = text.replace(i, "")

words = text.split()

word_frequency = dict()

for word in words:
    if word not in word_frequency.keys():
        word_frequency[word] = 1
    else:
        word_frequency[word] += 1

num_of_words = set(words)
print(f"Количество разных слов: {len(num_of_words)}")

print("Частота слов:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")