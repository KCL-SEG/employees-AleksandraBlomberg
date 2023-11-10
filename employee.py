"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
class Employee:
        def __init__(self, name):
            self.name = name
            self.pay = 0
            self.salary = 0
            self.hourly_rate = 0
            self.commission = 0
            self.numOfContracts = 0

        def set_salary(self, num):
            self.salary = num
            
        def set_hourly_rate(self, num):
            self.hourly_rate = num
            
        def set_hours_worked(self, num):
            self.hours_worked = num
            
        def set_commission(self, num):
            self.commission = num
            
        def set_num_contracts(self, num):
            self.numOfContracts = num

        def get_pay(self):
            if (self.salary > 0):
                self.pay = self.pay + self.salary
            elif (self.hourly_rate > 0 and self.hours_worked > 0):
                self.pay = self.pay + (self.hourly_rate * self.hours_worked)

            if (self.commission > 0 and self.numOfContracts == 0):
                self.pay = self.pay + self.commission
            elif (self.commission > 0 and self.numOfContracts > 0):
                self.pay = self.pay + (self.commission * self.numOfContracts)
            return self.pay

        def __str__(self):
            payment_string = self.name  
            if self.salary > 0:
                payment_string += f' works on a monthly salary of {self.salary}'
            elif self.hourly_rate > 0 and self.hours_worked > 0:
                payment_string += f' works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour'

            if self.commission > 0 and self.numOfContracts == 0:
                payment_string += f' and receives a bonus commission of {self.commission}'
            elif self.commission > 0 and self.numOfContracts > 0:
                payment_string += f' and receives a commission for {self.numOfContracts} contract(s) at {self.commission}/contract'

            payment_string += f'. Their total pay is {self.pay}.'  

            return payment_string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.set_salary(4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.set_hours_worked(100)
charlie.set_hourly_rate(25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.set_salary(3000)
renee.set_num_contracts(4)
renee.set_commission(200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.set_hours_worked(150)
jan.set_hourly_rate(25)
jan.set_num_contracts(3)
jan.set_commission(220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.set_salary(2000)
robbie.set_commission(1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.set_hours_worked(120)
ariel.set_hourly_rate(30)
ariel.set_commission(600)
