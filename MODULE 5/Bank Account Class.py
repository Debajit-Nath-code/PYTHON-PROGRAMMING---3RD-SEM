class BankAccount:
    def __init__(self, holder, funds):
        self.holder = holder
        self.funds = funds

    def add_funds(self, cash):
        self.funds += cash
        print("Amount Deposited:", cash)

    def remove_funds(self, cash):
        if cash <= self.funds:
            self.funds -= cash
            print("Amount Withdrawn:", cash)
        else:
            print("Insufficient Balance")

    def show_info(self):
        print("Account Holder:", self.holder)
        print("Balance:", self.funds)

user_acc = BankAccount("Debajit Nath", 8000)
user_acc.add_funds(3500)
user_acc.remove_funds(2000)
user_acc.show_info()
