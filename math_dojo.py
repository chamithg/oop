class MathDojo:
    def __init__(self):
        self.result = 0
    
    def add(self, num, *nums):
        self.result +=num
        for n in nums:
            self.result += n
        return self
    	# your code here
    def subtract(self, num, *nums):
        if num < self.result:
            self.result -=num
        for n in nums:
            if n < self.result:
                self.result -= n
        return self
    	# your code here
# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result

print(x)	# should print 5
# run each of the methods a few more times and check the result!

