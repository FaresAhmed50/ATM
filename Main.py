from tkinter import *
from tkinter import messagebox
from Admin import Admin
from FileHelper import FileHelper
import pandas as pd


# Gui App using tkinter V1.0.0
class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM System")

        # Main menu
        self.main_menu()

    def main_menu(self):
        self.clear_screen()

        Label(self.root, text="===== ATM System =====", font=("Arial", 16)).pack(pady=10)

        Button(self.root, text="Admin Account", width=25, command=self.admin_login).pack(pady=5)
        Button(self.root, text="Client Account", width=25, command=self.client_login).pack(pady=5)
        Button(self.root, text="Exit", width=25, command=self.root.quit).pack(pady=5)

    def admin_login(self):
        self.clear_screen()

        Label(self.root, text="===== Admin Login =====", font=("Arial", 16)).pack(pady=10)

        Label(self.root, text="Admin ID:").pack(pady=5)
        self.admin_id_entry = Entry(self.root)
        self.admin_id_entry.pack(pady=5)

        Label(self.root, text="Password:").pack(pady=5)
        self.admin_pass_entry = Entry(self.root, show="*")
        self.admin_pass_entry.pack(pady=5)

        Button(self.root, text="Login", command=self.admin_account).pack(pady=10)
        Button(self.root, text="Back to Main Menu", command=self.main_menu).pack(pady=5)

    def admin_account(self):
        admin_id = self.admin_id_entry.get()
        password = self.admin_pass_entry.get()

        admin = FileHelper.Admin_Search(FileHelper, admin_id, password)
        if admin is not None:
            self.admin_dashboard(admin)
        else:
            messagebox.showerror("Error", "Invalid Admin ID or Password")

    def admin_dashboard(self, admin):
        self.clear_screen()

        Label(self.root, text="===== Admin Account =====", font=("Arial", 16)).pack(pady=10)
        Button(self.root, text="Add Client Account", width=25, command=self.add_client_account).pack(pady=5)
        Button(self.root, text="Back to Main Menu", width=25, command=self.main_menu).pack(pady=5)

    def add_client_account(self):
        self.clear_screen()

        Label(self.root, text="===== Add Client Account =====", font=("Arial", 16)).pack(pady=10)

        self.firstname_entry = Entry(self.root)
        self.lastname_entry = Entry(self.root)
        self.phone_entry = Entry(self.root)
        self.age_entry = Entry(self.root)
        self.gender_entry = Entry(self.root)
        self.password_entry = Entry(self.root)
        self.balance_entry = Entry(self.root)

        entries = [
            ("First Name:", self.firstname_entry),
            ("Last Name:", self.lastname_entry),
            ("Phone Number:", self.phone_entry),
            ("Age:", self.age_entry),
            ("Gender (M/F):", self.gender_entry),
            ("Password:", self.password_entry),
            ("Initial Balance:", self.balance_entry),
        ]

        for label, entry in entries:
            Label(self.root, text=label).pack(pady=2)
            entry.pack(pady=2)

        Button(self.root, text="Create Client", command=self.create_client).pack(pady=10)
        Button(self.root, text="Back to Admin Menu", command=self.admin_dashboard).pack(pady=5)

    def create_client(self):
        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()
        phonenumber = int(self.phone_entry.get())
        age = int(self.age_entry.get())
        gender = self.gender_entry.get()
        password = self.password_entry.get()
        initial_balance = float(self.balance_entry.get() or 0)

        admin = Admin("admin", "admin", 1, "admin")
        admin.Creat_new_Client(firstname, lastname, phonenumber, age, gender, password, initial_balance)

        messagebox.showinfo("Success", f"Client '{firstname} {lastname}' created successfully!")
        self.admin_dashboard(None)

    def client_login(self):
        self.clear_screen()

        Label(self.root, text="===== Client Login =====", font=("Arial", 16)).pack(pady=10)

        Label(self.root, text="Account Name:").pack(pady=5)
        self.client_name_entry = Entry(self.root)
        self.client_name_entry.pack(pady=5)

        Label(self.root, text="Password:").pack(pady=5)
        self.client_pass_entry = Entry(self.root, show="*")
        self.client_pass_entry.pack(pady=5)

        Button(self.root, text="Login", command=self.client_account).pack(pady=10)
        Button(self.root, text="Back to Main Menu", command=self.main_menu).pack(pady=5)

    def client_account(self):
        client_name = self.client_name_entry.get()
        password = self.client_pass_entry.get()

        client = FileHelper.Client_Search(FileHelper, client_name, password)
        if client is not None:
            self.client_dashboard(client)
        else:
            messagebox.showerror("Error", "Invalid Client Name or Password")

    def client_dashboard(self, client):
        self.clear_screen()

        client_name = client.iloc[0]['firstname']
        client_id = client.iloc[0]['id']

        Label(self.root, text=f"===== Welcome {client_name} =====", font=("Arial", 16)).pack(pady=10)

        Button(self.root, text="Deposit", width=25, command=lambda: self.deposite_popuop(client)).pack(pady=5)
        Button(self.root, text="Withdraw", width=25, command=lambda: self.withdraw_popup(client)).pack(pady=5)
        Button(self.root, text="Change Password", width=25, command=lambda: self.changePasswordPopUP(client)).pack(
            pady=5)
        Button(self.root, text="View Transaction History", width=25,
               command=lambda: self.view_transaction(client_id)).pack(pady=5)
        Button(self.root, text="Transfer Money", width=25, command=lambda: self.transfer_money_popup(client)).pack(
            pady=5)
        Button(self.root, text="Back to Main Menu", width=25, command=self.main_menu).pack(pady=5)

    def deposite_popuop(self, client):

        popup = Toplevel(self.root)
        popup.title("Enter The  Deposite Amount")

        label = Label(popup, text="Enter the Amount to Deposite ")
        label.pack(pady=10)

        amount_entry = Entry(popup)
        amount_entry.pack(pady=10)

        submit_button = Button(popup, text="Submit", command=lambda: self.process_deposite(popup, amount_entry, client))
        submit_button.pack(pady=10)

    @staticmethod
    def process_deposite(popup, amount_entry, client):
        try:
            amount = float(amount_entry.get())
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be greater than zero.")
                return
            if client is not None:
                FileHelper.deposit(client, amount)
                messagebox.showinfo("Success", f"{amount} deposited successfully!")
                popup.destroy()
            else:
                messagebox.showerror("Error", "Client not found.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def withdraw_popup(self, client):

        popup = Toplevel(self.root)
        popup.title("Enter Withdrawal Amount")

        label = Label(popup, text="Enter the amount to withdraw:")
        label.pack(pady=10)

        amount_entry = Entry(popup)
        amount_entry.pack(pady=10)

        submit_button = Button(popup, text="Submit", command=lambda: self.process_withdraw(popup, amount_entry, client))
        submit_button.pack(pady=10)

    @staticmethod
    def process_withdraw(popup, amount_entry, client):
        try:
            amount = float(amount_entry.get())
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be greater than zero.")
                return
            if client is not None:
                FileHelper.withdraw(FileHelper, client, amount)
                messagebox.showinfo("Success", f"{amount} withdrawn successfully!")
                popup.destroy()  # Close the popup window after successful withdrawal
            else:
                messagebox.showerror("Error", "Client not found.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    @staticmethod
    def view_transaction(client_id):
        try:
            trans = pd.read_csv('transaction.csv')
            client_trans = trans[trans['sender_id'] == client_id]
            if client_trans.empty:
                messagebox.showinfo("No Transactions", "No transactions found for this client.")
            else:
                messagebox.showinfo("Transactions", client_trans.to_string())
        except FileNotFoundError:
            messagebox.showerror("Error", "Transaction history file not found.")

    def transfer_money_popup(self, client):
        popup = Toplevel(self.root)
        popup.title("Transfer Money")

        sender_label = Label(popup, text="Enter Sender's Client ID:")
        sender_label.pack(pady=5)
        sender_id_entry = Entry(popup)
        sender_id_entry.pack(pady=5)

        receiver_label = Label(popup, text="Enter Receiver's Client ID:")
        receiver_label.pack(pady=5)
        receiver_id_entry = Entry(popup)
        receiver_id_entry.pack(pady=5)

        label_amount = Label(popup, text="Enter Transfer Amount:")
        label_amount.pack(pady=5)
        amount_entry = Entry(popup)
        amount_entry.pack(pady=5)

        submit_button = Button(popup, text="Submit",
                               command=lambda: self.process_transfer(popup, sender_id_entry, receiver_id_entry,
                                                                     amount_entry, client))
        submit_button.pack(pady=10)

    @staticmethod
    def process_transfer(popup, sender_id_entry, receiver_id_entry, amount_entry, client):
        sender_id = sender_id_entry.get()
        receiver_id = receiver_id_entry.get()
        try:
            amount = float(amount_entry.get())
            FileHelper.transaction(FileHelper, sender_id, receiver_id, amount)
            messagebox.showinfo("Success", f"{amount} transferred successfully!")
            popup.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def changePasswordPopUP(self, client):
        popup = Toplevel(self.root)
        popup.title("Change Password")

        label = Label(popup, text="Enter Your Current Password")
        label.pack(pady=10)

        currentPass_entry = Entry(popup)
        currentPass_entry.pack(pady=10)

        label = Label(popup, text="Enter Your New Password")
        label.pack(pady=10)

        newPass_entry = Entry(popup)
        newPass_entry.pack(pady=10)

        submit_button = Button(popup, text="Submit",
                               command=lambda: self.change_password(popup, currentPass_entry, newPass_entry, client))
        submit_button.pack(pady=10)

    @staticmethod
    def change_password(popup, current_password, new_password, client):
        if not FileHelper.change_password(FileHelper, current_password.get(), new_password.get(), client, popup):
            return

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = Tk()
    app = ATMApp(root)
    root.mainloop()

# The Command line of the program V0.9.0

# # Main function for user interaction
# def main():
#     # admin = Admin("fares", "Ahmed", 123, "Fares")
#
#     while True:
#         print("\n===== ATM System =====")
#         print("1. Admin Account")
#         print("2. Client Account")
#         print("3. Exit")
#
#         choice = input("Enter your choice (1 | 3 ) : ")
#
#         if choice == "1":
#             print("\n===== Welcome to Admin Account =====")
#             admin_id = str(input("Enter your Admin id : "))
#             password = str(input("Enter your Admin password : "))
#             admin = FileHelper.Admin_Search( FileHelper ,admin_id , password)
#             if admin is not None:
#                 while True:
#                     print("\n===== Admin Account =====")
#                     print("1. Add Client Account")
#                     print("2. Exit")
#                     choice = input("Enter your choice (1 | 2 ) :")
#                     if choice == "1":
#                         admin = Admin("fares", "Ahmed", 123, "Fares")
#                         firstname = input("Enter client's first name: ")
#                         lastname = input("Enter client's last name: ")
#                         phonenumber = int(input("Enter client's phone number: "))
#                         age = int(input("Enter client's age: "))
#                         gender = input("Enter client's gender (M/F): ")
#                         password = input("Enter client's password: ")
#                         initial_balance = float(input("Enter initial balance (optional, default 0): ") or 0)
#                         admin.Creat_new_Client(firstname, lastname, phonenumber, age, gender, password, initial_balance)
#                     else:
#                         print("Exiting Admin Account.")
#                         break
#             else:
#                 break
#         elif choice == "2":
#             print("\n===== Client Account =====")
#             Client_name = input("Enter your Account Name : ")
#             password = input("Enter your Account password : ")
#             client = FileHelper.Client_Search(FileHelper , Client_name, password)
#             if client is not None:
#                 client_id = client.iloc[0]['id']
#                 client_name = client.iloc[0]['firstname']
#
#
#                 while True:
#                     print(f"\n===== Welcome {client_name} =====")
#                     print(f"\n===== What You Want To Do Today ====")
#                     print("1. Deposit")
#                     print("2. Withdraw")
#                     print("3. Change Password")
#                     print("4. View Transaction History")
#                     print("5. Transfer Money")
#                     print("6. Exit")
#                     choice = int(input("Enter your choice (1-6): "))
#
#                     if choice == 1:
#                         amount = float(input("Enter deposit amount: "))
#                         FileHelper.deposit(client, amount)
#                     elif choice == 2:
#                         amount = float(input("Enter The Withdraw amount: "))
#                         FileHelper.withdraw(FileHelper, client, amount)
#                     elif choice == 3:
#                         client_pass = input("Please Enter Your current password: ")
#                         new_password = input("Please Enter your new password: ")
#                         FileHelper.change_password(FileHelper , client_pass ,new_password , client)
#                     elif choice == 4 :
#                         try:
#                             trans = pd.read_csv('transaction.csv')
#                             client_trans = trans[trans['sender_id'] == client_id]
#                             if client_trans.empty:
#                                 print("No transactions found for this client.")
#                             else:
#                                 print(client_trans)
#                         except FileNotFoundError:
#                             print("Transaction history file not found.")
#                     elif choice == 5:
#                         sender_id = input("Enter sender's client ID: ")
#                         reciver_id = input("Enter receiver's client ID: ")
#                         amount = float(input("Enter transfer amount: "))
#                         FileHelper.transaction( FileHelper ,sender_id, reciver_id, amount)
#                     elif choice == 6:
#                         print("Exiting ATM system.")
#                         break
#                     else:
#                         print("Invalid choice. Please select a valid option.")
#         else:
#             print("Tanks for Using Our ATM")
#             break
#
#
#
# if __name__ == "__main__":
#     main()
