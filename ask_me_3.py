name = input("What is your awesome name? ")
name = name.title()
print("Hello," , name)

if name == "Jack" or name == "Jackie":
    print("Hello, ", name)
    print("Goodbye," , name)
else:
    print("Hello, friend!!!")

age = int(input("How old are you please? "))
if age < 18:
    print("Your are below the age of working.")
elif age > 18 and age < 25:
    print("You are in a job-seeking age.")
elif age > 25 and age < 30:
    print("You should be having a job already.")
elif age > 30 and age < 60:
    print("You should think about having a family.")
elif age > 90 and age < 60:
    print("You should retire!!")
else:
    print("Goodbye,", name)
    print("You are" , age , "years old.")
    print("You are an alien in nature.")





