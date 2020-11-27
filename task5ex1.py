num1=int(input("enter the input one:"))
num2=int(input("enter the input two:"))
print("Enter your choice:")
ch=input("Enter an operator :")
result=0
if ch=='+':
    result=num1+num2
elif ch=='-':
     result=num1-num2
elif ch=='*':
    result=num1*num2
elif ch=='/':
     result=num1/num2
else:
    print("invalid");
print(num1,ch,num2,":",result)