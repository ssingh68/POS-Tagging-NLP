##Importing necessary libraries
import nltk 
from sklearn.metrics import accuracy_score
import sys
from nltk.tag.util import str2tuple
from nltk.metrics import ConfusionMatrix
import time

#To check for Runtime of the scorer.py file where start denotes the start time of the Program
start=time.time()

#Taking two arguements from Command Prompt where one would be the pos-test-with-tags.txt file and the other would be pos-test-key.txt file
testtagged=sys.argv[1]
testkey=sys.argv[2]

#Opening both files
file_testwithtags = open(testtagged,'r')
file_key = open(testkey,'r')

#file_testwithtags = open(r"C:\Users\shrey\Desktop\pos-test-with-tags.txt")

#Reading the pos-test-with-tags.txt file and perform splitting
taggedtestfile = file_testwithtags.read()
taggedtest = taggedtestfile.split()

#Initializing list, creating tuple from string and appending in a
a=[]
for i in taggedtest:
    a.append(str2tuple(i))

#file_key = open(r"C:/Users/shrey/Desktop/George Mason University/Sem 2/AIT 690/Assignment/PA2/pos-test-key.txt")

##Reading the pos-test-key.txt file and perform splitting
testfile = file_key.read().split()

#Removing square brackets
if '[' in testfile:
    testfile = list(filter(('[').__ne__, testfile))   
if ']' in testfile:
    testfile = list(filter((']').__ne__, testfile))

#Initializing list, creating tuple from string and appending in b
b=[]
for j in testfile:
    if "|" in str2tuple(j)[1]:
        temp=str2tuple(j)
        b.append((temp[0],temp[1].split("|")[0]))
    else:
        b.append(str2tuple(j))

#Creating a list of predicted and actual and appending tags from a and b
predicted=[]
for i in a:
    predicted.append(i[1])
actual=[]
for i in b:
    actual.append(i[1])
    
#Creating Confusion Matrix
matrix = ConfusionMatrix(predicted,actual)
print("Confusion Matrix")
print(matrix)

#Check for Accuracy
print("Accuracy: " +str(accuracy_score(actual,predicted)))   

#Writing Confusion Matrix to pos-taggingreport.txt file
with open('pos-taggingreport.txt', 'w') as f:
    #Writing to file
    f.write("Confusion Matrix: "+str(matrix))
    f.write("Accuracy: "+str(accuracy_score(actual,predicted)))             ##Accuracy: 0.8485675066873152

#To check for Runtime of the scorer.py file where end denotes the end time of the Program
end=time.time()

#To check for total time taken for scorer.py for running
runtime=end-start

#Printing scorer runtime
print("Scorer Runtime: " +str(runtime))


