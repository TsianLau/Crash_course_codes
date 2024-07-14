class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.gender='male'
        self.age=3
        self.login_attempts=10
    
    def user_age(self,age):
        if age!=self.age:
            self.age=age

    def increment_login_attempts(self):
        self.login_attempts=self.login_attempts+1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts=0
        return self.login_attempts
  
    
    def user_gender(self,gender):
        if gender!=self.gender:
            self.gender=gender
  
    
    def describe_user(self):
        info=f"{self.first_name.title()}    {self.last_name.title()}    {self.gender.title()}   {self.age}"
        return(info)
    
# Me=User('David','Lau')
# print(Me.describe_user())
# print(f"{Me.first_name} {Me.last_name} has already logined in for {Me.login_attempts} times.\n")
# Me.increment_login_attempts()
# print(f"{Me.first_name} {Me.last_name} has already logined in for {Me.login_attempts} times.\n")
# Me.increment_login_attempts()
# print(f"{Me.first_name} {Me.last_name} has already logined in for {Me.login_attempts} times.\n")
# Me.reset_login_attempts()
# print(f"{Me.first_name} {Me.last_name} has already logined in for {Me.login_attempts} times.\n")