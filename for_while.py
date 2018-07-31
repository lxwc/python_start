####for####

arr = ['lili','haha','bibi']
for x in arr:
	print(x)

sum = 0
for x in range(5):
	print(x)
	
print(list(range(4)))



##########while###########33

sum = 0
n =99
while n> 0:
	sum = sum + n
	n = n - 2
print (sum)

#########break#######3

n=1
while n<= 100:
	if(n>10):
		break
	print(n)
	n=n+1
print('END')

############continue#############
t = 0
while t<100:
	t=t+1
	if t%2==0:
		continue
	print(t)
	
print('END')