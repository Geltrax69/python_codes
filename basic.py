# print("Hello, World!")
# print("This is a basic Python script.")
# print("It demonstrates simple print statements.")
# print("You can run this script to see the output.")
# print("Feel free to modify and expand upon it!")
# print("Happy coding!")
# print("Goodbye, World!")
# print("End of the script.")

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# sum = a+b
# print("The sum is: " + str(sum))


# i=int(input("Enter integer: "))
# f=float(input("Enter float: "))
# s=input("Enter string: ")
# b=bool(int(input("Enter boolean: ")))

# print("String: " + s)
# print("Float: " + str(f))
# print("Integer: " + str(i))
# print("Boolean: " + str(b))

# a=float(input("Enter the number: "))
# area = a*a
# print("The area of the square is: " + str(area)+ " is its right ?")


# #Type Conservation + Type Casting
# a=int(input("Enter integer: "))
# b=float(input("Enter float: "))
# sum = a + b
# print("The sum is: " + str(sum)+ "\nType of sum is: " + str(type(sum)))


# #Type Conservation + Type Casting - Character
# c=str(input("Enter character: "))
# increased_c = chr(ord(c) + 1)
# c = increased_c
# print("The character is: " + str(c)+ "\nType of character is: " + str(type(c)))


# Average of three subjects.

import statistics
# sub1 = float(input("Enter marks of subject 1: "))
# sub2 = float(input("Enter marks of subject 2: "))
# sub3 = float(input("Enter marks of subject 3: "))
# average = (sub1 + sub2 + sub3) / 3
# avg = statistics.mean([sub1, sub2, sub3])
# print("The average marks are: " + str(round(average, 2)))
# print("The average marks using statistics.mean are: " + str(round(avg, 2)))


# # Average of n subjects.
# no = int(input("Enter a no of subject marks you want to input: "))
# marks = []
# for i in range(no):
#     mark = float(input(f"Enter marks of subject {i+1}: "))
#     marks.append(mark)
# average = statistics.mean(marks)
# print("The average marks are: " + str(round(average, 2)))


# Shopping cart n items total cost + gst
# no = int(input("Enter number of items you want to buy: "))
# item_list = []

# total_cost = 0
# for i in range(no):
#     item_list.append(input(f"Enter name of item {i+1}: "))
#     cost = float(input(f"Enter cost of item {i+1}: "))
#     total_cost += cost
# gst = total_cost * 0.18
# final_amount = total_cost + gst
# print("Items you have purchased: " + ",".join(item_list))
# print("The total cost before GST is: " + str(round(total_cost, 2)))
# print("The GST amount is: " + str(round(gst, 2)))
# total_cost = final_amount
# print("The total cost is: " + str(round(total_cost, 2)))


#create a simple calculator with Ui nterface using Tkinter
# import tkinter as tk
# from tkinter import messagebox
# def add():
#     try:
#         num1 = float(entry1.get())
#         num2 = float(entry2.get())
#         result = num1 + num2
#         messagebox.showinfo("Result", f"The sum is: {result}")
#     except ValueError:
#         messagebox.showerror("Error", "Please enter valid numbers.")
# def subtract():
#     try:
#         num1 = float(entry1.get())
#         num2 = float(entry2.get())
#         result = num1 - num2
#         messagebox.showinfo("Result", f"The difference is: {result}")
#     except ValueError:
#         messagebox.showerror("Error", "Please enter valid numbers.")
# def multiply():
#     try:
#         num1 = float(entry1.get())
#         num2 = float(entry2.get())
#         result = num1 * num2
#         messagebox.showinfo("Result", f"The product is: {result}")
#     except ValueError:
#         messagebox.showerror("Error", "Please enter valid numbers.")
# def divide():
#     try:
#         num1 = float(entry1.get())
#         num2 = float(entry2.get())
#         if num2 == 0:
#             messagebox.showerror("Error", "Cannot divide by zero.")
#             return
#         result = num1 / num2
#         messagebox.showinfo("Result", f"The quotient is: {result}")
#     except ValueError:
#         messagebox.showerror("Error", "Please enter valid numbers.")
# root = tk.Tk()
# root.title("Simple Calculator")
# label1 = tk.Label(root, text="Enter first number:")
# label1.pack()
# entry1 = tk.Entry(root)
# entry1.pack()
# label2 = tk.Label(root, text="Enter second number:")
# label2.pack()
# entry2 = tk.Entry(root)
# entry2.pack()
# add_button = tk.Button(root, text="Add", command=add)
# add_button.pack()
# subtract_button = tk.Button(root, text="Subtract", command=subtract)
# subtract_button.pack()
# multiply_button = tk.Button(root, text="Multiply", command=multiply)
# multiply_button.pack()
# divide_button = tk.Button(root, text="Divide", command=divide)
# divide_button.pack()
# root.mainloop()



#make a simple calculator that can perform addition, subtraction, multiplication, and division based on user input.
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# operation = input("Enter operation (+, -, *, /): ")
# if operation == "+":
#     result = a + b
#     print("The sum is: " + str(result))
# elif operation == "-":
#     result = a - b
#     print("The difference is: " + str(result))
# elif operation == "*":
#     result = a * b
#     print("The product is: " + str(result))
# elif operation == "/":
#     if b == 0:
#         print("Error: Cannot divide by zero.")
#     else:
#         result = a / b
#         print("The quotient is: " + str(result))
# else:
#     print("Invalid operation.")


# 3 inputs and find the largest number
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))
# l= a>b and a>c and a or b>c and b or c
# m = max(a, b, c)
# print("The largest number is: " + str(l))
# print("The largest number using max() is: " + str(m))

#ATM Dispenser
# only 500 and 200 notes are available 
# take an amount input from user and
# if amount is dischargable,print Discharable
#else print Dischargeable not available

# amount = int(input("Enter the amount to withdraw: "))
# if amount % 200 == 0 or amount % 500 == 0 or amount % 700 == 0 or amount % 900 == 0:
#     print("Dischargable")
# else:
#     print("Dischargeable not available")


# table of a number
num = int(input("Enter a number to print its table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    