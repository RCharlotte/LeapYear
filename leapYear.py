from ast import Break
import datetime


date= datetime.date.today()
year= date.strftime("%Y")



def printLeap():
    print(f' {year} is a leap year')
def printNotLeap():
    print(f' {year} is not a leap year')



if int(year) %4 == 0:
    if int(year) %100 == 0:
        if int(year) %400 == 0:
            printLeap()
        else:
            printNotLeap()
    else:
        printLeap()
else:
    printNotLeap()       
        
    
