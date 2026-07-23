#WAP to find the largest of three numbers.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a>b and a>c:
    largest = a
elif b>a and b>c:
    largest = b
else:
    largest = c
print("Largest among three is :",largest)

#WAP to check whether a number is odd or even
a = int(input("Enter a number: "))
if a%2 == 0:
    print("Even number.")
else:
    print("Odd number")

#WAP to swap two numbers without using third variable.
a = int(input("Enter a number:"))
b= int(input("Enter another number: "))
a= a+b
b =a-b
a=a+b
print("After swapping a:",a,"b:",b)

#WAPto check whether a string is palindrome
a = input("Enter a string:")
rev = ""
for i in range(len(a)-1,-1,-1):
    rev= rev+a[i]
    if a== rev:
        print("Palindrome")
    else:
        print("Not a palindrome")

#WAP to implement a simple calculator:
a = int(input("Enter a number:"))
b = int(input("Enter another number: "))
op = input("Enter an operator(+,-*,/) : ")
if op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '*':
    print(a*b)
elif op == '/':
    print(a/b)
else:
    print("Invalid")

#WAP to count vowels in a string;
a= input("Enter a string: ")
count = 0
for ch in a:
    if ch in "aeiouAEIOU":
        count = count+1
        print("Number of vowels are:  ",count)

#WAP to check a number is prime.
a = int(input("Enter a number: "))
if a>2:
    print("Not prime")
else:
    for i in range(2,a):
        if a%i == 0:
            print("Not prime")
        else:
            print("Prime")

#WAP to find the sum of a number.
a = int(input("Enter a number  : "))
sum = 0
while a>0:
    digit = n%10
    sum = sum+digit
    n = n//10
    print("Sum is : ",sum)

#WAP to reverse a nnumber.
a = int(input("Enter a number: "))
rev =0 
while n>0:
    digit = n%10
    rev = rev*10+digit
    n = n//10
    print ("Reverse is:  ",rev)

#WAP to check the factorial of a number.
a = int(input("Enter a number: "))
fact =1
for i in range(1,n+1):
    fact= fact*i
    print("Factorial is : ",fact)
