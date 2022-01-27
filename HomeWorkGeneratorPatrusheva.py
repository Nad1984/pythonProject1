#Функція - генератор
import requests
import random
import re


def select_word():
    words = requests.get("https://raw.githubusercontent.com/ranjith19/random-quotes-generator/master/quotes.txt").text
    word_list = re.sub("[^\w]", " ", words).split()
    len_word_list = len(word_list)
    current_word = word_list[random.randint(0, len_word_list)].replace("\n", "<br>")
    print(current_word)

    for word in word_list:
        if current_word[-1] == word[0]:
            current_word = word
            yield current_word


iterator = select_word()
for _ in range(20):
    print(iterator.__next__())


#Співпрограма
