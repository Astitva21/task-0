def process_list(numbers):
    
    num = []
    result = []

    n = int(input("Enter the number of elements in list:"))
    for i in range (0,n):
        a = int(input("Enter the element of list"))
        num.append(a)


    #new list
    result = num.copy()
    print(result)


    #removal of negatives
    for i in result:
        if i < 0:
            result.remove(i)
    #specifically written two times due to an issue when two negative appear one after other
    for i in result:
        if i < 0:
            result.remove(i)


    result.append(0)
    result.sort()
    print(result)
