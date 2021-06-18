class User:
    def __init__(self,nombre,email):
        self.name = nombre
        self.email = email
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance  += amount
        return self
    def make_withrawal (self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance (self):
        print(f"usuario: {self.name}, saldo: {self.account_balance}")
        #other_user_balance = amount
        return self
    def transfer_money (self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


usuario1 = User("guido Van Rossum", "guido@python.com")
usuario2 =  User("Pedro Perez", "pedro@python.com")
usuario3 = User("jose Perez", "jose@py3thon.com")


#Haz que el primer usuario haga 3 depósitos y 1 retiro y luego muestre su saldo
usuario1.make_deposit(100).make_deposit(200).make_deposit(300)
usuario1.display_user_balance()

#Haz que el segundo usuario haga 2 depósitos y 2 retiros y luego muestre su saldo
usuario2.make_deposit(100).make_deposit(200)
usuario2.make_withrawal (50).make_withrawal (50)
usuario2.display_user_balance()

#Haz que el tercer usuario haga 1 depósitos y 3 retiros y luego muestre su saldo
usuario3.make_deposit(500)
usuario3.make_withrawal (50).make_withrawal (50).make_withrawal (50)
usuario3.display_user_balance()

#BONIFICACIÓN: Agrega un método transfer_money; haga que el primer usuario transfiera dinero al tercer usuario y luego imprima los saldos de ambos usuarios
usuario1.transfer_money(usuario3,30)
usuario1.display_user_balance()
usuario3.display_user_balance()