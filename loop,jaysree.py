user=int(input("enter numb:"))
a=[]
i=1
while i <=user:
    number=(input("enter num:"))
    b=len(number)-2
    c=int(number)//10**b
    d=c%10        
    if d==5:
        a.append(int(number))
    i+=1
print(a)



# a=[9,8,7,6,5,4,3,2,1]
# i=0
# while i<len(a):
#     if a[i]%2!=0:
#         j=0
#         while j<len(a):
#             if a[j]%2!=0:
#                 if a[i]<a[j]:
#                     new=a[i]
#                     a[i]=a[j]
#                     a[j]=new
#             j+=1
# a=["jayshree","rani","rina","kiran"]
# b=[58,49,60,30]
# c={}
# for i in range(len(a)):
#     c.update({a[i]:b[i]})
# print(c)
#     i+=1
# print(a)

# ##dict
# a=["jayshree","rani","rina","kiran"]
# b=[58,49,60,30]
# c={}
# for i in range(len(a)):
#     key=a[i]
#     value=b[i]
#     c.update({key:value})
# print(c)


# a=["jayshree","rani","rina","kiran"]
# b=[58,49,60,30]
# c={}
# for i in range(len(a)):
#     c.update({a[i]:b[i]})
# print(c)