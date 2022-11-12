import pandas as pd

corpus = pd.read_csv("yasma'oon hasisaha.csv").iloc[:, -1]
test = pd.read_csv("yasma'oon hasisaha Test.csv").iloc[:, -1]

count =0

for i in range(len(corpus)):
    if corpus[i] == test[i]:
        count+=1
        
print(count/len(corpus))