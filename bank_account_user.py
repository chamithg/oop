
# bank Account class
class BankAccount:
    Account_name = "Python Bank"
    
    def __init__(self, account_name, balance, int_rate): 
        self.account_name = account_name
        self.balance = balance   
        self.int_rate= int_rate
        return None 
        
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdrawal(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("insufficient funds.")
        return self
    def account_info(self):
        print( str(self.account_name) +"Balance--> $"+ str(self.balance))
        return self
        
    def yield_interest(self):
        self.balance += self.balance* self.int_rate /100 
        return self
    
    def __str__ (self):
        return "," + str(self.account_name) + ", Balance: $" + str(self.balance)+ ", Interest Rate: " + str(self.int_rate) + "%" 
        
#!bank account class ends

# user Class
class User:
    def __init__(self,name,account_name, balance):
        self.name = name
        self.account = BankAccount(account_name,balance, int_rate = 1.5)
        return None 
        
    def make_deposit(self,dep_amount):
        self.account.deposit(dep_amount)
        return self
    
    def make_withdrawal (self, wd_amount):
        if(self.account.balance > wd_amount):
            self.account.withdrawal(wd_amount)
        else:
            print("insufficient balance")
        return self
    
    def display_balance(self):
        print ( self.name + str(self.account.account_info()))
        return self
    
    def __str__(self):
        return self.name + "--> " + str(self.account)                
    
#!user class ends


chamith_savings = User("Chamith","Savings Account ",5000 )
chamith_current = User("Chamith", "Current Account",2500 )


chamith_current.make_deposit(500).make_deposit(100).make_deposit(600).make_deposit(400).make_deposit(700).display_balance()

