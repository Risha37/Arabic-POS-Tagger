#    $Author: belal (a.k.a risha) $
#    $Revision: 1.2 $

import Nouns
import Verbs
# import Stopwords

class knowntags:
    
    def __init__(self):
        pass
    
    def known_tags(self):
        horoof = ({
            'Voctal': 'يا أ أيا هيا وا'.split(),
            'Answer': 'نعم لا أجل بلى إي كلا إذن'.split(),
            'Conj': 'و ثم أو أم بل حتى لكن'.split(),
            'Genitive': 'من إلى في عن على مذ منذ رب كي لعل حتى لولا'.split(),
            'Exception': 'إلا'.split(),
            'Interro': 'أم هل أ'.split(),
            'Negative': 'لم إن غير لات لما لن لا'.split(),
            'Excpect': 'قد'.split(),
            'Notify': 'ألا أما'.split(),
            'Confirm': 'إن أن قد'.split(),
            'Wishing': 'ليت لو لعل عسى'.split(),
            'Interp': 'إذا أن'.split(),
            'Accusative': 'كأن لكن لعل كي إذن هلا لولا لوما أن لن حتى'.split(),
            'Condition': 'إذا كلما لما لو لولا لوما طالما'.split(),
            'Other': ''.split()
        })
        
        asmaa = ({
            'Exception': 'سوى'.split(),
            'Interro': 'أي ما متى أيان أين أنى كيف كم'.split(),
            'Pronouns': 'أنا نحن إياي أيانا أنت أنتما أنتم أنتن إياك إياكما إياكم إياكن هو هي هما هم هن إياه إياها إياهما إياهم إياهن'.split(),
            'Demonstrative': 'هذا ذاك ذلك هذه هاذي تلك هذان هاتان هؤلاء اولائك هنا هناك هنالك ثمة'.split(),
            'Adverb': 'أمس لدن إذ مع بين بينما الآن ريث ريثما أمس قط عوض حين أيان حيث أين مع صباح مساء فوق تحت أمام جانب خلف يمين يسار شمال جنوب شرق غرب'.split(),
            '5Nouns': 'أب أخ حم ذو فو'.split(),
            'Other': Nouns.nouns
        })
        
        afaal = ({
            'Exception': 'خلا حاشا عدا'.split(),
            'Kana': 'كان-أصبح-أضحى-أمسى-بات-ظل-صار-ما برح-ما انفك-ما زال-ما فتئ-ما دام-ليس-ما ظل'.split('-'),
            'Other': Verbs.verbs
        })
        return horoof, asmaa, afaal