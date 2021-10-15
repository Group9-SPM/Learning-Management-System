from employeeClass import Employee
from courseClass import Course
#from  import Class


class Administrator:

    def __init__(self,employeeName =  Employee.employeeName, RoleType = Employee.RoleType ):
        self.__employeeName = employeeName
        self.__RoleType = RoleType
        #self.__classID = classID


    def getAllLearners(self, employeeName , RoleType):
        if RoleType == 'L': 
            return self.__employeeName

    def getAllTrainers(self,employeeName,RoleType):
        if RoleType == 'T': 
            return self.__employeeName

    def getAllClasses(self,classes):
        return self.__classes
        #i think i need do for loop here ; ) will do when theres class py 

    def assignLearners(self, employName, Role, CourseID):
        return self.__employeeName
        #self._courses.append(CourseID)
        #urm im not sure where i should add the learners if i follow our class diagram 