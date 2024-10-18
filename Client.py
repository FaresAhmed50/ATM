class Client:

    def __init__(self, firstname: str, lastname: str, phonenumber: int, age: int, gender: str, initial_balance: float = 0):

        # Running validation Statement
        # assert int.__sizeof__(phonenumber) == 11, f"The Phone Number must be 11 characters long"
        # assert age >= 19, f"The Age of the user must be greater than 18 years old"

        # passing  the argument to the self object
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phonenumber
        self.age = age
        self.gender = gender
        self.balance = initial_balance

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

