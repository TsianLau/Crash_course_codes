class Car:
    # 定义初始化attribute
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    # 定义与类相关的方法
    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    # 输出行驶里程信息
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    # 更新里程信息
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
    # 里程增量,增加新的parameter：miles
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
    
# 利用上面的battery扩展为一个新的class
class Battery:
    def __init__(self,battery_size=40):
        self.battery=battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery}-kWh battery.")
    def get_range(self):
        if self.battery==40:
            range=150
        elif self.battery==65:
            range=225
        print(f"This car can go about {range} miles on a full charge.")

# 基于父类Car定义一个子类ElectricCar
class ElectricCar(Car):
    # 利用super()方法实现初始化
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        # 添加新的attribute：battery_size
        self.battery=Battery()

my_leaf=ElectricCar('nassan','leaf',2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

