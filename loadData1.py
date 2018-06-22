import csv
from numpy import *

def toInt(array):
    array=mat(array)
    m,n=shape(array)
    print(n)
    newArray=zeros((m,n),int)
    for i in range(m):
        for j in range(n):
                newArray[i,j]=int(array[i,j])
    return newArray

def nomalizing(array):
    m,n=shape(array)
    for i in range(m):
        for j in range(n):
            if array[i,j]!=0:
                array[i,j]=1
    return array

def loadTrainData():
    l=[]
    with open('DataSet/train.csv') as file:
         lines=csv.reader(file)
         for line in lines:
             l.append(line) #42001*785
    l.remove(l[0])
    l=array(l)
    label=l[:,0]
    data=l[:,1:]
    return nomalizing(toInt(data)),toInt(label)
    
def loadTestData():
    l=[]
    with open('DataSet/test.csv') as file:
         lines=csv.reader(file)
         for line in lines:
             l.append(line)#28001*784
    l.remove(l[0])
    data=array(l)
    return nomalizing(toInt(data))  #  data 28000*784
    #return testData
    
def loadTestResult():
    l=[]
    with open('DataSet/sample_submission.csv') as file:
         lines=csv.reader(file)
         for line in lines:
             l.append(line)#28001*2
    l.remove(l[0])
    label=array(l)
    return toInt(label[:,1])  #  label 28000*1
    
def classify(inX, dataSet, labels, k):
    inX=mat(inX)
    dataSet=mat(dataSet)
    labels=mat(labels)
    dataSetSize = dataSet.shape[0]                  
    diffMat = tile(inX, (dataSetSize,1)) - dataSet   
#     sqDiffMat = array(diffMat)**2
#     sqDistances = sqDiffMat.sum(axis=1)  
#     distances = sqDistances**0.5
    distances = linalg.norm(diffMat,ord = 2, axis = 1)
    
    sortedDistIndicies = distances.argsort()            
    classCount={}                                      
    for i in range(k):
        voteIlabel = labels[0,sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.items(), key=lambda item:item[1], reverse=True)
    return sortedClassCount[0][0]
    
#result是结果列表 
#csvName是存放结果的csv文件名
def saveResult(result,csvName):
    with open(csvName,'wb') as myFile:    
        myWriter=csv.writer(myFile)
        for i in result:
            tmp=[]
            tmp.append(i)
            myWriter.writerow(tmp) 
            
def fun():
    x1 = array([1,3,4,4,4,4])
    x1

    classCount = {}
    classCount[5] = 2
    classCount[4] = 4
    print(classCount)
    print(classCount.items())
    sorte = sorted(classCount.items(), key=lambda item:item[1], reverse=True)
    sorte