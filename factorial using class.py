class room:
        VALUE1=0
        def factorial(self):
                VALUE1=int(input("enter the number: "))
                fact=1
                i=1
                while i<=VALUE1:
                        fact=fact*i
                        i=i+1
                print("factorial is: ",fact)
obj=room()
print(obj.VALUE1)
obj.factorial()
