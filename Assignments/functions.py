# recreate mean, count, index function on your own using loops
def mean(x):
    if len(x) == 0:
        return 0 
    total = 0
    for number in x:
        total += number
    return round(total / len(x),2)

def count(x, value):
    count = 0
    for item in x:
        if item == value:
            count += 1
    return count

def index(x, value):
    for i in range(len(x)):
        if x[i] == value:
            return i
    return (f"{value} is not in list")


numbers = list(map(int,input().split()))
print("Mean:", mean(numbers))
x=int(input("enter x: "))
print(f"Count of {x}:", count(numbers, x)) 

print(f"Index of {x}:", index(numbers, x))  
