from bank_manager import BankManager

manager = BankManager()

print ("Добро пожаловать!")

while True:
    try:
        print ("1. Создать аккаунт")
        print ("2. Изменить аккаунт")
        print ("3. Удалить аккаунт")
        print ("4. Внести депозит")
        print ("5. Снять деньги")
        print ("6. Посмотреть список аккаунтов")
        print ("7. Выйти из программы")
        
        ch = int(input("Выберите действие: "))
        
        if ch == 1:
            name = input("Имя: ")
            try:
                balance = int(input("Баланс: "))
                manager.add_account(name,balance)
                manager.get_data()
            except(ValueError):
                print("Ошибка! Вводите только числа")
        
        elif ch == 2:
            print("1. Изменить только имя"
                "2. Изменить только баланс"
                "3. Изменить весь аккаунт"
                "4. Назад"
                )
            try:
                choi = int(input("Выбор: "))
                if 1<=choi and choi<=4:
                    choi2 = int(input("Номер аккаунта: ")) -1
                    manager.change_accounts(choi,choi2)
                else:
                    print("Ошибка! Выберите действие 1-4!")
            except(ValueError):
                print("Ошибка! Вводите только числа")    
        
        elif ch == 3:
            try:
                cho = int(input("Номер аккаунта: ")) -1
                manager.delete_account(cho)
            except(ValueError):
                print("Ошибка! Вводите только числа") 
        
        elif ch == 4:
            try:
                cho = int(input("Номер аккаунта: ")) -1
                manager.dep_acc(cho)
                manager.get_data()
            except(ValueError):
                print("Ошибка! Вводите только числа") 
        
        elif ch == 5:
            try: 
                cho = int(input("Номер аккаунта: ")) -1
                manager.withdraw_money(cho)
                manager.get_data()
            except(ValueError):
                print("Ошибка! Вводите только числа") 
        
        elif ch == 6:
            manager.get_data()
            
        elif ch == 7:
            print("Выход из программы...")
            break
        else:
            print("Вводите только числа 1-7!")
    except(ValueError):
        print("Вводите только числа!")
    