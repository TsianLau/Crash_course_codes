class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name=restaurant_name
        self.cuisine=cuisine_type

    def describe_restaurant(self):
        info=f"{self.name}  {self.cuisine}"
        return info
    
    def open_restaurant(self):
        print(f"The restaurant {self.name.title()} is open now.\n")


fandian={
    'dian1':{
        'name':'KFC',
        'type':'take_away_food'
        },
    'dian2':{
        'name':'shaxianxiaochi',
        'type':'Chinese_food'
    },
    'dian3':{
        'name':'Ajisen_Ramen',
        'type':'Japanese_food'
    },
   }

for place,place_info in fandian.items():
    R_info=Restaurant(place_info['name'], place_info['type'])
    print(R_info.describe_restaurant())
    R_info.open_restaurant()



    