a=[1,2,[3,4,5,6],7,8]
i=0
while i<len(a):
    b=a[i]
    if type(b) is list:
        j=0
        while j<len(b):
            sum=sum+b[j]
            j+=1
        else:
            sum=sum+a[i]
        i+=1
print(sum)