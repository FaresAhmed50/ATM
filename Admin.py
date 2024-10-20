from FileHelper import FileHelper
from Client import Client

ClientList = []
AdminList = []
Saved_ID = set()


class Admin:

    def __init__(self, firstname: str, lastname: str, id: int, password: str):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.password = password
        AdminList.append(self)
        FileHelper.Save_Admin_to_CSV("Admin.csv", AdminList)

    def Creat_new_Client(self, firstname: str, lastname: str, phonenumber: int, age: int, gender: str, password: str,
                         initial_balance: float = 0):
        newClient = Client(firstname, lastname, phonenumber, age, gender, password, initial_balance,
                           FileHelper.Generate_Unique_Id(self, Saved_ID)[:16])
        ClientList.append(newClient)
        print(newClient)
        FileHelper.Save_client_to_CSV(self, "Clients.csv", ClientList)
