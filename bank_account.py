class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, balance, int_rate): 
        self.balance = balance   
        self.int_rate= int_rate
        return None 
        
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("insufficient funds.")
        return self
    def display_account_info(self):
        print("Balance; $"+ str(self.balance))
        return self
        
    def yield_interest(self):
        self.balance += self.balance* self.int_rate /100 
        return self
    
    def __str__ (self):
        print("Current Balance: $" + str(self.balance))
        print("Interest Rate: " + str(self.int_rate) + "%" )
        return None 
        
    
    
account1 = BankAccount(500,1.05)
account2 = BankAccount(1000,4.5)

account1.deposit(500).deposit(450).deposit(670).yield_interest().display_account_info()
account2.deposit(780).deposit(980).withdraw(250).withdraw(154).withdraw(350).withdraw(700).yield_interest().display_account_info()


print(account2)