class Formater:

    def __init__(self, nextFormat = None):
        self.nextFormat = nextFormat
    
    def format(self, data = {}):
        # return executeNet(data) # don't forgette this
        raise NotImplementedError("Methodo process precisa ser reimplementado pelas classes filhas")
    
    def next(self, data):
        if self.nextFormat:
            return self.nextFormat.format(data)
        else:
            return data
    
    def setnext(self,nextFormat):
        if self.nextFormat:
            self.nextFormat.setnext(nextFormat)
        else:
            self.nextFormat = nextFormat

class StripAllFields(Formater):
    
    def __init__(self, nextFormat = None):
        Formater.__init__(self,nextFormat)
    
    def format(self, data = {}):
        for k in data.keys():
            if type(data[k]) is str:
                data[k] = data[k].strip()
        return self.next(data)

class ConvertToFloat(Formater):

    def __init__(self,nextFormat = None, fields = []):
        Formater.__init__(self,nextFormat)
        if not fields:
            raise TypeError('Campos para conversão não foram especificados')
        self.fields = fields
    
    def format(self, data = {}):
        for f  in self.fields:
            try:
                data[f] = float(data[f])
            except ValueError:
                continue
    