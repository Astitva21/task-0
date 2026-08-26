def process_list(numbers):
    import random
    num = []
    result = []

    n = random.randint(0,10)
    for i in range (0,n):
        a = random.randint(-10,10)
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
