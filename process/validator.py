"""
    Abstracao para um tipo de arquivo
"""

class ValidatorType():

    def __init__(self,base_name = ''):
        if not base_name:
            raise TypeError('Fornecer uma descricao do arquivo')
        self.base_name = base_name
        self.ext = '.xml'
        self.formaterRule = None

    def define_format_rule(self,nextformater):
        if self.formaterRule:
            self.formaterRule.next(nextformater)
        else:
            self.formaterRule = nextformater
    
    def validate(self, data):
        if self.formaterRule :
            return self.formaterRule.format(data)
        else:
            raise SyntaxError('No rule defined to validate')