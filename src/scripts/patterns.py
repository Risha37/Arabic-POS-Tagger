#    $Author: belal (risha) $
#    $Revision: 1.5 $

from KALIMAT_Corpus.verbs import verbs, verbsOLD
from KALIMAT_Corpus.nouns import nouns, nounsOLD

class Patterns:
    def __init__(self):
        pass
    
    
    def afaal(self):
    
        verb_prefix = ('|ل|ف|أ|ي|ت|ن|س|سي|سن|سأ|ست|است|يست|نست')
        
        verb_suffix = ('|ا|ه|ي|ت|ى|و|ك|ها|تها|هم|تهم|هما|تهما|هن|تهن|كما|كن|كم|نا|ني|ان|ون|ين|يه|وا|ما|تا')
        
        #  (فال) (فعا) (فعى) (أعول) افعل يفعل انفعل ينفعل يفاعل تفعل تفاعل افتعل تفعيل استفعل افعوعل افعول تفعلل يتفعلل افعنلل افعلل  يتفعل يتفاعل يفتعل يستفعل افتعلى
        verb_conjugations = '.ا.|..(ا|ى)|ا...|أ.و.|ي...|ان...|ين...|ي.ا..|ت...|ت.ا..|ا.ت..|ت..ي.|است...|ا..و..|ا..و.|ت....|يت....|ا..ن..|ا....|يت...|يت.ا..|ي.ت..|يست...|ا.ت..ى'
                        
        afaal = u'^({0})({1})({2})$'.format(verb_prefix, verb_conjugations, verb_suffix)
        afaal2 = u'^({0})({1})({2})$'.format(verb_prefix, verbs, verb_suffix)
        afaal3 = u'^({0})({1})({2})$'.format(verb_prefix, verbsOLD, verb_suffix)
        return afaal, afaal2, afaal3
    
    
    def asmaa(self):
    
        noun_prefix = ('|ب|ك|ل|ف|أ|م|لل')
        
        noun_suffix = ('|ا|ك|ه|ي|ل|ى|ها|تها|هم|تهم|هما|تهما|هن|تهن|ما|كما|كن|كم|نا|ان|ون|ين|وت|يه|تا|ات')
        
        # فعيل فعال فعول افعال مفعول مفعال مفعيل فعليل فعلاء فعلان فعلى فيعل مفعل فاعول استفعال تفعيل مفتعل
        noun_conjugations = '..ي.|..ا.|..و.|ا..ا.|م..و.|م..ا.|م..ي.|...ي.|...اء|...ان|...ى|.ي..|م...|.ا.و.|است..ا.|ت..ي.|م.ت..'
                            
        asmaa = u'^({0})({1})({2})$'.format(noun_prefix, noun_conjugations, noun_suffix)
        asmaa2 = u'^({0})({1})({2})$'.format(noun_prefix, nouns, noun_suffix)
        asmaa3 = u'^({0})({1})({2})$'.format(noun_prefix, nounsOLD, noun_suffix)
        return asmaa, asmaa2, asmaa3
    
    
    def horoof(self):

        particle_prefix = ('|ب|ك|ل|ف|أ|و')

        particle_suffix = ('|ا|ك|ه|ي|ها|تها|هم|تهم|هما|تهما|هن|تهن|ما|كما|كن|كم|نا')
        
        particles = ("يا|أ|أيا|ايا|هيا|نعم|لا|أجل|اجل|بلى|إي|اي|كلا|إذن|اذن|ثم|أو|او|أم|بل|حتى|لكن|من|إلى|الى|في|عن|على|مذ|منذ|كي|لعل|إلا|ام|هل|أي|لم|إن|غير|لما|لن|ألا|أما|اما|ليت|عسى|إذا|أن|إذ|كي|حتي|اذا|كلما|لو|لولا|لوما|طالما|آ|عل|قد|كأن|ما|علي|ل|ب|مع|أيضا|ايضا|ممن|حيث|ثم|لماذا|بين|اين|متى|اذ|إذ|ع|ك|ريث|متي|كيف|إياك")
        horoof = u'^({0})({1})({2})$'.format(particle_prefix, particles, particle_suffix)
        return horoof
        """
        #         horoof = {
        #             'Voctal': 'يا أ أيا هيا وا'
        #             'Answer': 'نعم لا أجل بلى إي كلا إذن'
        #             'Conj': 'و ثم أو أم بل حتى لكن'
        #             'Genitive': 'من إلى في عن على مذ منذ رب كي لعل حتى لولا'
        #             'Exception': 'إلا'
        #             'Interro': 'أم هل أ أي'
        #             'Negative': 'لم إن غير لات لما لن لا'
        #             'Excpect': 'قد'
        #             'Notify': 'ألا أما'
        #             'Confirm': 'إن أن قد'
        #             'Wishing': 'ليت لو لعل عسى'
        #             'Interp': 'إذا أن إذ'
        #             'Accusative': 'كأن لكن لعل كي إذن هلا لولا لوما أن لن حتى'
        #             'Condition': 'إذا كلما لما لو لولا لوما طالما'
        #             'Other': 'آ عل قد'
        #         }
        """
    
    
    def get_patterns(self):
                
        horoof = self.horoof()
        
        asmaa, asmaa2, asmaa3 = self.asmaa()
        
        afaal, afaal2, afaal3 = self.afaal()
        
        return horoof, asmaa, asmaa2, asmaa3, afaal, afaal2, afaal3