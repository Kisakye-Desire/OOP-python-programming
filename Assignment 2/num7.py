

birth_year=2001
def calculateAge(birth_year,name,weight):
    today = 2022
    age = today - birth_year
    print("your age is:", age)
    return age

name =  str(input("what is your name"))
if name =='':
    #adds Desire as defalt name
    name = "Desire"  
             
weight = int(input("what is  your weight"))
print(calculateAge(birth_year, name, weight))
print("your name is", name, "your  weight is", weight )