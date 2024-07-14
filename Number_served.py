class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name=restaurant_name
        self.cuisine=cuisine_type
        self.number_served=0

    def set_number_served(self,number_served):
        if number_served!=self.number_served:
            self.number_served=number_served
            print(f"This restrant has already seved {self.number_served} people.")

    def increment_number_served(self,increment):
        self.number_served+=increment
        print(f"The served number has benn updated to be {self.number_served} with increment {increment}.")

    def describe_restaurant(self):
        info=f"{self.name}  {self.cuisine}"
        return info
        
    
    def open_restaurant(self):
        print(f"The restaurant {self.name.title()} is open now.\n")

fandian=Restaurant('KFC','American_Food')
print(fandian.describe_restaurant)
print(f"This restrant has already seved {fandian.number_served} people.")
fandian.set_number_served(1000)
fandian.increment_number_served(250)





    