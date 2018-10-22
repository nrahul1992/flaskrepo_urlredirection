import nltk
import json
import ast
from langdetect import detect
from nltk.corpus import stopwords
from random import randint


__possibleQuestionList__ = ['where', 'who', 'when', 'what', 'why', 'whose', 'which', 'how']
__possibleAnswerList__ = ['Looks like answer came before the question!', "I asked for the question first, duh!", "What are you answering to?", "Question Please...first!", "It seems an answer was given for a question never asked."]
__possibleGreetingList__ = ["Hello!", "It’s nice to meet you.", "Hi!", "Hi, How are things with you?", "What’s new?", "It’s good to see you.", "Good day", "Howdy!", "Hey", "What’s up?", "How’s it going?", "What’s happenin’?", "What’s happening"]


def parseUsertext(text, db):
    text = str(text).lower()
    question = ''
    answer = ''
    botResponse = ''
    if str(text).startswith("q:") or str(text).startswith("q: "):
        if text.startswith("q:"):
            text = text.split("q:")[1]
            question = text
            print("question is ----", question)
        if text.startswith("q: "):
            text = text.split("q: ")[1]
            question = text
            print("question is ----", question)
        botResponse = createBuffer(question, db)

    if str(text).startswith("a:") or str(text).startswith("a: "):
        if text.startswith("a:"):
            text = text.split("a:")[1]
            answer = text
            print("answer is ----", answer)
        if text.startswith("a: "):
            text = text.split("a: ")[1]
            answer = text
            print("answer is ----", answer)
        botResponse = updateBuffer(answer, db)
    print("bot response is ---- ", botResponse)
    if botResponse != '':
        return botResponse
    else:
        return "Something Went Wrong! Connect with the bot admin."


def createBuffer(text, db):
    questionCount = -1
    try:
        bufferData = db.bufferdata.find_one({"qflag": 1})
        if bufferData is not None:
            questionCount = -1
        else:
            questionCount = 0
        print('question count is ----', questionCount)
    except Exception as e:
        print("Error reading db ----", e)
    if questionCount == 0 and text != '':
        insertBuffer = dict()
        insertBuffer['qflag'] = 1
        insertBuffer['question'] = text
        insertBuffer['answer'] = ''
        try:
            db.bufferdata.insert_one(insertBuffer)
            print("question added. Answer pending!")
        except Exception as e:
            print("Error occurred during buffer creation ----", e)
        return "Question Noted."
    else:
        return "There appears to be an unanswered question. Please answer the same. "


def updateBuffer(text, db):
    bufferData = db.bufferdata.find_one({"qflag": 1})
    if bufferData is not None:
        questionCount = 1
    else:
        questionCount = 0
    print('question count is ----', questionCount)
    if questionCount == 1 and text != '':
        question = db.bufferdata.find_one({"qflag": 1})
        trainingQuery = dict()
        trainingQuery['tag'] = fetchTag(question['question'])
        trainingQuery['query'] = question['question']
        trainingQuery['response'] = text
        try:
            db.bottrainingdata.insert_one(trainingQuery)
            print('training data recorded! ')
            db.bufferdata.delete_one({"qflag": 1})
            print("buffer cleared")
        except Exception as e:
            print('error occurred while inserting training data')

        return 'Answer Noted.'
    else:
        return 'There appears to be no pending question. Please give a question first.'


def fetchTag(question):
    qMatch = gMatch = sMatch = 0
    userTextTokens = [t for t in question.split()]
    print("user question tokens are ---- ", userTextTokens)
    for token in userTextTokens:
        print("token is ---- ", token)
        for qtoken in __possibleQuestionList__:
            print("qtoken is ---- ", qtoken)
            qt = [q for q in qtoken.split()]
            print("question token qt is ---- ", qt)
            if token in qt:
                print('match found for question...')
                qMatch += 1
                print('qmatch value is ----', qMatch)
        for gtoken in __possibleGreetingList__:
            print("gtoken is ----", gtoken)
            gt = [g for g in gtoken.split()]
            if token in gt:
                print('match found for greeting...')
                gMatch += 1
                print('gmatch value is ----', gMatch)
    print('final qmatch value is----', qMatch)
    print('final gmatch value is----', gMatch)
    if qMatch > gMatch:
        tag = "question"
    elif gMatch > qMatch:
        tag = "greeting"
    else:
        tag = "statement"

    print('tag assigned is ----', tag)
    return tag





