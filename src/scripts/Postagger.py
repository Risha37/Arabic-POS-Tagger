#    $Author: belal (risha) $
#    $Revision: 1.5 $

import re
from Tokenizer import tokenizer as tk
from patterns import Patterns as pt

class postagger:
    """
    This class tags each word in a file.
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
            - tokens_with_diac
            - last_haraka
        """
        tokens, tokens_with_diac = tk(self.document).tokenize()
        last_haraka = tk(self.document).keep_last_haraka()
        return tokens, tokens_with_diac, last_haraka
    
    
    
    def tag(self):
        """
        PosTag: Divide each word into its respective tag (Noun, Verb, Particle) using the provided rules.
         Outputs:
            - tagsList: A list that contains the tags ordered with respect to the word.
        """
        horoof, asmaa, afaal = pt().get_patterns()
        tokens, tokens_with_diac, last_haraka = self.get_tokens()
        tanween = ' ً  ٌ  ٍ'.split()
        
        tagsList = []
        
        
        for i in range(len(tokens)):
            for j in range(len(tokens[i])):
                
                
                if (re.search(horoof, tokens[i][j]) or tokens[i][j]=='و') and (tokens[i][j]!='كان'):
                    tagsList.append({tokens[i][j]: "Particle"})
                
                
                elif tokens[i][j].startswith(('ال', 'كال', 'فال', 'بال')) or tokens[i][j].endswith(('ة', 'ائي', 'ائك', 'ائه', 'اؤك', 'اؤه', 'اءك', 'اءه')):
                    tagsList.append({tokens[i][j]: "Noun"})
                elif (len(tokens[i][j])>2) and ((last_haraka[i][j][-1] in tanween) or (last_haraka[i][j][-2] in tanween)):
                    tagsList.append({tokens[i][j]: "Noun"})
                    
                    
                elif re.search(afaal, tokens[i][j]):
                    tagsList.append({tokens[i][j]: "Verb"})
                    
                    
                elif re.search(asmaa, tokens[i][j]):
                    tagsList.append({tokens[i][j]: "Noun"})
                    
                
                else:
                    tagsList.append({tokens[i][j]: "Don't Know"})
        
        
        return tagsList