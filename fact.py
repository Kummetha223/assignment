def factrec(num):
	if(num==1 or num==0):
		return 1
	else:	
		return (num*factrec(num-1))
print("enter the number to find factorail")
num=int(input("enter the number"))
print("factorail",factrec(num))
