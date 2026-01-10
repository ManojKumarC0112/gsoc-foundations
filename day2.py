#task 1.1
def greet(name,age):
    return f"you are {name} you will be {age+1} next year"
print(greet("manoj",20))
print(greet("pari",13))


#task 2.1

def count_even(numbers):
    count = 0
    for n in numbers:
        if n%2==0:
            count=count+1
    return count
print(count_even([1,2,3,4,5,6]))


#task 3.1

with open("data.txt","w") as f:
    f.write("1 2 3 4 5")
    f.close()

with open("data.txt","r") as f:
    for line in f:
        print(line)


