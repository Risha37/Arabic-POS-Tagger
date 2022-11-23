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
        """
        tokens = tk(self.document).tokenize()
        return tokens
    
    
    
    def tag(self):
        """
        PosTag: Divide each word into its respective tag (Noun, Verb, Particle) using the provided rules.
         Outputs:
            - tagsList: A list that contains the tags ordered with respect to the word.
        """
        horoof, asmaa, afaal = pt().get_patterns()
        tokens = self.get_tokens()
        
        tagsList = []
        
        
        for i in range(len(tokens)):
            for j in range(len(tokens[i])):
                
                # P.1
                if (re.search(horoof, tokens[i][j]) or tokens[i][j]=='و') and (tokens[i][j]!='كان'):
                    tagsList.append({tokens[i][j]: "Particle"})
                    
                    
                # N.1
                elif tokens[i][j].startswith(('ال', 'كال', 'فال', 'بال', 'وال')) or tokens[i][j].endswith(('ة', 'ائي', 'ائك', 'ائه', 'اؤك', 'اؤه', 'اءك', 'اءه', 'اء')):
                    tagsList.append({tokens[i][j]: "Noun"})
                    
                    
                # V.1
                elif tokens[i][j].startswith(('ت', 'ي', 'سأ', 'سي', 'ست', 'سن')) and tokens[i][j].endswith(('ون', 'وا', 'ين')):
                    tagsList.append({tokens[i][j]: "Verb"})
                # V.2
                elif re.search(afaal, tokens[i][j]):
                    tagsList.append({tokens[i][j]: "Verb"})
                    
                    
                # N.2
                elif re.search(asmaa, tokens[i][j]):
                    tagsList.append({tokens[i][j]: "Noun"})
                    

                # ??
                else:
                    tagsList.append({tokens[i][j]: "Don't Know"})
        
        
        return tagsList