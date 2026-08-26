
prime = []
p = int(input("Enter a number:"))
print(p)
for i in range(2,p+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        prime.append(i)

print(prime)
#as the else syntax is written after loop it will work only if loop is competly executed and not broken by (in this case) break 
