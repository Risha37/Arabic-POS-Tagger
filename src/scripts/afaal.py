#    $Author: belal (risha) $
#    $Revision: 1.5 $

from KALIMAT_Corpus.verbs import verbs, verbsOLD

def afaal():
    
    verb_prefix = ('|ل|ف|أ|ي|ت|ن|س|سي|سن|سأ|ست|است|يست|نست')
    
    verb_suffix = ('|ا|ه|ي|ت|ى|و|ك|ها|تها|هم|تهم|هما|تهما|هن|تهن|كما|كن|كم|نا|ني|ان|ون|ين|يه|وا|ما|تا')
    
    #  (فال) (فعا) (فعى) (أعول) افعل يفعل انفعل ينفعل يفاعل تفعل تفاعل افتعل تفعيل استفعل افعوعل افعول تفعلل يتفعلل افعنلل افعلل  يتفعل يتفاعل يفتعل يستفعل افتعلى
    verb_conjugations = '.ا.|..(ا|ى)|ا...|أ.و.|ي...|ان...|ين...|ي.ا..|ت...|ت.ا..|ا.ت..|ت..ي.|است...|ا..و..|ا..و.|ت....|يت....|ا..ن..|ا....|يت...|يت.ا..|ي.ت..|يست...|ا.ت..ى'
                    
    afaal = u'^({0})({1})({2})$'.format(verb_prefix, verb_conjugations, verb_suffix)
    afaal2 = u'^({0})({1})({2})$'.format(verb_prefix, verbs, verb_suffix)
    afaal3 = u'^({0})({1})({2})$'.format(verb_prefix, verbsOLD, verb_suffix)
    return afaal, afaal2, afaal3