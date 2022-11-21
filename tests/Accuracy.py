import pandas as pd

name = ''

corpus = pd.read_csv("{}.csv".format(name)).iloc[1:, -1]
test = pd.read_csv("{} result.csv".format(name)).iloc[1:, -1]

count = 0

for i in range(len(corpus)):
    if corpus[i] == test[i]:
        count+=1
        
print('Accuray = ', count/len(corpus))