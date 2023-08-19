class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return f"Your account balance is ${self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"${amount} deposited successfully."
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return f"${amount} withdrawn successfully."
        elif amount <= 0:
            return "Invalid withdrawal amount."
        else:
            return "Insufficient balance."

def main():
    atm = ATM()

    while True:
        print("ATM Simulator")
        print("Options:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            print(atm.check_balance())
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            print(atm.deposit(amount))
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            print(atm.withdraw(amount))
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
