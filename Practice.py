# ==========================================
# 1. Variables & Formatted Printing
# ==========================================

# Dynamically typed variable assignment
a = 'hello world'  # String variable
print(a)

# Multiple assignment in a single line
a, b = 5, 10

# Formatted printing options
print(a, 'apples')  # Output: 5 apples
print(f"{a} apples, {b} oranges")  # Output using f-string


# ==========================================
# 2. Basic Arithmetic & String Operations
# ==========================================

# Arithmetic Operations
sum_val = 5 + 10      # Addition (+)
diff = 10 - 5         # Subtraction (-)
prod = 5 * 10         # Multiplication (*)
div = 10 / 2          # Division (returns float)
power = 3 ** 5        # Power/Exponentiation (3^5 = 243)
modulus = 6 % 4       # Modulus/Remainder (returns 2)

# String Operations
str_concat = 'hello' + 'UIU'  # String concatenation -> 'helloUIU'
str_repeat = 'helloUIU' * 3   # String repetition -> repeats 3 times


# ==========================================
# 3. Typecasting
# ==========================================

# Converting String to Integer
num_str = '12343'
num_int = int(num_str)  # Converts '12343' to integer 12343

# Converting Integer to String
val = 100
str_val = str(val)
print(str(100) + str(100))  # Output: '100100'


# ==========================================
# 4. Taking User Input
# ==========================================

# Note: Uncomment the lines below to test user input

# Taking string input (default)
# user_str = input("Enter text: ")

# Taking integer input
# user_int = int(input("Enter an integer: "))

# Taking float input
# user_float = float(input("Enter a number: "))


# ==========================================
# 5. Conditional Statements (If-Elif-Else)
# ==========================================

a, b = 20, 5

if a > b:
    print('a is greater than b')
elif a < 100:
    print('a is between 9 and 100')
else:
    print('a is smaller')


# ==========================================
# 6. Loops (For & While)
# ==========================================

# For Loop Examples
print("Range 0 to 9:")
for i in range(10):  # Runs 0 to 9
    print(i, end=" ")
print()

print("Range 1 to 10:")
for i in range(1, 11):  # Runs 1 to 10
    print(i, end=" ")
print()

print("Range with step 2:")
for i in range(0, 10, 2):  # Step size of 2 -> 0, 2, 4, 6, 8
    print(i, end=" ")
print()

# While Loop Example
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1  # Increments by 1 (i++ is NOT supported in Python)


# ==========================================
# 7. Data Structures: Tuple, List & Dictionary
# ==========================================

# --- Tuple (Immutable) ---
my_tuple = (4, 5, 6)

# --- List (Mutable & Heterogeneous) ---
arr = ['apple', 100, 3.4]

# Adding elements
arr.append('orange')   # Appends to the end
arr.insert(1, 560)      # Inserts 560 at index 1

# Deleting elements
arr.pop(1)              # Removes element at index 1
arr.remove('apple')     # Removes specific element by value

# List Slicing
sub_list = arr[0:2]     # Get elements from index 0 to 1
reversed_arr = arr[::-1]  # Reverses the list

# Copying Lists
foo = [1, 2, 3]
bar_shallow = foo.copy()  # Shallow copy

import copy
bar_deep = copy.deepcopy(foo)  # Deep copy

# --- Dictionary (Key-Value Pairs) ---
my_dict = {"name": "osama", "id": 12}
print(f"Name: {my_dict['name']}, ID: {my_dict['id']}")


# ==========================================
# 8. Functions
# ==========================================

# Simple Function
def sum_numbers(a, b):
    return a + b

# Function with Default Parameter
def can_vote(age=0):
    if age >= 18:
        return True
    return False

print("Sum:", sum_numbers(10, 20))
print("Can Vote (Age 20):", can_vote(20))


# ==========================================
# 9. Object-Oriented Programming (OOP)
# ==========================================

class Employee:
    emp_num = 0  # Static / Class Variable

    def __init__(self, first, last, pay):  # Constructor
        self.first = first                  # Instance Variable
        self.last = last
        self.pay = pay
        Employee.emp_num += 1

    def fullname(self):  # Class Method
        return f'{self.first} {self.last}'

# Inheritance (Child Class inheriting from Employee)
class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # Call parent constructor
        self.prog_lang = prog_lang

# Testing OOP Classes
dev_1 = Developer('John', 'Doe', 50000, 'Python')
print("Developer Name:", dev_1.fullname())
print("Programming Language:", dev_1.prog_lang)


# ==========================================
# 10. NumPy Arrays
# ==========================================

import numpy as np

# Creating an Array
np_arr = np.array([3, 6, 7])
print("Array Shape:", np_arr.shape)

# Matrices with Zeros, Ones, and Identity Matrix
zeros_matrix = np.zeros((2, 2))      # 2x2 matrix filled with 0
ones_matrix = np.ones((2, 2))        # 2x2 matrix filled with 1
identity_matrix = np.eye(3)          # 3x3 Identity matrix

# Random Matrix (Integers between 0 and 50)
random_matrix = np.random.randint(0, 50, (4, 5))

print("Random Matrix:\n", random_matrix)