# Please fill the wallet class according to the writeup.
class BankAccont():
    pass
    # your code goes here
    # Remove pass statement when you start writing your code
    def __init__(self,Owner):
        self.balance=0.0
        self.Owner=Owner
    def Withdrawal(self,n):
        if(self.balance<n):
            return "Insufficient funds"
        elif(n<0):
            return "Amount can't be negative"
        else:  
            self.balance-=n
            return self.Owner+" Your account balance is "+str(self.balance)
    def deposit(self,n):
        if(n<0):
            return "Amount can't be negative"
        self.balance+=n
        return self.Owner+" Your account balance is "+str(self.balance)
  

# Don't change the below code
name=input()
n = int(input())
w = BankAccont(name)
for i in range(n):
    s = input().split(" ")
    if(s[0] == 'Withdrawal'):
        print(w.Withdrawal(float(s[1])))
    elif(s[0] == 'deposit'):
        print(w.deposit(float(s[1])))
    



