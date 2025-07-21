def second(numbers):
    unique=list(set(numbers))
    if len(unique) < 2:
        return "their is no second largest"
    unique.sort()
    return unique[-2]
arr = list(map(int,input("enter the numbers: ").split()))
result = second(arr)
print(result)