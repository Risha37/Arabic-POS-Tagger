#    $Author: belal (risha) $
#    $Revision: 1.0 $

from nouns import nouns
from verbs import verbs

class Patterns:
    def __init__(self):
        pass
    
    
    def get_patterns(self):
        
        verb_prefix = ('|س|ت|ن|ي|است|يت|ان')
        verb_suffix = ('|وا|هم|هما|هن|ون|ان|ن|ه|ها|نا|تن|تم|ي|ين|لي|لت|لن|لأ|لا|سا|سأ|سن|ست|سي|ت')
        # أفعل تفعل تفاعل انفعل افتعل استفعل افعل يفعل يفاعل يتفعل يتفاعل ينفعل يفتعل يستفعل افتعلى تفعلل
        verb_conjugations = "أ[ا-ي]{3}|ت[ا-ي]{3}|ت[ا-ي]ا[ا-ي]{2}|ان[ا-ي]{3}|ا[ا-ي]ت[ا-ي]{2}|است[ا-ي]{3}|ا[ا-ي]{3}|ي[ا-ي]{3}|ي[ا-ي]ا[ا-ي]{2}|يت[ا-ي]{3}|يت[ا-ي]ا[ا-ي]{2}|ين[ا-ي]{3}|ي[ا-ي]ت[ا-ي]{2}|يست[ا-ي]{3}|ا[ا-ي]ت[ا-ي]{2}(ى|ا)|ت[ا-ي]{2}ل[ا-ي]"
        afaal1 = u'^({0})({1})({2})$'.format(verb_prefix, verb_conjugations, verb_suffix)
        afaal2 = u'^({0})({1})({2})$'.format(verb_prefix, verbs, verb_suffix)
        
        
        particle_prefix = ('|ب|ه|ك|ل|ف|م')
        particle_suffix = ('|ها|تها|هم|تهم|تهما|هما|هن|تهن|ما|ا|كما|تما|كن')
        particles = ("يا|أ|أيا|هيا|وا|نعم|لا|أجل|بلى|إي|كلا|إذن|و|ثم|أو|أم|بل|حتى|لكن|من|إلى|في|عن|على|مذ|منذ|رب|كي|لعل|حتى|لولا|إلا|أم|هل|أ|أي|لم|إن|غير|لات|لما|لن|لا|قد|ألا|أما|إن|أن|قد|ليت|لو|لعل|عسى|إذا|أن|إذ|كأن|لكن|لعل|كي|إذن|هلا|لولا|لوما|أن|لن|حتى|إذا|كلما|لما|لو|لولا|لوما|طالما|آ|عل|قد|كأن|ما")
        horoof = u'^({0})({1})({2})$'.format(particle_prefix, particles, particle_suffix)
        
        
        noun_suffix = '|ة|ات|ائي|ائك|ائه|اؤك|اؤه|اءك|اءه|هما|كما|اك|ا'
        noun_prefix = '|ال|كال|بال|أ|فال'
        asmaa = u'^({0})({1})({2})$'.format(noun_prefix, nouns, noun_suffix)
        
        
        
        return afaal1, afaal2, horoof, asmaa
    
    
    
    
    
"""
#         verb_conjugations = (r'(%s)^أ[ا-ي]{3}(%s)$'%(verb_prefix, verb_suffix), r'^(%s)ت[ا-ي]{3}(%s)$'%(verb_prefix, verb_suffix),
#                               r'^(%s)ت[ا-ي]ا[ا-ي]{2}(%s)$'%(verb_prefix, verb_suffix), r'^(%s)ان[ا-ي]{3}(%s)$'%(verb_prefix, verb_suffix),
#                               r'^(%s)ا[ا-ي]ت[ا-ي]{2}(%s)$'%(verb_prefix, verb_suffix), r'^(%s)است[ا-ي]{3}(%s)$'%(verb_prefix, verb_suffix),
#                               r'^(%s)ا[ا-ي]{3}(%s)$'%(verb_prefix, verb_suffix), r'^(%s)ي[ا-ي]{3}(%s)$'%(verb_prefix, verb_suffix),
#                               r'^(%s)ي[ا-ي]ا[ا-ي]{2}(%s)$'%(verb_prefix, verb_suffix), r'^(%s)يت[ا-ي]{3}(%s)$'%(verb_prefix, verb_suffix),
#                               r'^(%s)يت[ا-ي]ا[ا-ي]{2}(%s)$'%(verb_prefix, verb_suffix), r'^(%s)ين[ا-ي]{3}(%s)$'%(verb_prefix, verb_suffix),
#                               r'^(%s)ي[ا-ي]ت[ا-ي]{2}(%s)$'%(verb_prefix, verb_suffix), r'^(%s)يست[ا-ي]{3}(%s)$'%(verb_prefix, verb_suffix),
#                               r'^(%s)ا[ا-ي]ت[ا-ي]{2}(ى|ا)(%s)$'%(verb_prefix, verb_suffix), r'^(%s)ت[ا-ي]{2}ل[ا-ي](%s)$'%(verb_prefix, verb_suffix))



#         horoof = {
#             'Voctal': 'يا أ أيا هيا وا'.split(),
#             'Answer': 'نعم لا أجل بلى إي كلا إذن'.split(),
#             'Conj': 'و ثم أو أم بل حتى لكن'.split(),
#             'Genitive': 'من إلى في عن على مذ منذ رب كي لعل حتى لولا'.split(),
#             'Exception': 'إلا'.split(),
#             'Interro': 'أم هل أ أي'.split(),
#             'Negative': 'لم إن غير لات لما لن لا'.split(),
#             'Excpect': 'قد'.split(),
#             'Notify': 'ألا أما'.split(),
#             'Confirm': 'إن أن قد'.split(),
#             'Wishing': 'ليت لو لعل عسى'.split(),
#             'Interp': 'إذا أن إذ'.split(),
#             'Accusative': 'كأن لكن لعل كي إذن هلا لولا لوما أن لن حتى'.split(),
#             'Condition': 'إذا كلما لما لو لولا لوما طالما'.split(),
#             'Other': 'آ عل قد'.split()
#         }
"""