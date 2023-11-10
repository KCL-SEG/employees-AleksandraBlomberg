"""Employee pay calculator."""

class Employee:
    def __init__(self):
        self.name = ""
        self.contract = False
        self.hours = 0
        self.salary = 0
        self.hourlyRate = 0
        self.pay = 0
        self.commission = False
        self.bonusCommission = False
        self.commissionNum = 0
        self.commissionPay = 0
        self.payMethod = f"^"

    def set_name(self,name):
        self.name = name
        self.payMethod = self.payMethod + f"{self.name}"

    def set_contract(self, contract):
        self.contract = contract

    def set_hours(self,hours):
        self.hours = hours
        
    def set_salary(self,salary):
        self.salary = salary

    def set_hourlyRate(self,rate):
        self.hourlyRate = rate

    def set_commission(self,commission):
        self.commission = commission

    def set_bonusCommission(self,commission):
        self.bonusCommission = commission

    def set_commissionNum(self,num):
        self.commissionNum = num

    def set_commissionPay(self,pay):
        self.commissionPay = pay
    
    def commission_payout(self):
        if self.bonusCommission == True:
            self.payMethod = self.payMethod +f" and recives a bonus commission of {self.commissionPay}"
            return self.commissionPay
        if self.commission == False:
            return 0
        else:
            self.payMethod = self.payMethod +f" and recives a commission for {self.commissionNum} contracts at {self.commissionPay}/constract"
            return self.commissionNum*self.commissionPay

    def get_pay(self):
        if self.contract == False:
            self.pay = self.pay + self.salary
            self.payMethod = self.payMethod + f" works on a monthly salary of {self.salary}"
            self.pay = self.pay + self.commission_payout()
        else:
            self.pay = self.hours*self.hourlyRate
            self.payMethod = self.payMethod +f" works on a contract of {self.hours} hours at {self.hourlyRate}/hour"
        self.payMethod= self.payMethod + f".\\s+Their totoal pay is {self.pay}.$"
        return self.pay;
        
    def __str__(self):
        self.get_pay()
        return self.payMethod


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee()
billie.set_name("Billie")
billie.set_salary(4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee()
charlie.set_name("Charlie")
charlie.set_contract(True)
charlie.set_hours(100)
charlie.set_hourlyRate(25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee()
renee.set_name("Renne")
renee.set_salary(3000)
renee.set_commission(True)
renee.set_commissionNum(4)
renee.set_commissionPay(200)
