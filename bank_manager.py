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
            json.dump([t.to_dict() for t in self.accounts],f,ensure_ascii=False, indent=4)
        
    def add_account(self,name,balance):
        self.accounts.append(Account(name,balance))
        self.save()
    
    def delete_account(self,index):
        if self.accounts:
            if 0<=index<len(self.accounts):
                self.accounts.pop(index)
                self.save()
            else:
                print("\nАккаунта с таким номером не существует!")
        else:
            print("\nПока не существует ни 1 аккаунта")
    
    def get_data(self):
        for i,accounts in enumerate(self.accounts,1):
            print(f"{i}. {accounts.name} | {accounts.balance}")
            
    def change_accounts(self,choice,index):
        if 0<=index<len(self.accounts):
            data = self.accounts[index]
            if choice == 1:
                name = input("\nНовое имя: ")
                data.rename(name)
            elif choice == 2:
                dep = int(input("\nНовый баланс: "))
                data.new_balance(dep)
            elif choice == 3:
                name = input("\nНовое имя: ")
                dep = int(input("\nНовый баланс: "))
                data.change_all(name,dep)
            self.save()
        else:
            print("\nАккаунта под таким номером не существует!")
    
    def dep_acc(self,index):
        if 0<=index<len(self.accounts):
            amoun = int(input("\nСумма депозита: "))
            if amoun>0:
                self.accounts[index].balance += amoun
                self.save()
            else:
                print("\nОшибка! Сумма депозита должна быть положительным числом!")
        else:
            print("\nАккаунта с таким номером не существует!")
    
    def withdraw_money(self,index):
        if 0<=index<len(self.accounts):
            amoun = int(input("\nСумма снятия: "))
            if amoun>0:
                self.accounts[index].balance -= amoun
                self.save()
            else:
                print("\nОшибка! Сумма снятия должна быть положительным числом!")
        else:
            print("\nАккаунта с таким номером не существует!")