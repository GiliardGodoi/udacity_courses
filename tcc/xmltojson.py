import codecs
import json
import os
import xml.etree.ElementTree as ET 

def dict_to_json(dict_data) :
    return json.JSONEncoder(ensure_ascii=False,indent=2).encode(dict_data)

def save_json_file(json_data,json_file='file.json'):
    with codecs.open(json_file,encoding='utf-8',mode='a') as file :
        for d in json_data:
            file.write(d)
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

def process_xml_file(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    lenght = len(root)
    limit = 500
    padding = limit
    skip = 0
    data = []
    while(skip < lenght):
        for i in range(skip, limit):
            element = root[i]
            attr = element.attrib
            d = dict_to_json(attr)
            data.append(d)
        save_json_file(data,'arquivo.json')
        data = []
        skip = limit
        limit = (limit + padding) if (limit + padding) < lenght else lenght

if __name__ == '__main__' :
    diretorio = 'despesas'
    arquivo = '2014_410100_Empenho.xml'
    process_xml_file(os.path.join(diretorio,arquivo))