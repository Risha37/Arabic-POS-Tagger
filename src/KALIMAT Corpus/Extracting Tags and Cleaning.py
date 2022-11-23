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
            x.append(ele.strip())
  

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
verb_tags = 'VBD VBP VBN VB'.split()
noun_tags = 'NN NNP JJ DTNN NNS DTJJ DTNNS DTNNP VN VBG JJR DTJJR ADJ_NUM NOUN_QUANT RB DT WP RP PRP DTNNPS'.split()
particle_tags = 'IN WRB CC'.split()

for i in y.items():
    if (i[0] not in ignoreList) and (i[1] not in 'CD PRP$ PUNC'.split()):
        
            if i[1] in verb_tags:
                new_y[str(i[0])] = 'Verb'

            elif i[1] in noun_tags:
                if (i[0].startswith(('ال', 'لل'))) and (str(i[0][2:]) not in new_y):
                    new_y[str(i[0][2:])] = 'Noun'
                elif (i[0].startswith(('كال', 'فال', 'بال', 'وال', 'ولل'))) and (str(i[0][3:]) not in new_y):
                    new_y[str(i[0][3:])] = 'Noun'
                else:
                    new_y[str(i[0])] = 'Noun'

            elif i[1] in particle_tags:
                new_y[str(i[0])] = 'Particle'

            else:
                new_y[str(i[0])] = 'Unknown'
            
            
            
            
            
nouns = ''
verbs = ''
particles = ''
unknown = ''

for i in new_y.items():
    
    if i[1] == 'Verb':
        verbs += str(i[0])+'|'
    elif i[1] == 'Noun':
        nouns += str(i[0])+'|'
    elif i[1] == 'Particle':
        particles += str(i[0])+'|'
    else:
        unknown.join(i[0])
        
        
        

text_file = open("particles.txt", "w", encoding='utf-8-sig')
n = text_file.write(particles)
text_file.close()

text_file = open("verbs.txt", "w", encoding='utf-8-sig')
n = text_file.write(verbs)
text_file.close()

text_file = open("nouns.txt", "w", encoding='utf-8-sig')
n = text_file.write(nouns)
text_file.close()


            
            
            
            
import pandas as pd

df1 = pd.DataFrame.from_dict(new_y.keys())
df2 = pd.DataFrame.from_dict(new_y.values())

df = pd.DataFrame(columns= ['Word','Tag'])
df['Word'] = df1
df['Tag'] = df2
df.to_csv('Cleaned KALIMAT Multipurpose Arabic Corpus.csv', encoding='utf-8-sig')