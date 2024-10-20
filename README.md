
# ATM System with GUI and CSV Data Storage

## Description

This is a simple ATM system built using Python with a graphical user interface (GUI) developed using the `tkinter` library. It allows administrators and clients to perform various operations, such as deposits, withdrawals, balance inquiries, and money transfers, while saving and reading user information from CSV files. 

The project includes the following features:
- Admin account management.
- Client account management.
- Password management with similarity checks.
- Transaction history management.
- Data is persisted using CSV files.

## Features

- **Admin Features:**
  - Add new client accounts.
  - View all client details.

- **Client Features:**
  - Deposit and withdraw money.
  - Change password (with similarity check).
  - View transaction history.
  - Transfer money between accounts.

## Requirements

- Python 3.x
- `tkinter` (usually pre-installed with Python)
- `pandas` library for CSV data handling

### Python Libraries

You can install the required libraries by running:

```bash
pip install pandas
```

## Setup and Installation

### Running the Program

1. Clone this repository or download the project files.

2. Ensure that you have Python 3.x installed on your machine.

3. Install the necessary dependencies using:
    ```bash
    pip install pandas
    ```

4. Run the program using the following command:
    ```bash
    python main.py
    ```

### Creating an Executable (.exe)

If you want to package the project as a standalone `.exe` file, follow these steps:

1. Install **PyInstaller** using:
    ```bash
    pip install pyinstaller
    ```

2. To create the `.exe` file, run the following command from the project directory:
    ```bash
    pyinstaller --onefile --windowed --add-data "Clients.csv;." --add-data "transaction.csv;." --add-data "Admin.csv;." main.py
    ```

3. The generated executable will be placed in the `dist` folder.

4. Ensure the CSV files (`Clients.csv`, `transaction.csv`, `Admin.csv`) are either included in the `dist` folder or packaged inside the `.exe` using the `--add-data` option.

### CSV Files

The program uses the following CSV files to manage data:

- **Clients.csv**: Stores client details such as name, password, balance, etc.
- **Admin.csv**: Stores administrator credentials.
- **transaction.csv**: Stores transaction records for all clients.

Make sure these CSV files are present in the same directory as the executable or Python script, as the application reads and writes data to these files during operation.

## How to Use

### Admin Login

1. When the program is launched, you can log in as an admin by providing the correct admin ID and password.
2. Admins can add new clients and manage client accounts.

### Client Dashboard

1. Clients can log in using their account name and password.
2. Clients can deposit money, withdraw money, change passwords, view transaction history, and transfer money.

### Changing Password

- When a client attempts to change their password, the program checks for similarity between the old and new passwords. If they are too similar, the user will be prompted to enter a new password.

## File Structure

```
ATM_Project/
│
├── main.py                 # Main application logic
├── FileHelper.py           # Helper class for file operations (CSV)
├── Admin.py                # Admin class
├── Clients.csv             # CSV file to store client details
├── Admin.csv               # CSV file to store admin details
├── transaction.csv         # CSV file to store transaction history
└── README.md               # This file
```

## License

This project is open-source and available under the [MIT License](LICENSE).
