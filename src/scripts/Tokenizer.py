#    $Author: belal (risha) $
#    $Revision: 1.5 $

import string

class tokenizer:
    """
    This class takes a document file, cleans it, and tokenizes it into list of individual words.
     Input:
        - document: A document file (.txt preferred) containing the sentences.
    """
    
    def __init__(self, document):
        self.document = document
    
    
    def ignore_list(self):
        """
        Ignore List: Contains the punctuation, English letters, and numbers to be removed.
         Output:
            - ignoreList: A list of undesirable punctuations.
            - diacritics: A list of Arabic diacritics
        """
        ignoreList = (list(string.punctuation) + list(string.ascii_letters) +
                      '''ﷺ 1 2 3 4 5 6 7 8 9 0 ٠ ١ ٢ ٣ ٤ ٥ ٦ ٧ ٨ ٩ ؟ …  ٰ ﴿ ﴾ ، " ' ” “ ·  ۛ  ۗ  ۚ  ۙ  ۖ'''.split())
        diacritics = ' ُ  َ  ِ  ْ  ّ  ً  ٌ  ٍ'.split()
        return ignoreList, diacritics
    
    
    def clean_text(self):
        """
        Clean Text: Removes unnecessary punctuation, diacritics, English letters, and numbers.
         Output:
            - cleanedLines: A list of indices, each of which contains a cleaned line from the document.
        """
        ignoreList, diacritics = self.ignore_list()
        file = [line.strip() for line in open(self.document, 'r', encoding='utf-8-sig')]
        cleanedLines = [(''.join([word for word in line if ((word not in ignoreList) and (word not in diacritics))])).strip() for line in file]
        return cleanedLines
    
    
    def tokenize(self):
        """
        Tokenize: Using the split() function, create a list within a list of each word of the document's line from the output of clean_text().
         Output:
            - tokens: A list within a list whose indices are one word from each line of the document.
        """
        cleanedLines = self.clean_text()
        tokens = [line.split() for line in cleanedLines if line != '']
        return tokens
    
    
    
    
    def keep_last_haraka(self):
        """
        Keep Last Haraka: Keep the last diacritic of each word if there is one.
         Output:
            - last_haraka
            - tokens_with_diac
        """
        ignoreList, diacritics = self.ignore_list()
        file = [line.strip() for line in open(self.document, 'r', encoding='utf-8-sig')]
        keep_diacritics = [(''.join([word for word in line if word not in ignoreList])).strip() for line in file] # Keep All Diacritics
        tokens_with_diac = [line.split() for line in keep_diacritics if line != ''] # Keep All Diacritics
        tanween = ' ً  ٌ  ٍ'.split()
        
        last_haraka = [[(''.join([letter for letter in word[:-2] if letter not in diacritics]) + word[-2:]) if (len(word)>=2 and word[-2] in tanween)
                else (''.join([letter for letter in word[:-1] if letter not in diacritics]) + word[-1]) if (word[-1] in diacritics) 
                else (''.join([letter for letter in word if letter not in diacritics])) for word in line] for line in tokens_with_diac]
        return last_haraka, tokens_with_diac