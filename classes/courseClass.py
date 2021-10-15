class Course: 
    def __init__(self , CourseID , CourseName, CourseDesc, CourseDuration, PreReqCourses):
        self.__CourseID = CourseID
        self.__CourseName = CourseName
        self.__CourseDesc = CourseDesc
        self.__CourseDuration = CourseDuration
        self.__PreReqCourses = PreReqCourses

    def getCourseID(self):
        return self.__CourseID
    
    def getCourseName(self):
        return self.__CourseName

    def getCourseDesc(self):
        return self.__CourseDesc

    def getCourseDuration(self):
        return self.__CourseDuration
        
    def getPreReqCourses(self):
        return self.__PreReqCourses

