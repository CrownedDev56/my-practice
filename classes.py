# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create Class
class User:
     # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
  
    
    def has_birthday(self):
        self.age +=1

    def greeting(self):
        return f'My name is {self.name} and i am {self.age}'


# Customer C;lass
class Customer(User):
  def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

  def set_balance(self, balance):
      self.balance = balance  

  def greeting(self):
      return f'My name is {self.name} and i am {self.age} and i owe a balance of {self.balance}'

    



# Init user objecr
brad = User('Brad', 'test@test.com', 25)
janet = User('Janet Williams', 'test2@test.com', 30)

# Edit property

brad.age = 26

janet.has_birthday


# Call method
print(janet.greeting())

# Init customer

john = Customer('John Doe','Johan@gmail.com', 40)

john.set_balance(500)

print(john.greeting())