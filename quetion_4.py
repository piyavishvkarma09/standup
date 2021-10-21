# Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# for i in Dict:
#     print(Dict[i])




# dict = ["window","pi","fy","tr"]
# for i of dict:
#     print(i)


# def number(list):
#     # list=[23,45,6,7]
#     i=0
#     max=list[i]
#     while i<len(list):
#         if list[i]>max:
#             max=list[i]
#         i=i+1
#     print("max=",max)
# number([23,45,6,7])

list=[1,2,3,4,5,6,7,8]  #output 8 aa raha hai. jab ki pair ban tha 
i=0
a=[]
while i<len(list):
    b=(list[i-1]==list[-i])
    a.append(b)
    i=i+1
print(i)
        
