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
        if(os.path.isfile(f) and f.endswith('.xml') ):
            process_xml_file(f)
        elif(os.path.isdir(f)) :
            new_folder = os.path.join(os.getcwd(), f)
            file_handler(new_folder)
            os.chdir(folder)

def process_xml_file(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    lenght = len(root)
    print(lenght)
    limit = 500 if 500 < lenght else lenght
    skip = 0; padding = limit
    while(skip < lenght):
        data = process_root_xml_data(root,skip, limit)
        save_json_file(data,'2014_410100_Empenho.json')
        skip = limit
        limit = (limit + padding) if (limit + padding) < lenght else lenght

def process_root_xml_data(root, skip, limit):
    data =  []
    for i in range(skip, limit):
        element = root[i]
        attr = strip_all_fields(element.attrib)
        d = dict_to_json(attr)
        data.append(d)
    return data

def strip_all_fields(dictionary):
    keys = dictionary.keys()
    for k in keys:
        if( type(dictionary[k]) is str ):
            dictionary[k] = dictionary[k].strip()
    return dictionary



if __name__ == '__main__' :
    diretorio = 'despesas'
    arquivo = '2014_410100_Empenho.xml'
    process_xml_file(os.path.join(diretorio,arquivo))