class ATM:
    def __init__(self, user_name, balance=0):
        self.user_name = user_name
        self.balance = balance

    def check_balance(self):
        print(f"\n💰 Current Balance: ₹{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ ₹{amount} deposited successfully.")
            self.check_balance()
        else:
            print("❌ Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Enter a valid amount to withdraw.")
        elif amount > self.balance:
            print("❌ Insufficient balance.")
        else:
            self.balance -= amount
            print(f"✅ ₹{amount} withdrawn successfully.")
            self.check_balance()

    def menu(self):
        while True:
            print("\n==== ATM Menu ====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                try:
                    amt = float(input("Enter amount to deposit: ₹"))
                    self.deposit(amt)
                except ValueError:
                    print("❌ Please enter a valid number.")
            elif choice == '3':
                try:
                    amt = float(input("Enter amount to withdraw: ₹"))
                    self.withdraw(amt)
                except ValueError:
                    print("❌ Please enter a valid number.")
            elif choice == '4':
                print("👋 Thank you for using the ATM. Goodbye!")
                break
            else:
                print("❌ Invalid option. Try again.")

# Run the ATM
if __name__ == "__main__":
    name = input("Enter your name: ")
    atm = ATM(name, 1000)  # initial balance = ₹1000
    atm.menu()
