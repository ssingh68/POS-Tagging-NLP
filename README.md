# POS-Tagging-NLP

### Steps on how to run the program:

Step 1: We need to go to the Windows Command Prompt and type the following command $ python tagger.py pos-train.txt pos-test.txt

This will run the tagger.py program which takes 2 files as input and gives output in pos-test-with-tags.txt file which includes tags assigned to the words in test file.

Step 2: We need to type the following command to access the scorer.py in cmd prompt-$ python scorer.py pos-test-with-tags.txt pos-test-key.txt 

This will run the scorer.py program which takes 2 files as input and gives output in pos-taggingreport.txt file which includes confusion matrix and accuracy of the actual vs predicted tags.

Step 3: Run time for both the programs were recorded and the output was taken in tagger-log.txt along with the pos-test-with-tags.txt(first 100 lines), confusion matrix and Accuracy of the program.

## Achieved overall Accuracy: 0.8517351823173307
