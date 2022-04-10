# N = int(input('Enter the number of elements:'))

# lst = []

# for i in range(N):
#     tmp = int(input('Enter value at index {}:'.format(i))) 
#     lst.append(tmp)

# print(lst)



# # def func(amount,desc):
# #     print("This is a function")
    
# # func()
# def betterprint(expense):
#     print("Expese of amount {} for {}".format(expense.amount,expense.desc))


# class Expense:
    
#     def __init__(self,amount,desc):
#         self.amount = amount
#         self.desc = desc

#     def betterprint(self):
#         print("Expese of amount {} for {}".format(self.amount,self.desc))
    
# exp1 = Expense(100,'Cab')
# exp2 = Expense(200,'Lunch')

# expenses = [exp1,exp2]

# # print(expenses)

# for exp in expenses:
#     # print(exp)
#     exp.betterprint()

# print(exp1)
# exp1.betterprint()

# print(exp2)
# exp2.betterprint()


# betterprint(exp1)
# betterprint(exp2)


# print(exp1)
# print("Expese of amount {} for {}".format(exp1.amount,exp1.desc))
# print(exp2)
# print("Expese of amount {} for {}".format(exp2.amount,exp2.desc))





# print(exp1)
# print(exp2)

# # These addresses will be unique
# # <__main__.Expense object at 0x7f4095b2b4c0>
# # <__main__.Expense object at 0x7f4095a908b0>


    
class Expense:
    expenses_counter =0

    def __init__(self,id,amount,desc):
        self.id = id
        self.amount = amount
        self.desc = desc
        Expense.expenses_counter+=1

    def betterprint(self):
        print("Expese for ID: {}, amount {} and desccription {}".format(self.id,self.amount,self.desc))
    

expenses = []

while True:
    choice = input('Budget Manager add/quit/update/all > ')
    
    if choice =='add':
        amt = int(input('Enter amount: '))
        description = input('Enter description: ')
        
        exp = Expense(id = Expense.expenses_counter+1,amount = amt,desc = description)

        expenses.append(exp)
        
        print("Successfully added new expense!\n")
    
    if choice == 'all':
        print("Expenses:\n")
        for exp in expenses:
            exp.betterprint()
            print("")
        
        # Calculating total expenses amount
        total = 0
        for exp in expenses:
            total += exp.amount
        
        print("Total: {} Rs.\n".format(total))

    if choice == 'del':
        id = int(input('Enter expense ID to delete: '))
        for exp in expenses:
            if exp.id == id:
                expenses.remove(exp)
                print("Successfully deleted expense!\n")
                break
        else:
            print("No expense found with ID {}\n".format(id))

    if choice == 'update':
        id = int(input('Enter expense ID to update: '))
        for exp in expenses:
            if exp.id == id:
                amt = int(input('Enter new amount: '))
                description = input('Enter new description: ')
                exp.amount = amt
                exp.desc = description
                print("Successfully updated expense!\n")
                break
        else:
            print("No expense found with ID {}\n".format(id))
    
    if choice =='quit':
        print("Thanks for using this budget manager :)")
        break
        
      