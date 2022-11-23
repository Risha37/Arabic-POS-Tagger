# Import Module
import os
  
# Folder Path
path = r"~\corpus_posttag"
  
# Change the directory
os.chdir(path)
  
# Read text File
  
x = []
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        f1 = f.readlines()
        for ele in f1:
            x.append(ele.rstrip())
  

# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"
  
        # call read text file function
        read_text_file(file_path)
        
        
        
        
y = {}
for i in range(len(x)):
    y[str(x[i].split('/')[0])] = str(x[i].split('/')[1])
    
    
    
    
import string
ignoreList = (list(string.punctuation) + list(string.ascii_letters) +
                      '''ﷺ 1 2 3 4 5 6 7 8 9 0 ٠ ١ ٢ ٣ ٤ ٥ ٦ ٧ ٨ ٩ ؟ …  ٰ ﴿ ﴾ ، " ' ” “ ·  ۛ  ۗ  ۚ  ۙ  ۖ ؛ ‘ ـ'''.split())
new_y = {}

for i in y.items():
    if i[0] not in ignoreList and i[1] != 'CD':
        new_y[str(i[0])] = str(i[1])
        
        
        
        

import pandas as pd

df1 = pd.DataFrame.from_dict(new_y.keys())
df2 = pd.DataFrame.from_dict(new_y.values())

df = pd.DataFrame(columns= ['Word','Tag'])
df['Word'] = df1
df['Tag'] = df2
df.to_csv('out'+' result.csv', encoding='utf-8-sig')