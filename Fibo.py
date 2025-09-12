n = int(input())    
n1 = 0 
n2 = 1
print(n1)
print(n2)
for i in range(1,n):
    result = n1+n2
    print(result)
    n1 = n2
    n2 = result
