'''
Assignment No: 4
To simulate simple calculator that performs basic tasks such as,
addition, 
subtraction,
multiplication and division. 
'''

def add(x, y):		# function definition of addition
   return x + y

def subtract(x, y):	# function definition of subtraction
   return x - y

def multiply(x, y):	# function definition multiplication
   return x * y

def divide(x, y):		# function definition of divide
   return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
# Take input from the user 
choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Enter numbers as integers")
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '3':
   print(num1,"/",num2,"=", divide(num1,num2))
		elif choice == '4':
		   print(num1,"/",num2,"=", divide(num1,num2))
		else:
		   print("Invalid input")

if __name__ == '__main__':
	main()


