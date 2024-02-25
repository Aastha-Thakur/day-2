# print("Hello"[0]) #subscripting
# print("Hello"[4])
# #data types
# #integer

# print(123 + 345)

# #float

# 3.14159

# #boolean
# True
# False

#strings and integers cannot be concatenated
# num_char = len(input("What is your name?"))
# print("Your name is" + num_char + "Characters")
#error
#solution
#print(type(len(input("What is your name?"))))#checking data type

# #type casting or type conversion
# num_char = len(input("What is your name?"))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " Characters")

# a = float(123)
# print(type(a))
# print(70 + float("100.5"))
# print(str(70) + str(100))

# print(39)
# print(3 + 9)

# two_digit_number = input()

# first_digit_number = int(two_digit_number[0])
# second_digit_number = int(two_digit_number[1])

# two_digit_number = first_digit_number + second_digit_number
# print(two_digit_number)

#mathematical operations
# print(2 ** 3) #exponet
# PEMDAS
# ()
# **
# */
# +-

# print(3 * 3 + 3 / 3 - 3)
# print(3 *(3 + 3) / 3 - 3)

#calculate body mass index


# weight = input()
# height = input()
# # #converting weight to whole number integer type and height to float type
# weight_as_int = int(weight)
# height_as_float = float(height)
# bmi = weight_as_int / height_as_float ** 2
# bmi_as_int = int(bmi)
# print(bmi_as_int)

# #number manipulation and f string
# print(round(8 / 3, 2))
# print(type(8//3))
# result = 4/2
# result /= 2
# print(result)

# score = 0
# #user scores a point
# score += 1
# print(score)
# similarly -=, *=, /=
# score = 0
# height = 1.8
# iswinning = True
# #f-string, to concatinate different data types without changing each
# print(f"your score is {score}, your height is {height}, you are winning is {iswinning} ")
# #your life in weeks blog, 4000 weeks
# #how many weeks in a persons life when we know their age
# age = input()
# years = 90 - int(age)#how many years left
# weeks = years*52 #52 weeks in a year
# print(f"you have {weeks} left.")

# #tip calculator 
#if the bill was $150.00, split between 5 people, with 12% tip.
#each person should pay (150.00/5)*1.12
#round the result to 2
# print("Welcome to the tip calculator")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10, 12"))
# members = int(input("How many people to split the bill?"))
# payment = tip / 100 * bill + bill
# bill_per_person = payment / members
# final_amount = (round(bill_per_person,2))
# final_amount = "{:.2f}".format(bill_per_person) #formatting for 2 decimal places
# print(f"Each person should pay {final_amount}, $")
                           # LOVE CALCULATOR
name1 = input()
name2 = input()

combined_names = name1 + name2
lower_name = combined_names.lower()
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
first_digit = t + r + u + e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if(score<10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos")
elif (score>=40) or (score <= 50):
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}.")
