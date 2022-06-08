class User:
    def __init__(self,name,balancce):
        self.name = name
        self.balance = balancce
        
    def make_deposit(self,deposit):
        self.balance += deposit
    
    def make_withdrawal (self, withdraw):
        if(self.balance> withdraw):
            self.balance -= withdraw
        else:
            print("insufficient balance")
    
    def display_user_balance(self):
        print (self.name + " current balance is:" + str(self.balance))
    
    def __str__(self):
        print(self.name + "-->" + self.balance )
        
            
user1 = User("Chamith",500)
user2 = User("Matt",4750)
user3 = User("Jason",7500)

userList = [user1, user2, user3] 

user1.make_deposit(500)
user1.make_deposit(700)
user1.make_deposit(172)
user1.make_withdrawal(574)

user2.make_deposit(871)
user2.make_deposit(285)
user2.make_withdrawal(592)

user3.make_deposit(5872)
user3.make_withdrawal(672)
user3.make_withdrawal(1500)
user3.make_withdrawal(2200)


