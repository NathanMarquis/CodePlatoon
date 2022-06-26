from audioop import add
import csv

class Bank:
    def __init__(self):
        pass
    def __str__():
        pass

class Owner:
    def __init__(self, user_id, l_name, f_name, street_address, city, state):
        self.user_id = user_id
        self.full_name = f"{f_name} {l_name}"
        self.address = f"{street_address}, {city}, {state}"


    def __str__(self):
        return(f"{self.name}'s account.")

    def all_owners():
        own_list = []
        path = r"C:\Users\natha\Documents\Coding\oop-bank-accounts\support\owners.csv"
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                own_list.append(Owner(int(row['ID']), row['L_name'], row["F_name"], row['street_address'], row['city'], row['state']))

        return own_list

class Account():

    def __init__(self, id, initial_balance, open_date):
        if initial_balance < 0:
            raise Exception('Initial balance cannot be negative.')
        self.id = id
        self.balance = initial_balance
        self.open_date = open_date

    def __str__(self):
        return self.id

    def withdraw(self, amount):
        if amount > self.balance:
            print('Sorry, insufficient account balance for withdrawl.')
        else:
            self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def add_owner(self):
        self.owner = Owner()

        path = r"C:\Users\natha\Documents\Coding\oop-bank-accounts\support\account_owners.csv"
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                own_list.append(Owner(int(row['ID']), row['L_name'], row["F_name"], row['street_address'], row['city'], row['state']))

    @classmethod
    def all_accounts():
        acc_list = []
        path = r"C:\Users\natha\Documents\Coding\oop-bank-accounts\support\accounts.csv"
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                acc_list.append(Account(int(row['ID']), int(row['Balance']), row["Open_date"]))

        return acc_list

    def find(id):
        accounts = Account.all_accounts()
        for account in accounts:
            if account.id == id:
                return account

class Savings_account(Account):
    def __init__(self, id, initial_balance):
        if initial_balance < 10:
            raise ValueError ('Initial savings balance cannot be less than $10.')
        self.id = id
        self.initial_balance = initial_balance

    def add_interest(rate):
        pass

    def withdrawl(amount):
        pass

    




# Acc1 = Account(123, 10)
# Acc1.add_owner('Jeff', '121 w street road', '20')
# print(Acc1.owner)

print(Account.find('1212'))
list1 = Account.all_accounts()

persona = list1[0]

print(persona.id)