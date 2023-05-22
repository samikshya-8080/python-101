# # we have a function called input this function takes input from the user
# # using console/terminal

# # the default type that the function outputs is string..


# # we can use that but it is  not always good to use string or usecases might differ based on the situation


# # console/terminal the black box
# # shortcut key ctrl+~


# # first_name holds value given by the user from the console
# # input function takes input from the user
# # \t is used for design purposes only or formatting
# first_name = input("please enter your first name:\t")

# # print function shows output to console
# print(first_name)

# # to run this code press f5

# # here we are using string interpolation so this basically means we are injecting value 
# # of variables into the string, {} will replace the value that is passed inside 
# # .fromat(first_name) 
# # first_name -> holds the user input
# # print("how are you {}?".format(first_name))

# # adding two numbers using user input
# # we failed cuz expectation was 3+3 = 6 but we got 3+3 = 33
# # adding two strings will just add then or append(add but just glue it example line no 31. end) 
# # them so to add two numbers it should always be either interger or decimal
# # we call then int or float in python

# # to fix this issue we need to convert string to int or float (not done today)
# # we are just taking two numbers so we need to use int (not done today)
 

# # we haven't changed the input type so as a result we are still getting string (not done today)
# first_number:int =  input("please enter first number: ")

# # More explanation how python works and how variable is understood by python while running code..

# # python is dynamic language meaning it will determine the data type (int,float,str.. etc) on runtime (while running code)
# # though we had changed the data type (first_number:int)

# # to check the data type on runtime we can use type(value) -> value can be replaced by the variable name that you want to check
# # this functiona will show us what type did python understood while running the code
# print("the data type that i have understood is {}".format(type(first_number)))

# # <class 'str'> 
# # explanation is in line no. 4 to line no. 7

# # more explanation why it didn't performed as expection....

# # <class 'str'>  means python understood it as string 
# # meaning 43+33 = 4333

# # to solve this issue we need to convert the data type to our prefered type
# # i.e. wrap with the data type we want.

# # here we are first taking string and then converting to our prefered type i.e int
# # only int and int can be added
# # only float and float can be added
# # only string and string can be added
# # will it work now? Let's see through example:
# new_expected_int_number:int = int(input("please enter the number:\t"))
# second_expected_int_number:int = int(input("please enter the number:\t"))
# # same thing goes for float so wrap it with float instead of int

# print(new_expected_int_number+second_expected_int_number)
# # example;02
new_expected_float_number:float = float(input("please enter the number:\t"))
second_expected_float_number:float = float(input("please enter the number:\t"))

print(new_expected_float_number+second_expected_float_number)