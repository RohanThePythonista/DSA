class EMPLOYEE:
    def __init__(self, ID, Name):
        self.ID = ID
        self.EmployeeName = Name


class Sale_EMPLOYEE(EMPLOYEE):
    fix_commission = 1000

    def __init__(self, id, EmployeeName, salary):
        EMPLOYEE.__init__(self,id, EmployeeName)
        self.salary = salary

    def CalculatePayroll(self):
        return self.salary + self.fix_commission

    def WORK(self, hours):
        d = 5
        TotalHoursWorked = 0
        while (d > 0):
            TotalHoursWorked =  TotalHoursWorked + hours
        print("%s worked %s hours " % (self.ID, TotalHoursWorked))