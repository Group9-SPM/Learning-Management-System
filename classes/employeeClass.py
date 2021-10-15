class Employee: 
    def __init__(self ,empID, employeeName , Department, Username, RoleType):
        self.__empID = empID
        self.__employeeName = employeeName
        self.__Department = Department
        self.__Username = Username
        self.__RoleType = RoleType 

    def getEmpID(self, empID):
        return self.__empID
    
    def getName(self, employeeName):
        return self.__employeeName

    def getDepartment(self, Department):
        return self.__Department

    def getRoleType(self, RoleType):
        return self.__RoleType

    def getUsername(self,Username):
        return self.__Username

