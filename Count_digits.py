n = -321
rev = 0
num = 0
if(n<0):
     n=-n    #-123 becomes 123
     num = 1

while(n>0):
    digit = n%10
    rev = rev*10 + digit
    n = n//10


if(num==1):
    rev = -rev
    print(rev)
    exit()

print(rev)