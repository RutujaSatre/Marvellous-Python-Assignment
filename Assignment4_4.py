# write program which contains filter(),map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user . Filter should filter all such numbers which are even. Map function will calculate its square,Reduce will return addition of all that numbers.

from functools import reduce

CheckEven= lambda no:(no%2==0)
square= lambda no:no**2
Sum= lambda A,B:A+B
  

def filterX(Task,values):
    Result=[]
    for no in values:
        Ret=Task(no)
        if(Ret==True):
            Result.append(no)

    return Result

def mapX(Task,values):
    Result=[]
    for no in values:
        Ret=Task(no)
        Result.append(Ret)

    return Result

def reduceX(Task,values):
    Result=0
    
    for no in values:
        Result=Task(Result,no)

    return Result

def main():

    Data=[]
    print("Enter no of elements: ")
    Size=int(input())

    print("PLease enter numeric values: ")
    for i in range(Size):
        no=int(input())
        Data.append(no)

    print("Input Data: ",Data)

    FData=list(filterX(CheckEven,Data))
    print("Filter Output: ",FData)

    MData=list(mapX(square,FData))
    print("Map Output: ",MData)

    RData=reduceX(sum,MData)
    print("Reduce Output: ",RData)

if __name__=="__main__":
    main()