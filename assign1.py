'''
Assignment No: 1
To calculate salary of an employee given his basic pay (take as input from user). 
Calculate gross salary of employee. Let HRA be 10 % of basic pay and TA be 5% of basic pay. 
Let employee pay professional tax as 2% of total salary. 
Calculate net salary payable after deductions. 
'''
basic_pay = input("Enter your basic pay: ")	
basic_pay = float(basic_pay)
if basic_pay<0:					# basic pay cannot be less than zero 
	print("Basic pay can't be negative.")
	exit()
hra = basic_pay*0.1				# hra is 10 % of basic pay
ta = basic_pay*0.05				# ta is 5 % of basic pay
print("Basic Pay:", basic_pay)
print("HRA:",hra)
print("TA:",ta)
total_salary = basic_pay + hra + ta 		
print("Gross Salary(Total Salary):",total_salary)
p_tax = total_salary*0.02	# professional tax is 2 % of total salary
print("Professional Tax:",p_tax)
salary_payable = total_salary - p_tax
print("Salary Payable(Net Salary):",salary_payable)	


