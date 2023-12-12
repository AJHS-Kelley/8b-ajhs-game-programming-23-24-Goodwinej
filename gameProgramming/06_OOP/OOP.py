# object-oriented Programming, Jermya Goodwine, V0.0

class Person: #USE PASCALCASE for ClassName
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.weakness = None
        self.nemesis = None

    # To string Function -- HOw the object appears as a string
    def __str__(self):
        return f"Name: {self.name}\nthis person is {self.age} years old\nand weighs {self.weight} pounds.\n"
    def classFunction(self):
        print("this is and example class function.\n")
        print('It only works when called on an object of that class.\n')

person1 = Person("jermya", 16, 115.6)
person2 = Person("mcGriddle",75, 365.5)
# print (person1)  
# print (person2)

# if person1.weight > person2.weight:
#     print(f"{person1.name} weighs more than that {person2.name}\n")
# elif person1.weight == person2.weight:
#     print(f"{person1.name} and {person2.name} weigh the same.\n")
# else:
#     print (f'{person1.name} weighs less than {person2.name}')       

# if person1.age > person2.age:
#     print(f"{person1.name} is older than {person2.name}\n")
# elif person1.age == person2.age:
#     print(f"{person1.name} and {person2.name} are the same age.\n")
# else:
#     print (f'{person1.name} is younger than {person2.name}')           

# person1.classFunction()


#Changingg Properties After Creation
person1.name = "TURTLE MAN"
print(person1.name)

# Deleting properties -- DANGER WILL ROBINSON, DANGER!
# THIS DOES NOT "RESET A PROPERTY, IT COMPLETELY GET RID OF IT.
print(person1.name)
del person1.weight
# print (person1)

# Deleting Obects -- delete them when you're completely done with it!
del person1

# Adding Properties to objects
person2.weakness = 'kryptonite'
print(person2)
print (person2.weakness)