import tkinter as tk
import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database='bank_system'
)
db_cursor = db_connection.cursor()

db_cursor.execute('''CREATE TABLE IF NOT EXISTS 
bank_accounts ( id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255) NOT NULL,
age INT,phone_number VARCHAR(20),
credit DECIMAL(10, 2),
password INT)''')


db_connection.commit()

class BankAccountApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Account System")

        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self.root, text="Enter Your Name")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.age_label = tk.Label(self.root, text="Enter Your Age")
        self.age_label.pack()
        self.age_entry = tk.Entry(self.root)
        self.age_entry.pack()

        self.phone_label = tk.Label(self.root, text="Enter Your Phone Number")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.pack()

        self.credit_label = tk.Label(self.root, text="Enter Your Credit")
        self.credit_label.pack()
        self.credit_entry = tk.Entry(self.root)
        self.credit_entry.pack()

        self.password_label = tk.Label(self.root, text="Enter Your Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root)
        self.password_entry.pack()

        self.create_button = tk.Button(self.root, text="Create Bank Account", command=self.create_bank_account)
        self.create_button.pack()

    def create_bank_account(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        phone_number = self.phone_entry.get()
        credit = self.credit_entry.get()
        password = self.password_entry.get()


        insert_query = "INSERT INTO bank_accounts (name, age, phone_number, credit, password) VALUES (%s, %s, %s, %s, %s)"
        values = (name, age, phone_number, credit, password)  # Initialize credit, password, and national_id to zero
        db_cursor.execute(insert_query, values)
        db_connection.commit()

        self.name_entry.delete(0, 'end')
        self.age_entry.delete(0, 'end')
        self.phone_entry.delete(0, 'end')
        self.credit_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')

def main():
    root = tk.Tk()
    app = BankAccountApp(root)
    root.mainloop()


main()

