class Quiz():
     
    def __init__(self, quizID, quizQuestions, quizAnswers, quizDuration, passingCriteria, quizType, quizOption):
        self.__quizID = quizID
        self.__quizQuestions = quizQuestions
        self.__quizAnswers = quizAnswers
        self.__quizDuration = quizDuration
        self.__passingCriteria = passingCriteria
        self.__quizType = quizType
        self.__quizOption = quizOption
        self.__quizGrade = quizQuestions

    def getQuizID(self):
        return self.__quizID
    def getQuizQuestions(self):
        return self.__quizQuestions
    def getQuizAnswers(self):
        return self.__quizAnswers
    def getQuizDuration(self):
        return self.__quizDuration
    def getPassingCriteria(self):
        return self.__passingCriteria
    def getQuizType(self):
        return self.__quizType
    def getQuizOption(self):
        return self.__quizOption

    def getQuizGrade(self):
        # Each question is worth 1 mark. Compare submitted answers to correct answers.
        return self.__quizGrade