#    $Author: belal (risha) $
#    $Revision: 1.0 $

import re
from Tokenizer import tokenizer as tk
from patterns import Patterns as pt
import nouns
import verbs

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
            - tags: A dictionary that includes each word and its associated tag.
        """
        
        afaal1, afaal2, horoof, asmaa = pt().get_patterns()
        tokens = self.get_tokens()
        
        tags = {}
        tagsList = []
        
        for sentence in tokens:
            for word in sentence:
                
                if re.search(horoof, word):
                    tags[word] = "Particle"
                    tagsList.append({word: "Particle"})
                
                
                elif word.startswith(('ال', 'كال', 'فال')) or word.endswith(('ة', 'ات', 'ائي', 'ائك', 'ائه', 'اؤك', 'اؤه', 'اءك', 'اءه', 'هما', 'كما')):
                    tags[word] = "Noun"
                    tagsList.append({word: "Noun"})
                elif (word in nouns.nouns.split(sep='|')) or (re.search(asmaa, word)):
                    tags[word] = "Noun"
                    tagsList.append({word: "Noun"})
                
                
                elif re.search(afaal1, word):
                        tags[word] = "Verb"
                        tagsList.append({word: "Verb"})
                elif (word in verbs.verbs.split('|')) or (re.search(afaal2, word)):
                    tags[word] = "Verb"
                    tagsList.append({word: "Verb"})
#                 elif len(word) == 3:
#                     tags[word] = "Verb"
#                     tagsList.append({word: "Verb"})
                    
                
                else:
                    tags[word] = "Noun"
                    tagsList.append({word: "Noun"})
        
        
        return tags, tagsList