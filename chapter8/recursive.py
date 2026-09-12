# recursive function

def sum(n):
    if(n == 1):
        return 1
    return sum(n-1) + n

n = int(input("Enter a number: "))
result = sum(n)
print(result)