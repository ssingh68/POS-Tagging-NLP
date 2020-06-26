# =============================================================================
# #Programming Assignment 2 - POS Tagging
# 
# #Team Members - Abhishek Shambhu , Jeyamurugan Krishnakumar & Shreyans Singh
#
# #Team Name - TeamBots
#
# #Steps on how to run the program:
# Step 1: We need to go to the Windows Command Prompt and type the following command
# $ python tagger.py pos-train.txt pos-test.txt
# This will run the tagger.py program which takes 2 files as input and gives output
# in pos-test-with-tags.txt file which includes tags assigned to the words in test file.
#
# Step 2: We need to type the following command to access the scorer.py in cmd prompt-
# $ python scorer.py pos-test-with-tags.txt pos-test-key.txt 
# This will run the scorer.py program which takes 2 files as input and gives output
# in pos-taggingreport.txt file which includes confusion matrix and accuracy of the actual 
# vs predicted tags.
#
# Step 3:Run time for both the programs were recorded and the output was taken in
# tagger-log.txt along with the pos-test-with-tags.txt(first 100 lines), confusion matrix
# and Accuracy of the program.
#
# =============================================================================

#Importing necessary libraries
import nltk 
import sys
import time
from nltk.tag.util import str2tuple

#Measuring Runtime using time package
start=time.time()

#Taking two arguements from Command Prompt where one would be the pos-train.txt file and the other would be pos-test.txt file
train=sys.argv[1]
test=sys.argv[2]

#Opening both files
file_train = open(train,'r')
file_test = open(test,'r')

#Reading the pos-test-with-tags.txt file and perform splitting
trainfile = file_train.read()
train_list = trainfile.split()

#Removing square brackets
if '[' in train_list:
    train_list = list(filter(('[').__ne__, train_list))
if ']' in train_list:
    train_list = list(filter((']').__ne__, train_list))

#Initializing list, creating tuple from string and appending in a
#Dictionaries are created for the training dataset in order to ease data manipulation.
a=[]
for i in train_list:
    if "|" in str2tuple(i)[1]:
        temp=str2tuple(i)
        a.append((temp[0],temp[1].split("|")[0]))
    else:
        a.append(str2tuple(i))
        dict(a)

#Looking out for the most frequent tag and assigning it to the word
cfd = nltk.ConditionalFreqDist(a[:])
likely_tag = dict((word, cfd[word].max()) for word in dict(a))

testfile =dict()

##Reading the pos-test.txt file and perform splitting
testfile = file_test.read().split()

#Removing square brackets
if '[' in testfile:
    testfile = list(filter(('[').__ne__, testfile))  
if ']' in testfile:
    testfile = list(filter((']').__ne__, testfile))

#Creating a list test_list
test_list=[]
#The below loops indicate the 5 rules that we are defining in order to improve the tagger accuracy.
#This helps us to improve the accuracy a little bit compared to previous model using rule defined tags   

#Finding words ending in ly and last but one words, last but two words, last but three words are classified as
for i in testfile:  
    if i in likely_tag:
        test_list.append(i+"/"+likely_tag[i])
#Finding words ending in ly - last but 1 word and assigning tag as RB
    elif i[-2:] == 'ly':
        test_list.append(i+"/"+'RB')
#Finding words ending in  - last but 2nd word and assigning tag as VBG
    elif i[-3:] == 'ing':
        test_list.append(i+"/"+'VBG')
#Finding words ending in ness - last but 3rd word and assigning tag as NN
    elif i[-4:] == 'ness':
        test_list.append(i+"/"+'NN')
#Finding words ending in ed - last but 2nd word and assigning tag as VBN
    elif i[-2:] == 'ed':
        test_list.append(i+"/"+'VBN')
#Rest of them are default tagged as Noun
    else:        
        test_list.append(i+"/"+'NN')        
        
#Creating file and writing into it
with open('pos-test-with-tags.txt', 'w') as f:
    for item in test_list:
        f.write("%s\n" % item)
 
#To check for Runtime of the tagger.py file where end denotes the end time of the Program    
end=time.time()

#To check for total time taken for tagger.py for running
runtime=end-start

#Printing tagger runtime
print("Tagger Runtime:" +str(runtime))