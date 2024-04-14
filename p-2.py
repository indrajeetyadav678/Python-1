
# def capitalize_each_word(input_str):
#     # Capitalize each word in the string
#     return input_str.title()

# input_string = 'we are one'

# # Output
# output_string = capitalize_each_word(input_string)
# print(output_string)

#================================== Quest - 3 =============================

# def count_occurrences(lst, x):
#     count = 0
#     for num in lst:
#         if num == x:
#             count += 1
#     return count

# lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
# x = 10

# print("Number of occurrences of", x, "in the list:", count_occurrences(lst, x))

#================================== Quest - 4 =============================
# def findname(name):
#     global phonebook
#     if name in phonebook:
#         del phonebook[name]
#         print("Phone number deleted for", name)
#     else:
#         print("Name not found in phonebook")

# # Example phonebook dictionary
# phonebook = {"ajay": 9898989898, "aman": 8787878787, "raj": 9090909090}

# findname("aman")
# print("Updated phonebook:", phonebook)

# ======================== Quest -5 ========================

# def sum_and_avg_of_digits(s):
#     # Initialize variables to store sum and count of digits
#     digit_sum = 0
#     digit_count = 0
#     for char in s:
#         if char.isdigit():
#             digit_sum += int(char)
#             # Increment the count of digits
#             digit_count += 1
#     # Calculate the average of digits
#     if digit_count > 0:
#         avg = digit_sum / digit_count
#     else:
#         avg = 0  # Set avg to 0 if no digits are found
#     return digit_sum, avg
# # Example input
# s = "this is 909 speaking"
# # Calculate sum and average of digits
# sum_of_digits, avg_of_digits = sum_and_avg_of_digits(s)

# # Output
# print("Sum of digits:", sum_of_digits)
# print("Average of digits:", avg_of_digits)

# ======================== Quest -5 ========================

# class Circle:
#     def calculate_area(radius):
#         self.area = 3.14*radius*radius
#         print(area)
    
#     def calculate_circumference(radius):
#         self.circumference = '{:.2f}'.format(2 * 3.14 * radius)
#         print(circumference)

# r=int(input("Enter the radius of circle : "))
# c = Circle
# c.calculate_area(r)
# c.calculate_circumference(r)

# ======================== Quest - 6 ========================

# class Rectangle:
#     def __init__(self, l, w):
#         self.l = l
#         self.w = w

#     def calculate_area(self):
#         self.area = self.l * self.w
#         print("Area:", self.area)

#     def calculate_perimeter(self):
#         self.perimeter = 2 * (self.l + self.w)
#         print("Perimeter:", self.perimeter)

# l = int(input("Enter the length of rectangle : "))
# w = int(input("Enter the width of rectangle : "))

# rect = Rectangle(l, w)

# rect.calculate_area()
# rect.calculate_perimeter()

# ======================== Quest - 8 ========================

# class Person:
#     def __init__(self, name, age, country):
#         self.name = name
#         self.age = age
#         self.country = country

#     def getter(self):
#         return self.name, self.age, self.country
    
#     def change_age(self, new_age):
#         self.age = new_age
#         print(self.name, self.age, self.country)

# P = Person("ram", 34, "india")
# print(P.getter())
# P.change_age(32)

# ======================== question - 9 =======================
class Bank:
    def __init__(self, accountNumber , balance ):
        self.accountNumber = accountNumber
        self.balance = balance
        print(self.balance)

    def withdraw(self, amount ):
        self.balance = self.balance - amount
        print(f"ammount {amount} withdraw successfully")
        print(self.balance)

    def deposite(self, amount):
        self.balance = self.balance + amount
        print(f"ammount {amount} deposite successfully")
        print(self.balance)

b=Bank(1234, 5000)
b.withdraw(2000)
b.deposite(1000)