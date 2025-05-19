# write program which contains filter(),map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user . Filter should filter all prime numbers. Map function will multiply each number by 2,Reduce will return maximum number from that numbers.

from functools import reduce

def CheckPrime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

Mult= lambda no: no*2
Max= lambda  A, B: A + B
  

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

    FData=list(filterX(CheckPrime,Data))
    print("Filter Output: ",FData)

    MData=list(mapX(Mult,FData))
    print("Map Output: ",MData)

    RData=reduceX(Max,MData)
    print("Reduce Output: ",RData)

if __name__=="__main__":
    main()
