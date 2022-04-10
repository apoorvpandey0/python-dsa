class Blog:

    counter = 0

    def __init__(self,title,desc):
        self.title = title
        self.desc = desc
        Blog.counter += 1
        self.id = Blog.counter

    def __str__(self):
        return "Blog with title: {} and desc: {}".format(self.title,self.desc)
    

Blogs = []

while True:
    choice = input('Blogs Manager add/del/all/update/quit/ > ')
    
    if choice =='add':
        title = input('Enter title: ')
        description = input('Enter description: ')
        
        exp = Blog(title = title,desc = description)

        Blogs.append(exp)
        
        print("Successfully added new Blog!\n")
    
    if choice == 'all':
        print("Blogs:\n")
        for exp in Blogs:
            print(exp)
            print("")

    if choice == 'del':
        id = int(input('Enter Blog ID to delete: '))
        for exp in Blogs:
            if exp.id == id:
                Blogs.remove(exp)
                print("Successfully deleted Blog!\n")
                break
        else:
            print("No Blog found with ID {}\n".format(id))
            
    if choice =='update':
        id = int(input('Enter Blog ID to update: '))
        for exp in Blogs:
            if exp.id == id:
                title = input('Enter new title: ')
                description = input('Enter new description: ')
                exp.title = title
                exp.desc = description
                print("Successfully updated Blog!\n")
                break
        else:
            print("No Blog found with ID {}\n".format(id))

    if choice =='quit':
        print("Thanks for using this budget manager :)")
        break
    