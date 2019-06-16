# def greet(): #function definition
#     print("Good morning")
# greet() #function calling
# print("I am outside the function ")
# greet()
# print("Completed")
# 

# def my_pet(owner , pet , city = "Karachi"):
#     print(owner ," is an owner of ", pet , ".They are from ",city)
# my_pet(pet = "Cat" , owner = "Sarah" , city = "Lahore")


# def sum(): #takes nothing return something
#     a = 2
#     b = 3
#     # print("Sum is " (a+b))
#     return (a+b)
# result = sum()
# print(result)

# a = int(input("Enter value 1 "))
# b = int(input("Enter value 2 "))

# def sum(val1, val2): #takes something returns something
#     result = val1+val2
#     return result
# output_of_function = sum(a,b)
# print(output_of_function)

#   ----X---------X--------X-------------X-----------X

# def pizza(crust , *topping):
#     print("You have ordered a pizza with " , crust,"crust and the following toppings :" )
#     for each in topping:
#         print(each)
# pizza("Thick" ,"Green olives","Chicken" , "Black olives")

# def pizza(crust , **topping):
#     print("You have ordered a pizza with " , crust,"crust and the following toppings :" )
#     for key in topping.keys():
#         print(key)
# pizza("Thick", topping1 = "Green olives" , topping2 = "Chicken" , topping3 = "Black olives")

#topping = {topping1 :"Green Olives " , Topping2 = "Chicken"}