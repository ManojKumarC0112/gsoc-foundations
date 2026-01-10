#task 1.1
# alist=[1,2,3,4,5]
# atuple=(1,2,3,4,5)
# alist[0]=0
# #atuple[0]=0 this does not work because tuple is immutable and give typeError when we try to change it


#task 2.1
# students={"A":85,"B":72,"C":90}
# maximum=0
# for key in students:
#     print("",key,":",students[key])
#     if students[key] > maximum:
#         maximum = students[key]
#         addr=key
# print(addr,"scored the highest with marks of",maximum)


# #task 3.1
# numbers=[1,2,2,3,4,4,5]
# no_dup=(set(numbers))
# new_numbers=list(no_dup)
# print(new_numbers) # this would be useful when we want to remove the duplicates



#task 4.1
users={
    "manoj":"1234",
    "admin":"admin"
}

username=input("enter username:")
password=input("enter password:")
if username in users:
    if password==users[username]:
        print("login successful")
    else:
        print("invalid password")
else:
    print("invalid username")
