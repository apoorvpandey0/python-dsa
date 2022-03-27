class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


class Expense:

    expenses_counter = 0

    def __init__(self,amount,desc):
        self.amount = amount
        self.desc = desc
        Expense.expenses_counter += 1

    def betterprint(self):
        print("Expese of amount {} for {}".format(self.amount,self.desc))
    
