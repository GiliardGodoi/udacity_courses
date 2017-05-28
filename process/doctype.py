

class Doctype():

    def __init__(self, basename, ext='.xml'):
        self.basename = basename
        self.ext = ext

    def __str__(self):
        return 'Doctype {}{}'.format(self.basename,self.ext)
    
    def istype(self, file_name =''):
        if not file_name:
            raise TypeError('File_name is not especifed')
        