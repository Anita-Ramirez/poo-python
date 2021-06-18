#Si has estado siguiendo, utilizará la clase de usuario que hemos estado discutiendo para esta tarea.
#Para esta tarea, agregaremos algunas funcionalidades a la clase Usuario:
#make_withdrawal (self, amount) : haz que este método disminuya el saldo del usuario en la cantidad especificada
#display_user_balance (self) : haz que este método imprima el nombre del usuario y el saldo de la cuenta en el terminal
#p.ej. "Usuario: Guido van Rossum, Saldo: $ 150
#BONIFICACIÓN: transfer_money (self, other_user, amount) : haz que este método disminuya el saldo del usuario en la cantidad y agrega esa cantidad al saldo de otro other_user
#Crea un archivo con la clase Usuario, incluidos los métodos __init__ y make_deposit
#Agrega un método make_withdrawal a la clase Usuario
#Agrega un método display_user_balance a la clase Usuario
#Crea 3 instancias de la clase de usuario
#Haz que el primer usuario haga 3 depósitos y 1 retiro y luego muestre su saldo
#Haz que el segundo usuario haga 2 depósitos y 2 retiros y luego muestre su saldo
#Haz que el tercer usuario haga 1 depósitos y 3 retiros y luego muestre su saldo
#BONIFICACIÓN: Agrega un método transfer_money; haga que el primer usuario transfiera dinero al tercer usuario y luego imprima los saldos de ambos usuarios


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
usuario1.make_deposit(100)
usuario1.make_deposit(200)
usuario1.make_deposit(300)
usuario1.display_user_balance()

#Haz que el segundo usuario haga 2 depósitos y 2 retiros y luego muestre su saldo
usuario2.make_deposit(100)
usuario2.make_deposit(200)
usuario2.make_withrawal (50)
usuario2.make_withrawal (50)
usuario2.display_user_balance()

#Haz que el tercer usuario haga 1 depósitos y 3 retiros y luego muestre su saldo
usuario3.make_deposit(500)
usuario3.make_withrawal (50)
usuario3.make_withrawal (50)
usuario3.make_withrawal (50)
usuario3.display_user_balance()

#BONIFICACIÓN: Agrega un método transfer_money; haga que el primer usuario transfiera dinero al tercer usuario y luego imprima los saldos de ambos usuarios
usuario1.transfer_money(usuario3,30)
usuario1.display_user_balance()
usuario3.display_user_balance()