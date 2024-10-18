import csv
import uuid
from abc import ABC, abstractmethod


class FileHelper(ABC):

    @abstractmethod
    def Save_to_CSV(self, fielname: str, ClientList: list):
        with open(fielname, mode="a", newline="") as file:
            write = csv.writer(file)

            for Client in ClientList:
                write.writerow([Client.id , Client.firstname, Client.lastname, Client.phonenumber, Client.age, Client.balance])

    print("Done")

    @abstractmethod
    def Generate_Unique_Id(self, Saved_ID: set):
        while True:
            new_id = str(uuid.uuid4())
            if new_id not in Saved_ID:
                Saved_ID.add(new_id)
                return new_id
