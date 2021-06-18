class BankAccount:
    def __init__(self, int_rate=0, balance=0):
    #def display_user_balance (self):
    #print(f"usuario: {self.name}, saldo: {self.account_balance}")// no dejar print en constructor
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
    #Agrega un método de depósito a la clase BankAccount
        self.balance += amount
        return self
    def withdraw(self, amount):
    #Agrega un método de retiro a la clase BankAccount
        if amount > self.balance:
            print(f"Fondos insuficientes: cobrar una tarifa de ${amount - self.balance}")
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
    #Agrega un método display_account_info a la clase BankAccount
        print(f"Saldo: ${self.balance}")
        return self
    def yield_interest(self):
    # Agrega un método yield_interest a la clase BankAccount
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
        
    #Crea 2 cuentas
    #En la primera cuenta, realice 3 depósitos y 1 retiro, luego calcule los intereses y muestre la información de la cuenta en una sola línea de código (es decir, encadenamiento)
    #En la segunda cuenta, realice 2 depósitos y 4 retiros, luego calcule los intereses y muestre la información de la cuenta en una sola línea de código (es decir, encadenamiento)
    
cuenta1 = BankAccount(0.01)
cuenta2 = BankAccount(0.09)

cuenta1.deposit(200).deposit(200).deposit(200).withdraw(100).yield_interest().display_account_info()

cuenta2.deposit(1000).deposit(1000).withdraw(300).withdraw(200).withdraw(500).yield_interest().display_account_info()
    