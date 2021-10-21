user=(input("enter user name :"))
string=list(user)
vovel=['a','e','i','o','u']
# string.sort()
for i in string:
    if i in vovel:
        # vovel.sort()
        print(i,"vovel")
    elif i not in  vovel:
        print(i,"comnsonents")