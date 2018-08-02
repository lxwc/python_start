age = 12
if age >= 18:
	print('your age is',age)
	print('adult')
else:
	print('your age is',age)
	print('teenager')
	
if age >= 18:
	print('adult')
elif age >= 6:   #elif  is  else if  abbreviation
	print('teenager')
else:
	print('kid')
	
	
height = input("Please input your height:")

if int(height) >= 180:
	print('tall,high')
elif int(height) >=170:
	print('normal')
else :
	print('low,short')
	
h = 1.75
w = 80.5
BMI = float(w/(h*h))
print('BMI=',BMI)
if BMI <= 18.5:
	print('under weight')
elif BMI<=25:
	print('normal')
elif BMI<=28:
	print('over weight')
elif BMI<=32:
	print('obesity,fat')
else :
	print('severe obesity');