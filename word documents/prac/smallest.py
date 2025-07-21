def smallest(numbers):
    unique_numbers=list(set(numbers))
    if len(unique_numbers) < 2:
        return "no second smallest"
    unique_numbers.sort()
    return unique_numbers[1]
arr=list(map(int,input("enter numbers").split()))
result=smallest(arr)
print(result)
