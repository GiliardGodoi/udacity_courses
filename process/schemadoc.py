import xml.etree.ElementTree as ET
import os

class Schema():

    def process(self,folder):
        os.chdir(folder)
        files = os.listdir(os.getcwd())
        for f in files:
            if(os.path.isfile(f) and f.endswith('.xml')):
                self.extract_schema(f)
            elif(os.path.isdir(f)) :
                new_folder = os.path.join(os.getcwd(), f)
                self.process(new_folder)
                os.chdir(folder)

    def extract_schema(self, xml_file):
        xml = ET.parse(xml_file)
        root = xml.getroot()
        print(xml_file, root.tag)
        qtd = len(root)
        if(qtd == 0 ) :
            return 0
        if (qtd == 1) :
            e1 = root[0]
        else:
            e1 = root[1]
        fs_name = e1.tag + '.txt'
        keys = e1.attrib.keys()
        fs = open(fs_name, 'w')
        for k in keys:
            fs.write(k+'\n')
        fs.close()
        return 1

if __name__ == '__main__':
    folder_start = os.path.join(os.getcwd(),'dados')
    sc = Schema()
    sc.process(folder_start)