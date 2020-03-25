class fib():
    def __init__(self):
        self.fib = [0,1]

    def fibo(self,num):
        self.fib = [0,1]
        while(self.fib[len(self.fib)-1]<=num):
            if((self.fib[len(self.fib)-1]+self.fib[len(self.fib)-2])<=num):
               self.fib.append(self.fib[len(self.fib)-1]+self.fib[len(self.fib)-2])
            else:
               break
        return self.fib


obj = fib()
fibb = obj.fibo(1000)
print(fibb)
    
