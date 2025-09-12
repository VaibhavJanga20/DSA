n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

l1 = []
l2 = []

for i in range(1,n1//2 + 1):
    if(n1%i==0):
        l1.append(i)


for j in range(1,n2//2 + 1):
    if(n2%j==0):
        l2.append(j)


#print(l1)
#print(l2)


set1 = set(l1)
set2 = set(l2)

final_set = set1 & set2

#print(final_set)

print(list(final_set)[-1])
