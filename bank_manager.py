import json
from account import Account

class BankManager:
    def __init__(self, filename="accounts.json"):
        self.filename = filename
        self.accounts = self.load()
    
    def load(self):
        try:
            with open (self.filename,"r",encoding="utf-8")as f:
                data = json.load(f)
                return [Account.from_dict(t) for t in data]
        except(FileNotFoundError, json.JSONDecodeError):
            return[]
        
    def save(self):
        with open(self.filename,"w",encoding="utf-8")as f:
            json.dump([t.to_dict for t in self.accounts],f,ensure_ascii=False, indent=4)
        
    def add_account(self,name,balance):
        self.accounts.append(Account(name,balance))
        self.save()
    
    def delete_account(self,index):
        if self.accounts:
            if 0<=index<len(self.accounts):
                self,self.accounts.pop(index)
                self.save()
            else:
                print("Введите корректное число!")
        else:
            print("Пока не существует ни 1 аккаунта")
    
    def get_data(self):
        return self.accounts
    
    def change_accounts(self,choice,index):
        if 0<=index<len(self.accounts):
            data = self.accounts[index]
            if choice == 1:
                name = input("Новое имя: ")
                data.rename(name)
            elif choice == 2:
                dep = int(input("Сумма депозита: "))
                data.deposit(dep)
            elif choice == 3:
                name = input("Новое имя: ")
                dep = int(input("Сумма депозита: "))
                data.change_all(name,dep)
            elif choice == 4:
                return
        else:
            print("Аккаунта под таким номером не существует!")