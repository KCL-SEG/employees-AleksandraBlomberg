"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, hours, hourlyRate, salary, commission, bonusCommission, commissionNum, commissionPay):
        self.name = name
        self.contract = contract
        self.hours = hours
        self.salary = salary
        self.hourlyRate = hourlyRate
        self.pay = 0
        self.commission = commission
        self.bonusCommission = bonusCommission
        self.commissionNum = commissionNum
        self.commissionPay = commissionPay
        self.payMethod = f"{self.name}"

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
        self.payMethod= self.payMethod + f". Their totoal pay is {self.pay}"

    def __str__(self):
        self.get_pay()
        return self.payMethod


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
