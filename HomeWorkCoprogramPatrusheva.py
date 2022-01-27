import requests
import re


def get_words():
    words = requests.get("https://raw.githubusercontent.com/ranjith19/random-quotes-generator/master/quotes.txt").text
    word_list = re.sub("[^\w]", " ", words).split()
    return word_list


words = get_words()


entered_word = input('Enter any english word: ')
if entered_word in words:
    print(next(word for word in words if word[0] == entered_word[-1]))
else:
    print('No such word')


# if entered_word in get_words():
#     for current_word in filter(lambda a: entered_word[-1] == a[0], get_words()):
#         print(current_word)
#         break
# else:
#     print("StopIteration")
#








