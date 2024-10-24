def show_balance(balance):
    print('*' * 20)
    print(f'Your Balance is :{balance:.2f}')
    print('*' * 20)


def deposit(balance):
    print('*' * 20)
    amount = float(input("enter the amount you want to deposit:"))
    print('*' * 20)
    if amount < 0:
        print('*' * 20)
        print("That's not a valid amount")
        print('*' * 20)
        return 0
    else:
        return amount+balance


def withdraw(balance):
    print('*' * 20)
    amount = float(input("enter the amount to be withdraw: "))
    print('*' * 20)
    if amount > balance:
        print('*' * 20)
        print("insufficient fund")
        print('*' * 20)
        return 0
    elif amount < 0:
        print('*' * 20)
        print("Amount must be greater than zero")
        print('*' * 20)
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print('*'*20)
        print('Welcome to SBI Bank')
        print('*' * 20)
        print("1.show Balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.exit")
        print('*'*20)

        choice = (input("enter your choice (1-4):"))

        if choice == '1':
            show_balance(balance)
            # quit()
        elif choice == '2':
            balance += deposit(balance)
            # quit()

        elif choice == '3':
            balance -= withdraw(balance)
            # quit()
        elif choice == '4':
            is_running = False
        else:
            print('*' * 20)
            print("enter the valid choice")
    print('*' * 20)
    print("Thank you have a nice day")
    print('*' * 20)


if __name__ == '__main__':
    main()
