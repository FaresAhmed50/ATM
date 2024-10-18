import csv
from abc import ABC, abstractmethod


class FileHelper(ABC):

    @abstractmethod
    def Save_to_CSV(self, fielname: str, ClientList: list):
        with open(fielname, mode="a", newline="") as file:
            write = csv.writer(file)

            for Client in ClientList:
                write.writerow([Client.firstname, Client.lastname, Client.phonenumber, Client.age, Client.balance])

    print("Done")
