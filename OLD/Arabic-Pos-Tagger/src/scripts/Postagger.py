#    $Author: belal (a.k.a risha) $
#    $Revision: 1.5 $

# import pandas as pd
import KnownTags as kt
import Tokenizer as tok
from itertools import chain


class postagger():
    """
    This class tokenizes a document file and then tags each word in a dictionary.
     Input:
        - document: A document file (.txt preferred) containing the sentences.
    """
    
    def __init__(self, document):
        self.document = document
    
    
    def get_tokens(self):
        """
        Get Tokens: To obtain the tokens, using the Tokenizer class.
         Output:
            - tokens: A list within a list whose indices are one word from each line of the document.
        """
        tokens = tok.tokenizer(self.document).tokenize()
        return tokens
    
    
    def tag(self):
        """
        PosTag: Divide each word into its respective tag (Noun, Verb, Particle) using the provided rules.
         Outputs:
            - tagsList: A list that contains the tags ordered with respect to the word.
            - tags: A dictionary that includes each word and its associated tag.
        """
        tokens = self.get_tokens()
        horoof, asmaa, afaal = kt.knowntags().known_tags()
        
        horoof = list(chain.from_iterable(horoof.values()))
        asmaa = list(chain.from_iterable(asmaa.values()))
        afaal = list(chain.from_iterable(afaal.values()))
        
        tagsFinal = list()
        tagsListFinal = list()
        
        for sentence in tokens:
            tagsList = list()
            tags = dict()
            for word in range(len(sentence)):
                
                
                
                if sentence[word] in horoof:
                    tags[sentence[word]] = 'Particle'
                    tagsList.append('Particle')
                elif sentence[word].startswith(('ب', 'ف', 'ك')) and (sentence[word][1:] in horoof):
                    tags[sentence[word]] = 'Particle'
                    tagsList.append('Particle')
                elif sentence[word].endswith(('ها', 'هم', 'نا', 'ما', 'هن', 'كم', 'كن')) and (sentence[word][:-2] in horoof):
                    tags[sentence[word]] = 'Particle'
                    tagsList.append('Particle')
                elif sentence[word].endswith(('هما', 'تما', 'كما')) and (sentence[word][:-3] in horoof):
                    tags[sentence[word]] = 'Particle'
                    tagsList.append('Particle')
                    
                    
                    
                elif sentence[word].startswith(('ال')) or sentence[word].endswith(('ة', 'ات', 'ائي', 'ائك', 'ائه', 'اؤك', 'اؤه', 'اءك', 'اءه', 'هما', 'كما')):
                    tags[sentence[word]] = 'Noun'
                    tagsList.append('Noun')
                elif len(sentence[word])==5 and (sentence[word].startswith(('م')) and 
                                                (sentence[word][2]=='ا' or sentence[word][-2]=='ي' or 
                                                 sentence[word][-2]=='ا' or sentence[word][2]=='ت' or
                                                 sentence[word][1]=='ن' or sentence[word][-2]=='و' or
                                                 sentence[word][1]=='ت' or sentence[word][-2]=='ل')):
                    tags[sentence[word]] = 'Noun'
                    tagsList.append('Noun')
                elif sentence[word].startswith(('ب', 'ف', 'ك', 'و')) and sentence[word][1:3] == 'ال':
                    tags[sentence[word]] = 'Noun'
                    tagsList.append('Noun')
                    
                    
                    
                elif sentence[word].startswith(('است')) or sentence[word].endswith(('وا', 'ت', 'سي', 'ست', 'سن', 'سأ', 'سا', 'لا', 'لأ', 'لن', 'لت', 'لي')):
                    tags[sentence[word]] = 'Verb'
                    tagsList.append('Verb')
                elif len(sentence[word])==4 and (sentence[word].startswith(('ي', 'أ', 'ت', 'ا')) or 
                                                 sentence[word][1] == 'ا'):
                    tags[sentence[word]] = 'Verb'
                    tagsList.append('Verb')
                elif len(sentence[word])==5 and ((sentence[word].startswith(('ان', 'ت', 'يت'))) or
                                                 (sentence[word].startswith(('ت')) and sentence[word][2]=='ا') or 
                                                 (sentence[word].startswith(('إ', 'ا')) and sentence[word][2]=='ت') or
                                                 (sentence[word].startswith(('ي', 'ن')) and ((sentence[word][2]=='ا') or (sentence[word][-2]=='ا')))):
                    tags[sentence[word]] = 'Verb'
                    tagsList.append('Verb')
                elif len(sentence[word])==6 and ((sentence[word].startswith(('است', 'ي', 'ت'))) or
                                                 (sentence[word].startswith(('ا')) and sentence[word][-3] == 'و')):
                    tags[sentence[word]] = 'Verb'
                    tagsList.append('Verb')
                elif sentence[word].startswith(('ي', 'ن', 'ت', 'ا')) and sentence[word].endswith(('ون', 'ين', 'وا', 'ي', 'تم', 'تن', 'نا', 'ان', 'ها', 'هم', 'هن', 'ه', 'هما')):
                    tags[sentence[word]] = 'Verb'
                    tagsList.append('Verb')
                    
                
                
                
                elif sentence[word] in asmaa:
                    tags[sentence[word]] = 'Noun'
                    tagsList.append('Noun')
                elif sentence[word] in afaal:
                    tags[sentence[word]] = 'Verb'
                    tagsList.append('Verb')
                elif len(sentence[word])==3:
                    tags[sentence[word]] = 'Verb'
                    tagsList.append('Verb')
                    
                
                
#                 elif sentence[word].endswith(('ون', 'ين')):
#                     tags[sentence[word]] = 'Noun'
#                     tagsList.append('Noun')
                else:
                    tags[sentence[word]] = 'Noun'
                    tagsList.append('Noun')
                
                
                
            tagsListFinal += [tagsList]
            tagsFinal.append(list(tags.items()))
        return tagsListFinal, tagsFinal
    
    
    # def save_file(self, name):
    #     """
    #     Save File: Export the tags into a .csv file
    #     """
    #     tagsListFinal, tagsFinal = self.tag()
    #     df = pd.DataFrame(tagsFinal)
    #     df.to_csv(str(name)+'.csv', encoding='utf-8-sig')