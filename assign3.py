'''
Assignment No: 4
To accept students five courses marks and compute his/her result. 
Student is passing if he/she scores marks equal to and above 40 in each course. 
If student scores aggregate greater than 75%, then the grade is distinction. 
If aggregate is 60>= and <75 then the grade if first division. 
If aggregate is 50>= and <60, then the grade is second division. 
If aggregate is 40>= and <50, then the grade is third division.
'''
print("Program to accept student's five courses marks and compute his or her result")

sub1=int(input('Enter marks of first subject: '))
sub2=int(input('Enter marks of second subject: '))
sub3=int(input('Enter marks of third subject: '))
sub4=int(input('Enter marks of fourth subject: '))
sub5=int(input('Enter marks of fifth subject: '))

if(sub1 and sub2 and sub3 and sub4 and sub5>40):
	print('Student is passed.')
	average=(sub1+sub2+sub3+sub4+sub5)/5
	if average>=75:
		print('Distinction. Congratulations!!!')
	elif average<75 and average>=60:
		print('You have got First division.')
	elif average<60  and average>=50:
		print('You have got Second division.')
	elif average<50 and average>=40:
		print('You have got Third division. Better luck next time!')
else:
	print('You have failed. Extremely sorry.')