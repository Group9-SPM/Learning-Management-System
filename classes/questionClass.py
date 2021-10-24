from quizClass import Quiz

class Question():
     
    def __init__(self, quizNo, quizQuestion, quizOption,quizAnswer):
        self.__quizNo = quizNo
        self.__quizQuestion = quizQuestion
        self.__quizOption = quizOption
        self.__quizAnswer = quizAnswer

    def getQuizNo(self):
        return self.__quizNo
    def getQuizQuestions(self):
        return self.__quizQuestion
    def getQuizOption(self):
        return self.__quizOption
    def getQuizAnswers(self):
        return self.__quizAnswer

    def getQuizID():
        return Quiz.getQuizID()