
#number allocation
n = int(input("Enter the number of numbers:"))
num = [int(x) for x in input("Enter numbers: ").split()]


#for sum of numbers
sum = 0
for i in range(0,n):
    sum += num[i]
print(f"Sum is :",sum)


#for maximum
max = 0
for i in range(0,n):
    if max < num[i]:
        max = num[i]
print(f"Max is:",max)


#for minimum
min = max
for i in range(0,n):
    if min > num[i]:
        min = num[i]
print(f"Min is:",min)


#for number of even and odd
even = 0
odd = 0
for i in range(0,n):
    if num[i]%2 == 0:
        even+=1
    else:
        odd+=1
print(f"Number of odd numbers:",odd)
print(f"Number of even numbers:",even)


#revrse of list
num.reverse()
print(*num)
