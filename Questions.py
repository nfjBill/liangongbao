import json


class Questions:
    def __init__(self, filename='answers.json') -> None:
        self.filename = filename
        self.answersDict = {}
        self.initAnswers()

    def initAnswers(self):
        with open(self.filename, encoding='utf-8', mode='r') as f:
            res = json.load(f)
        for i in res:
            self.answersDict[i['content']] = i['rightOptions']

    def getAnswer(self, question):
        answer = None
        if question in self.answersDict:
            answer = self.answersDict[question]
        return answer

