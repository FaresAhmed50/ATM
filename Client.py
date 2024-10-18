
class Client:

    def __init__(self, firstname, lastname, phonenumber, age, initial_balance=0):
        # Constructor to initialize the client with personal details and balance
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phonenumber
        self.age = age
        self.balance = initial_balance  # Default balance is set to 0

    def deposit(self, amount):
        # Method to deposit an amount into the client's account
        if amount > 0:
            self.balance += amount
            print(f"{amount} has been deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        # Method to withdraw an amount from the client's account
        if amount > self.balance:
            print(f"Insufficient funds. Your balance is {self.balance}.")
        elif amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn. New balance: {self.balance}")

    def __str__(self):
        # A string method to display the client details and balance
        return (f"Client: {self.firstname} {self.lastname}, Phone: {self.phonenumber}, "
                f"Age: {self.age}, Balance: {self.balance}")

