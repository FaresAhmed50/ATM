from FileHelper import FileHelper
import pandas as pd
import datetime

Saved_ID = set()


class Client:

    def __init__(self, firstname: str, lastname: str, phonenumber: int, age: int, gender: str, password: str,
                 initial_balance: float = 0, id: str = None):
        # Running validation Statement
        # assert int.__sizeof__(phonenumber) == 11, f"The Phone Number must be 11 characters long"
        # assert age >= 19, f"The Age of the user must be greater than 18 years old"

        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phonenumber
        self.age = age
        self.gender = gender
        self.password = password
        self.balance = initial_balance

    def __str__(self):
        # A string method to display the client details and balance
        return (f"Client: {self.firstname} {self.lastname}, Phone: {self.phonenumber}, "
                f"Age: {self.age}, Balance: {self.balance}")
