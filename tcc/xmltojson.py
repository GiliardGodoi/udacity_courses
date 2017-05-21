import codecs
import json
import os
import xml.etree.ElementTree as ET 

def dict_to_json(dict_data) :
    return json.JSONEncoder(ensure_ascii=False,indent=2).encode(dict_data)

def save_json_file(json_data,json_file='file.json'):
    with codecs.open(json_file,encoding='utf-8',mode='a') as file :
        file.write(json_data)
        return True

def file_handler(folder):
    os.chdir(folder)
    files = os.listdir(os.getcwd())
    for f in files:
        if(os.path.isfile(f)):
            # extract_schema(f) extract_data
            pass
        else :
            new_folder = os.path.join(os.getcwd(), f)
            file_handler(new_folder)
            os.chdir(folder)

if __name__ == '__main__' :
    diretorio = 'despesas'
    arquivo = '2014_410100_Empenho.xml'
    tree = ET.parse(os.path.join(diretorio,arquivo))
    root = tree.getroot()
    for elem in root:
        attr = elem.attrib
        data = dict_to_json(attr)
        save_json_file(data,'2014_410100_empenho.json')