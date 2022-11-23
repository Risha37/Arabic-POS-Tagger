#    $Author: belal (risha) $
#    $Revision: 1.5 $

import horoof as hor
import asmaa as asm
import afaal as afa

class Patterns:
    def __init__(self):
        pass
    
    
    def get_patterns(self):
                
        horoof = hor.horoof()
        
        asmaa, asmaa2, asmaa3 = asm.asmaa()
        
        afaal, afaal2, afaal3 = afa.afaal()
        
        return horoof, asmaa, asmaa2, asmaa3, afaal, afaal2, afaal3