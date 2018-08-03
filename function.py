def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bas operand type')
	if x >=0:
		return x
	else:
		return -x
print(my_abs(-99))

############pass##################3

def nop():
	pass
	

import math

def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx,ny

x,y=move(100,100,60,math.pi/6)
#python -m pip install -U pylint --user
print(x,y)


####################arguments########################
def power(x):
	if not isinstance(x,(int,float)):
		return 'Please input number!'
	return x*x

print(power(5))

print(power('11ss'))

def power3(x,n):
	s=1
	if not isinstance(x,(int,float)):
		return x+' is not a number'
	if not isinstance(n,(int,float)):
		return n + ' is not a number'
	while n>0:
		n = n -1
		s=s*x
	return s

print(power3(2,2))

#########default arguments########
def powerD(x,n=2):
	s = 1
	if not isinstance(x,(int,float)):
		return x + 'is not a number'
	if not isinstance(n,(int, float)):
		return n + 'is not a number'
	while n>0:
		n = n-1
		s = s * x
	return s

print(powerD(5))
print(powerD(5,6))

def enroll(name,sex,age='7',city='BeiJing'):
	print('name:',name)
	print('sex:',sex)
	print('age:',age)
	print('city:',city)

enroll('zhangsan','M','6')
enroll('lisi','F',city='shanghai')

def per(name,age,*,city,job):
	print(name,age,city,job)

per('Jack',24,city='BeiJing',job='Engineer')

def pp(a,b,c=0,*arg,**kw):
	print('a=',a,'b=',b,'c=',c,'arg=',arg,'kw=',kw)

pp('a','b','c','d','e',vv='qq')