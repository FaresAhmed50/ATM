from FileHelper import FileHelper
from Client import Client

ClientList = []


class Admin():

    def __init__(self):
        self.ClientList = []

    def Creat_new_Client(self, firstname: str, lastname: str, phonenumber: int, age: int, gender: str, initial_balance: float = 0):
        newClient = Client(firstname, lastname, phonenumber, age, gender, initial_balance)
        self.ClientList.append(newClient)
        FileHelper.Save_to_CSV( self, "Clients.csv", self.ClientList)



admin = Admin()

admin.Creat_new_Client("Fares", "Ahmed", 12159161611, 29, "M", 0)