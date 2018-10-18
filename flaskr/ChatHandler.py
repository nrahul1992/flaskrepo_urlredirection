import nltk

from langdetect import detect
from nltk.corpus import stopwords
from random import randint


def parentController(usertext):
    tokens = parseText(usertext)


def parseText(usertext):
    tokens = [t for t in usertext.split()]
    print("python tokens are ---- ", tokens)

    clean_tokens = tokens[:]
    sr = stopwords.words('english')
    for token in tokens:
        if token in sr:
            clean_tokens.remove(token)
    print("clean tokens are ---- ", clean_tokens)
    freq = nltk.FreqDist(clean_tokens)
    print("frequency is ---- ", freq)
    for key, val in freq.items():
        print(str(key) + ':' + str(val))


def sayHi():
    greetings = ["Hello!", "It’s nice to meet you.", "Hi!", "Hi, How are things with you?", "What’s new?", "It’s good to see you.", "Good day", "Howdy!", "Hey", "What’s up?", "How’s it going?", "What’s happenin’?", "What’s happening"]
    randomnumber = randint(0, len(greetings) - 1)
    greet = greetings[randomnumber]
    return greet

