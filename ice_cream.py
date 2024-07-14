"""Write a class called IceCreamStand inherits from the Resaurant class"""
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name=restaurant_name
        self.cuisine=cuisine_type

    def describe_restaurant(self):
        info=f"{self.name}  {self.cuisine}"
        return info
    
    def open_restaurant(self):
        print(f"The restaurant {self.name.title()} is open now.\n")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavor):
        super().__init__(restaurant_name,cuisine_type)
        self.flavor=flavor
    def show_flavor(self):
        full_name=f"{self.name} {self.cuisine}"
        print(f"The flavor of {full_name} is {self.flavor}.")




icecreams={
    'stand1':{
        'name':'KFC',
        'type':'Sweets',
        'flavor':'vanilla'
        },
    'stand2':{
        'name':'McDonald',
        'type':'Sweets',
        'flavor':'Avocado'
    },
    'stand3':{
        'name':'PizzaHunt',
        'type':'Sweets',
        'flavor':'Mango'
    },
   }
for IC,IC_info in icecreams.items():
    icecream=IceCreamStand(IC_info['name'], IC_info['type'], IC_info['flavor'])
    icecream.show_flavor()



    
