'''Number of toys
Akshay has a number of toys and he decided to donate some of them to 
an NGO. After 
the donation, he still has some toys left. Write a program to 
help Akshay to determine 
the number of remaining toys.
Example:
Input: 50 45
Output: The remaining number of toys = 5
Input: 60 6
Output: The remaining number of toys = 54'''
x,y,n=map(int,input().split())
lis = []
def donition(heHave,Requred,divi):
    reminder = heHave%Requred
    howmany = heHave//divi
    borrow = divi-reminder
    if reminder == 0:
        lis.append(howmany*n)