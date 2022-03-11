###
# Neil Lukowski
# 5/7/2019
# Final
###

import bank_account_class

class Person:
    
    def __init__(self, acc_id, name, account):
        self.acc_id = acc_id
        self.name = name
        self.account = account
    
    def get_acc_id(self):
        
        return self.acc_id
        
    def get_name(self):
        
        return self.name
    
    def set_name(self, name):
        
        self.name = name
    
    def find_account_balance(self):
        
        bal = self.account.get_bal()
        
        return bal

def test_person():
    
    acc1 = bank_account_class.BankAccount(1234, 100)
    customer1 = Person(1234, "Jill Smith", acc1)
    
    print(customer1.get_acc_id())
    print(customer1.get_name())
    print(customer1.find_account_balance())
    customer1.set_name("Hannah Jones")
    print(customer1.get_name())
    
    
test_person()