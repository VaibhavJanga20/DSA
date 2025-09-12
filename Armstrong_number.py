n = int(input("Enter the number: "))
o_n = n
count = 0
sum = 0
while(n>0):
    digit = n%10
    count+=1
    n=n//10
n = o_n  
while(n>0):
    digit = n%10
    sum = sum + digit**(count)
    n=n//10

if(sum==o_n):
    print("Armstrong number")

else : print("Not an armstrong number")