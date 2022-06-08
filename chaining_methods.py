class User:
    def __init__(self,name,balancce):
        self.name = name
        self.balance = balancce
        return None
        
    def make_deposit(self,deposit):
        self.balance += deposit
        return self
    
    def make_withdrawal (self, withdraw):
        if(self.balance> withdraw):
            self.balance -= withdraw
        else:
            print("insufficient balance")
        return self
    
    def display_user_balance(self):
        print (self.name + " current balance is:" + str(self.balance))
        
        return self
    
    def __str__(self):
        print(self.name + "-->" + str(self.balance ))
        
        return self
            
chamith = User("Chamith",500)
Matt = User("Matt",4750)
Jason = User("Jason",7500)

userList = [chamith,Matt,Jason] 

chamith.make_deposit(500).make_deposit(700).make_deposit(172).make_withdrawal(574).display_user_balance()

Matt.make_deposit(871).make_deposit(285).make_withdrawal(592).display_user_balance()

Jason.make_deposit(5872).make_withdrawal(672).make_withdrawal(1500).make_withdrawal(2200).display_user_balance()


