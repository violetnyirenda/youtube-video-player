class car:
    def __init__(self,name,brand,year_made):
        self.name=name
        self.brand=brand
        self.year_made=year_made


    def update_year(self):
        self.year_made=2024

    def update_name(self):
        self.name='jeep'

info=car('c300','mercedes_benz','2022')

info.update_year()

info.update_name()

print(info.name)
print(info.brand)
print(info.year_made)




class student:
    def __init__(self,name,grade,age):
        self.name=name
        self.grade=grade
        self.age=age

info=student('genesis',12,17)

print(info.name)
print(info.grade)
print(info.age)
