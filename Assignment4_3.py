# write program which contains filter(),map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user . Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10.Reduce will return product of all that numbers

Greater= lambda no:(no>=70 and no<=90)
Increase= lambda no:no+10
Mult= lambda A,B:A*B
  

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

    print("Please enter numeric values: ")
    for i in range(Size):
        no=int(input())
        Data.append(no)

    print("Input Data: ",Data)

    FData=list(filterX(Greater,Data))
    print("Filter Output: ",FData)

    MData=list(mapX(Increase,FData))
    print("Map Output: ",MData)

    RData=reduceX(Mult,MData)
    print("Reduce Output: ",RData)

if __name__=="__main__":
    main()