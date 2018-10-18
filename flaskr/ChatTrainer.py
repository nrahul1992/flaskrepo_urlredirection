import nltk
import json
import ast
from langdetect import detect
from nltk.corpus import stopwords
from random import randint


__possibleQuestionList__ = ['where', 'who', 'when', 'what', 'why', 'whose', 'which', 'how']
__possibleAnswerList__ = ['Looks like answer came before the question!', "I asked for the question first, duh!", "What are you answering to?", "Question Please...first!", "It seems an answer was given for a question never asked."]
__possibleGreetingList__ = ["Hello!", "It’s nice to meet you.", "Hi!", "Hi, How are things with you?", "What’s new?", "It’s good to see you.", "Good day", "Howdy!", "Hey", "What’s up?", "How’s it going?", "What’s happenin’?", "What’s happening"]
# __bufferFilePath__ = 'C:\Users\\nourahul\\Desktop\\Rahul\'s folder\\git-repos\\f\\flaskr\static\\buffer\questionBuffer.txt'
__bufferFilePath__ = '‪C:\\Users\\nourahul\\Desktop\\questionBuffer.txt'


def parseUsertext(text):
    text = str(text).lower()
    question = ''
    answer = ''
    if str(text).startswith("q:") or str(text).startswith("q: "):
        if text.startswith("q:"):
            text = text.split("q:")[1]
            question = text
            print("question is ----", question)
        if text.startswith("q: "):
            text = text.split("q: ")[1]
            question = text
            print("question is ----", question)

    if str(text).startswith("a:") or str(text).startswith("a: "):
        if text.startswith("a:"):
            text = text.split("a:")[1]
            answer = text
            print("answer is ----", answer)
        if text.startswith("a: "):
            text = text.split("a: ")[1]
            answer = text
            print("answer is ----", answer)
    createQuery = dict()
    tag = fetchTag(question)
    readBuffer = createBuffer(question, answer)
    if readBuffer is not None:
        createQuery['tag'] = tag
        createQuery['buffer'] = readBuffer
        print("create query is ---- ", createQuery)
        return "Understood!"
    else:
        return "continue please!"


def createBuffer(question, answer):
    print("Creating buffer...")
    insertquery = dict()
    if question != '' and answer == '':
        print("Processing question...", question)
        questDict = {'qflag': 1, 'question': question}
        try:
            with open(__bufferFilePath__, 'r+', encoding='utf-8') as file:
                content = file.read()
                if content is not None or content != '':
                    whip = ast.literal_eval(content)
                    print("whip is ----", whip)
                    print( "Previous question: \"" + whip['question'] + "\" is not answered. Please answer the same to move further.")
                else:
                    file.write(json.dumps(questDict))
                    file.close()
                    print("Question taken. Waiting for the answer...")
        except Exception as e:
            print('Error occurred while opening the file. Full stack trace ---- ', e)
        return insertquery
    elif question == '' and answer != '':
        print("Processing answer...")
        questDict = {'qflag': 0, 'question': question}
        with open(__bufferFilePath__, 'r+', encoding='utf-8') as file1:
            text = file1.read()
            if text is None or text == '':
                print(__possibleAnswerList__[randint(0, len(__possibleAnswerList__) - 1)])
            else:
                whip = ast.literal_eval(text)
                iQuestion = whip['question']
                iAnswer = answer
                insertquery['query'] = iQuestion
                insertquery['response'] = iAnswer
                file1.truncate(0)
                file1.write(json.dumps(questDict))
                print("Answer Noted")
        return insertquery


def fetchTag(question):
    userTextTokens = [t for t in question.split()]
    qMatch = gMatch = sMatch = 0
    print("user question tokens are ---- ", userTextTokens)
    for token in userTextTokens:
        for qtoken in __possibleQuestionList__:
            qt = [q for q in qtoken.split()]
            if token in qt:
                qMatch += 1
        for gtoken in __possibleGreetingList__:
            gt = [g for g in gtoken.split()]
            if token in gt:
                gMatch += 1
    if qMatch > gMatch:
        tag = "question"
    elif gMatch > qMatch:
        tag = "greeting"
    else:
        tag = "statement"
    return tag




