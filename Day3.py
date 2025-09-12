def reversenumber(n):
    flag = 0
    rev = 0
    if(n<0):
        n = -n
        flag = 1

    while(n>0):
        digit = n%10
        rev = rev*10 + digit
        n//=10

    if(flag==1):
        rev = -rev

    return rev

n = int(input("Enter the number: "))
reversed_num = reversenumber(n)
print(reversed_num)


if(n==reversed_num):
    print(n , "Is Palindrome")

else: print(n , "is not palidrome")
