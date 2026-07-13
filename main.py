from bank_manager import BankManager

manager = BankManager()

print ("\n\nДобро пожаловать!\n")

while True:
    try:
        print ("\n1. Создать аккаунт\n")
        print ("2. Изменить аккаунт\n")
        print ("3. Удалить аккаунт\n")
        print ("4. Внести депозит\n")
        print ("5. Снять деньги\n")
        print ("6. Посмотреть список аккаунтов\n")
        print ("7. Выйти из программы\n\n")
        
        ch = int(input("Выберите действие: "))
        print("")
        if ch == 1:
            name = input("Имя: ")
            try:
                balance = int(input("Баланс: "))
                manager.add_account(name,balance)
            except(ValueError):
                print("Ошибка! Вводите только числа")
        
        elif ch == 2:
            print("1. Изменить только имя\n"
                "2. Изменить только баланс\n"
                "3. Изменить весь аккаунт\n"
                "4. Назад\n"
                )
            try:
                print("Список аккаунтов:\n")
                manager.get_data()
                choi = int(input("\nВыбор: "))
                if choi ==4:
                    continue
                if 1<=choi and choi<4:
                    choi2 = int(input("\nНомер аккаунта: ")) -1
                    manager.change_accounts(choi,choi2)
                else:
                    print("\nОшибка! Выберите действие 1-4!")
            except(ValueError):
                print("\nОшибка! Вводите только числа")    
        
        elif ch == 3:
            try:
                print("Список аккаунтов:\n")
                manager.get_data()
                cho = int(input("\nНомер аккаунта для удаления: ")) -1
                manager.delete_account(cho)
            except(ValueError):
                print("\nОшибка! Вводите только числа") 
        
        elif ch == 4:
            try:
                print("Список аккаунтов:\n")
                manager.get_data()
                cho = int(input("\nНомер аккаунта для депозита: ")) -1
                manager.dep_acc(cho)
            except(ValueError):
                print("\nОшибка! Вводите только числа") 
        
        elif ch == 5:
            try: 
                cho = int(input("\nНомер аккаунта: ")) -1
                manager.withdraw_money(cho)
            except(ValueError):
                print("\nОшибка! Вводите только числа") 
        
        elif ch == 6:
            print("Список аккаунтов:\n")
            manager.get_data()
            
        elif ch == 7:
            print("\nВыход из программы...\n")
            break
        else:
            print("\nВводите только числа 1-7!")
    except(ValueError):
        print("\nВводите только числа!")
    