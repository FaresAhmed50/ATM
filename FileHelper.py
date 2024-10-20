import csv
import uuid
from abc import ABC, abstractmethod
import pandas as pd
import datetime
from tkinter import messagebox


class FileHelper(ABC):

    @abstractmethod
    def Save_client_to_CSV(self, fielname: str, ClientList: list):
        with open(fielname, mode="a", newline="") as file:
            write = csv.writer(file)

            for Client in ClientList:
                write.writerow(
                    [Client.id, Client.firstname, Client.lastname, Client.phonenumber, Client.age, Client.gender,
                     Client.password,
                     Client.balance])
        print("Done")

    @classmethod
    def Save_Admin_to_CSV(self, fielname: str, AdminList: list):
        with open(fielname, mode="a", newline="") as file:
            write = csv.writer(file)

            for Admin in AdminList:
                write.writerow(
                    [Admin.firstname, Admin.lastname, Admin.id, Admin.password]
                )

    @abstractmethod
    def Generate_Unique_Id(self, Saved_ID: set):
        while True:
            new_id = str(uuid.uuid4())
            if new_id not in Saved_ID:
                Saved_ID.add(new_id)
                return new_id

    @abstractmethod
    def jaccard_similarity(self, s1, s2):
        """Calculates the Jaccard similarity between two strings."""
        set1 = set(s1)
        set2 = set(s2)
        intersection = set1.intersection(set2)
        union = set1.union(set2)
        if len(union) == 0:
            return 0
        return len(intersection) / len(union)

    @abstractmethod
    def Client_Search(self, clientname, clientpass):
        df = pd.read_csv('Clients.csv')
        client = df[(df['firstname'] == clientname) & (df['password'] == clientpass)]

        if not client.empty:
            return client
        else:
            print("Client Not Found OR Invalid Password")
            return None

    @abstractmethod
    def Admin_Search(self, Admin_id : str, Admin_pass : str):
        df = pd.read_csv('Admin.csv')
        df['id'] = df['id'].astype(str)
        df['password'] = df['password'].astype(str)
        admin = df[(df['id'] == Admin_id) & (df['password'] == Admin_pass)]
        if not admin.empty:
            return admin
        else:
            print("Admin Not Found OR Invalid Password")
            return

    @classmethod
    def deposit(self, client, amount):
        client_balance = client.iloc[0]['balance']
        client_id = client.iloc[0]['id']
        if amount > 0:
            client['balance'] += amount
            print(f"{amount} has been deposited. New balance: {client_balance}")
            df = pd.read_csv('Clients.csv')
            sender_index = df[df['id'] == client_id].index
            print(f"ssender index : {sender_index}")
            if sender_index.empty:
                print("sender not found")
                return
            df.loc[sender_index[0], 'balance'] += amount
            print(f"{amount} has been deposited. New balance: {client_balance}")
            df.to_csv('Clients.csv' , mode='w', index=False)

            trans = pd.read_csv('transaction.csv')
            trans.loc[len(trans)] = [client_id, client_id, amount, 'deposit',
                                     datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
            trans.to_csv('transaction.csv', mode='w',  index=False)
            print('Done')
        else:
            print("Deposit amount must be greater than zero.")

    @abstractmethod
    def withdraw(self, client, amount):
        client_balance = client.iloc[0]['balance']
        client_id = client.iloc[0]['id']
        if amount > client_balance:
            print(f"Insufficient funds. Your balance is {client_balance}.")
        elif amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        else:
            client_balance -= amount
            df = pd.read_csv('Clients.csv')
            sender_index = df[df['id'] == client_id].index
            if sender_index.empty:
                print("sender not found")
                return
            df.loc[sender_index[0], 'balance'] -= amount
            print(f"{amount} has been withdrawn. New balance: {client_balance}")

            df.to_csv('Clients.csv', index=False)

            trans = pd.read_csv('transaction.csv')
            trans.loc[len(trans)] = [client_id, client_id, amount, 'withdraw',
                                     datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
            trans.to_csv('transaction.csv', index=False)

    @abstractmethod
    def change_password(self, old_password, new_password, client , popup):
        client_pass = client.iloc[0]['password']
        if old_password == client_pass:
            password_similarity = self.jaccard_similarity(FileHelper, old_password, new_password)
            if password_similarity > 0.5:
                # print(f"password similar {password_similarity * 100} change your password")
                messagebox.showwarning("Warning", f"Password similarity is high: {password_similarity * 100:.2f}%. Please choose a different password.")
                response = messagebox.askyesno(
                    "Warning",
                    f"Password similarity is high: {password_similarity * 100:.2f}%. Do you want to try again?"
                )
                if response:
                    return
                else:
                    messagebox.showinfo("INFO", f"Password Not Change")
                    popup.destroy()
                    return 
            else:
                df = pd.read_csv('Clients.csv')
                target_index = df[df['id'] == client.iloc[0]['id']].index
                if not target_index.empty:
                    df.loc[target_index[0], 'password'] = new_password  
                    df.to_csv('Clients.csv', index=False)
                    messagebox.showinfo("Success", "Password changed successfully!")
                    popup.destroy()
                else:
                    messagebox.showerror("Error", "Client not found in the database.")
                    popup.destroy()
        else:
            messagebox.showerror("Error", "Current password is incorrect.")
            popup.destroy()

    @abstractmethod
    def transaction(self, sender_id, reciver_id, amount):
        df = pd.read_csv('Clients.csv')
        sender_index = df[df['id'] == sender_id].index
        if sender_index.empty:
            print("sender not found")
            return
        sender_balance = df.loc[sender_index[0], 'balance']
        reciver_index = df[df['id'] == reciver_id].index
        if reciver_index.empty:
            print("reciver not found")
            return
        if sender_balance >= amount:
            df.loc[sender_index[0], 'balance'] -= amount
            df.loc[reciver_index[0], 'balance'] += amount
            df.to_csv('Clients.csv', index=False)
            trans = pd.read_csv('transaction.csv')
            trans.loc[len(trans)] = [sender_id, reciver_id, amount, 'transaction',
                                     datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
            trans.to_csv('transaction.csv', index=False)
            return f"Transaction Successful. Remaining Balance for sender: {sender_balance - amount} and for receiver: {df.loc[reciver_index[0], 'balance']}"
        else:
            print("Insufficient funds")
