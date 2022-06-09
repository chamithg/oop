class Store:
    def __init__(self,name):
        self.name = name
        self.list =[]
    
    def add_product(self,new_product):
        if new_product not in self.list:
            self.list.append(new_product)
        
    def sell_product(self,id):
        print(f"{self.list[id]} is sold")
        self.list.pop(id)
        return(self)
    
    def inflation (self, inflation_rate):
        for item in self.list:
            item.update_price(percent_changed = inflation_rate, is_increased = True)    
            
    def set_cleareance (self, clearance_rate):
        for item in self.list:
            item.update_price(percent_changed = clearance_rate, is_increased = False)    
            
    def __str__(self):
        for item in self.list:
            print(item) 
            
        return "end of the list"

class Product:
    def __init__(self,name, price, catagory):
        self.name = name
        self.price = price
        self.catagory = catagory
        
    def print_info(self):
        return f"{self.name} catagory: {self.catagory} price: {self.price}"
    
    def update_price(self,percent_changed, is_increased):
        if is_increased:
            self.price += round(self.price * percent_changed / 100,2)
        else:
            self.price -= round(self.price * percent_changed / 100,2)
        return self
    
    def __str__(self):
        return f"{self.name} catagory: {self.catagory} price: {self.price}"
    

lucky_supermarket = Store("lucky")


carrot = Product("carrot",1.99 ,"vegatable")
cabbage = Product("cabbage",2.99 ,"vegatable")
chicken = Product("chicken",1.99 ,"meat")
apple = Product("apple",4.99 ,"fruit")
milk = Product("milk",1.99 ,"dairy")
yogurt = Product("yogurt",1.99 ,"dairy")
pears = Product("pears",1.99 ,"fruits")

list = [carrot,cabbage,chicken,apple,milk,yogurt,pears]

lucky_supermarket.add_product(carrot)
lucky_supermarket.add_product(cabbage)
lucky_supermarket.add_product(chicken)
lucky_supermarket.add_product(apple)
lucky_supermarket.add_product(milk)
lucky_supermarket.add_product(yogurt)
lucky_supermarket.add_product(pears)

print(lucky_supermarket)

lucky_supermarket.inflation(1.05)


print(lucky_supermarket)

lucky_supermarket.set_cleareance(25)

print(lucky_supermarket)