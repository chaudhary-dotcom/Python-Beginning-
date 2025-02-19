#Bank account system
class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposite(self, amount):
        try:
            amount = float(amount)
            if amount > 0:
                self.balance += amount
                print(f"{amount} has been credited")
                print(f"{self.balance} is your current balance")
            
            else:
                ("Invalid! enter positive number")

        except ValueError:
            print('Invalid! enter numeric value')
    
    def withdraw(self, amount):
        try:
            amount = float(amount)

            if amount > 0:
                
                if amount <= self.balance:
                    self.balance -= amount
                    print(f'{amount} is debited')
                    print(f'{self.balance} is your current balance.')
                    

                else:
                    print(f"Insufficient ! balance.")
            else:
                print('Enter positive value')
        except ValueError:
            print('Invalid! enter numeric')
    
    def get_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f'Current balance: {self.balance}')

class SavingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance = 0.0):
        super().__init__(account_number, account_holder, balance)
    
    def withdraw(self, amount):
        if amount > 500:
            print('Withdrawal failed. The maximum limit per transactio is $500.')
        
        else:
            super().withdraw(amount)
    
    def add_intrest(self, rate):
        if rate < 0:
            print('Intrest rate must be positive')
        
        else:
            intrest = self.balance * (rate / 100)
            self.balance += intrest
            print(f"Intrest rate: {rate}, Intrest: {intrest:.2f} added. New balance: {self.balance}")
        
