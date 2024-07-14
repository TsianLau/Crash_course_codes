from user import User
class Admin(User):
    """Add an attribute, privileges"""
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        
    def show_privileges(self):
        self.privileges=' '
        msg=input("can this admin add post,Y/N?")
        if msg=='Y':
            self.privileges+='can add post  '
        msg=input("Can this admin delete post,Y/N?")
        if msg=='Y':
            self.privileges+='can delete post   '
        msg=input("Can this admin ban user,Y/N?")
        if msg=='Y':
            self.privileges+='can ban user  '
        print(f"The admin have the following privileges:\n {self.privileges}")

guy=Admin('David','Lau')
guy.show_privileges()


