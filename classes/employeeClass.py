class Employee: 
    def __init__(self , employeeName , Department, Username, Role):
        self.__employeeName = employeeName
        self.__Department = Department
        self.__Username = Username
        self.__Role = Role 

    def getName(self, employeeName):
        return self.__employeeName

    def getDepartment(self, Department):
        return self.__Department

    def getRole(self, Role):
        return self.__Role

    def getUsername(self,Username):
        return self.__Username

