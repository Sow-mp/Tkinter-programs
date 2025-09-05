
'''import calendar
mystr=input("enter the string")
words=mystr.split()
words.sort()
for word in words:
    print(word)


# define punctuation
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
# take input from the user
my_str = input("Enter a string: ")
# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuation:
       no_punct = no_punct + char
# display the unpunctuated string
print(no_punct)'''



num1=input("enter the first number")
num2=input("enter the second number")
add=float(num1)+float(num2)
print("addition",add)
# print("addition of "num1 "and" num2 "is" ,add)
# print('The sum of {0} and '.format(num1, num2, add))


a=float(input("enter the first side"))
b=float(input("enter the second side"))
c=float(input("enter the third side"))
s=int(a+b+c)/2
area=float(s*(s-a)*(s-b)*(s-c))**0.5
print("area of triangle",area)

p=input("enter the number")
q=input("enter the number")
temp=p
p=q
q=temp
print("after swapping" ,p ,"and",q)

'''def kilometre_1(km):
    conversion_ratio_1= 0.621371
    miles_1 = km * conversion_ratio_1
    print ("The speed value of car in Miles: ", miles_1)
km = float (input ("Please enter the speed of car in Kilometre as a unit: "))
kilometre_1(km)'''

yy=input("enter the year")
mm=input("enter the month") '''

# print(calendar.month(yy,mm))


def checknum(a):
     if a>0:
        print("given number is +ve num")
     elif a<0:
         print("-ve num")
     else:
         print("zero num ")
a=int(input("enter the number"))
checknum(a)









