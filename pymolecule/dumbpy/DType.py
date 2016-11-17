class dtype():
    signature = {}
    names = []

    def __init__(self, signature):
        # Signature is a dictionaray now!!!
        # var => type
        for var in signature.keys():
            typ = signature[var]
            ****
            for var, typ in [(i[0], i[1].replace("|", ""). replace("<", "")) for i in signature]:
            self.signature[var] = typ 
        self.names = [i[0] for i in signature]
    
    def __str__(self):
        print str(self.signature)

    @staticmethod
    def convert(tp, val):
        if tp == bool:
            return bool(val)

        tp = tp.replace("|", ""). replace("<", "")
        
        if tp[:1].upper() == "F":
            return float(val)
        
        if tp[:1].upper() == "I":
            return int(val)
        
        if tp[:1].upper() == "S":
            return str(val)
