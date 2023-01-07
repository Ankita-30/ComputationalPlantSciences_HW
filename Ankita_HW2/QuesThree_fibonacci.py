def fib(n):

	if n==0:
		return 0

	elif n==1:
		return 1

	else:
		return fib(n-1) + fib(n-2)

i=0
print "Output: "

while i<=100:

	print fib(i)
	i=i+1





