s1=input("enter the string1  ")
s2=input("enter the string2  ")
res1=''.join(sorted(s1))
res2=''.join(sorted(s2))
if(res1.upper()==res2.upper() and len(res1)==len(res2)):
	print("anagram")
else:
	print("not anagram")
