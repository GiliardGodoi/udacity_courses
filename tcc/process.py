import lxml.etree as ET
import os

def process(folder):
    os.chdir(folder)
    files = os.listdir(os.getcwd())
    for f in files:
        if(os.path.isfile(f)):
            extract_schema(f)
        else :
            new_folder = os.path.join(os.getcwd(), f)
            process(new_folder)
            os.chdir(folder)

def extract_schema(xml_file):
    xml = ET.parse(xml_file)
    root = xml.getroot()
    print xml_file, root.tag
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

folder_start = os.path.join(os.getcwd(),'despesas')
process(folder_start)