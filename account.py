class Account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        
    def rename(self,new_name):
        self.name = new_name
    
    def new_balance(self, new_bal):
        self.balance = new_bal
    
    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def change_all(self, new_name,amount):
        self.balance = amount
        self.name = new_name
    def to_dict(self):
        return {
            "name": self.name,
            "balance": self.balance
        }
        
    @staticmethod
    def from_dict(data):
        return Account (
            data["name"],
            data["balance"]
        )