num=int(input("enter the number: "))
reverse=0
while num!=0:
    digit=num%10
    reverse=reverse*10+digit
print(reverse)


num=int(input("enter the number: "))
i=0
while num>0:
    num=num//10              
    i=i+1
print(i)
