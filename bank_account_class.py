###
# Neil Lukowski
# 5/7/2019
# Final
###

class BankAccount:
    
    def __init__(self, acc_id, bal):
        
        if bal < 0:
            bal = 0
        
        self.acc_id = acc_id
        self.bal = bal
    
    def deposit(self, amt):
        
        if amt > 0:
            self.bal = self.bal + amt
    
    def withdrawal(self, amt):
        
        if amt > 0:
            self.bal = self.bal - amt
    
    def get_bal(self):
        
        return self.bal
        
    def get_acc_id(self):
        
        return self.acc_id
        
    def __eq__(self, other):
        
        out = False
        
        if self.get_acc_id == other.get_acc_id:
            out = True
        elif self.get_bal == other.get_bal:
            out = True
        
        return out

        
def test_bank_account():
    acc1 = BankAccount(1, 200)
    print(acc1.get_bal())
    acc2 = BankAccount(2, 100)
    print(acc2.get_bal())
    
    acc2.deposit(-25)
    acc1.deposit(50)
    print(acc1.get_bal())
    print(acc2.get_bal())
    
    acc1.withdrawal(30)
    acc1.withdrawal(-40)
    print(acc1.get_bal())
    print(acc2.get_bal())
    
    
    print(acc1 is acc2)
    print(acc1 is acc1)
test_bank_account()
