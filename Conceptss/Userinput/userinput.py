# In Python, you can take input from the user using the input() function.
# Remember python always takes input as string.


# variable = input("Your message here: ")

name = input("Enter your name: ")
print("Hello, " + name + "!")

# Input an integer

age = int(input("Enter your age: "))
print("Your age is:", age)


#  Input a float:

price = float(input("Enter price: "))
print("Price entered:", price)


#  Input multiple values in one line:

x, y ,p , u = input("Enter four numbers: ").split()


print("X:", x)
print("Y:", y)
print("p:", p)
print("u:", u)