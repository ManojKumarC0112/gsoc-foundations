#task 1

# name=input("Enter your name: ")
# age=int(input("enter your age:"))
# print("your name is",name,"and your age next year is",age+1,)

#taske 1.2
# print("using while loop")
# i=1
# while(i<=10):
#     print(i,end=" ")
#     i=i+1
# print("")
# print("using for loop")
# for i in range(1,11):
#     print(i,end=" ")

#task 3
numbers=[1,2,2,3,3,3,4]

freq={}

for n in numbers:
    if n in freq:
        freq[n]=freq[n]+1
    else:
        freq[n]=1

print(freq)