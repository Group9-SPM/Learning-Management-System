from courseClass import Course

class Classes: 
    def __init__(self , ClassID , StartDate, EndDate, ClassSize, StartTime, EndTime, maxSlots, minSlots, regStartDate, regEndDate, TrainerID, courseID = Course.CourseID):
        self.__ClassID = ClassID
        self.__StartDate = StartDate
        self.__EndDate = EndDate
        self.__ClassSize = ClassSize
        self.__StartTime = StartTime
        self.__EndTime = EndTime
        self.__maxSlots = maxSlots
        self.__minSlots = minSlots
        self.__regStartDate = regStartDate
        self.__regEndDate = regEndDate
        self.__courseID = courseID
        self.__trainerID = trainerID

    def getClassID(self):
        return self.__ClassID
    
    def getStartDate(self):
        return self.__StartDate

    def getEndDate(self):
        return self.__EndDate

    def getClassSize(self):
        return self.__ClassSize
        
    def getStartTime(self):
        return self.__StartTime

    def getEndTime(self):
        return self.__EndTime
    
    def getmaxSlots(self):
        return self.__maxSlots

    def getminSlots(self):
        return self.__minSlots

    def getregStartDate(self):
        return self.__regStartDate
        
    def getregEndDate(self):
        return self.__regStartDate

    def getCourseID(self):
        return self.__courseID

    def getTrainerID(self):
        return self.__TrainerID




