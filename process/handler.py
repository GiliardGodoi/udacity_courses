import codecs
import json
import os
import xml.etree.ElementTree as ET

#! usr/bin/env python

import formater

class Handler():
    
    def __init__(self, input_dir = 'dados', output_dir = '.\data'):
        self.formaterRule = formater.StripAllFields(None)
        self.dirXML = input_dir
        self.dirJSON = output_dir
        self.startfolder = os.getcwd()
    
    def __str__(self):
        return "Handler files from {0} to {1}".format(self.dirXML, self.dirJSON)
    
    def start(self):
        diretorio = os.getcwd()
        self.file_handler(os.path.join(diretorio, self.dirXML))
    
    def file_handler(self, folder):
        os.chdir(folder)
        files = os.listdir(os.getcwd())
        for f in files:
            if(os.path.isfile(f) and f.endswith('.xml')):
                self.process_xml_file(f, f.lower().replace('.xml', '.json'))
            elif (os.path.isdir(f)) :
                new_folder = os.path.join(os.getcwd(), f)
                print('current folder: {}'.format(folder))
                print('looking at {}'.format(new_folder))
                self.file_handler(new_folder)
                os.chdir(folder)
    
    def process_xml_file(self, xml_input_file, xml_output_file = 'arquivo.json'):
        tree = ET.parse(xml_input_file)
        root = tree.getroot()
        lenght = len(root)
        print(lenght)
        limit = 500 if 500 < lenght else lenght
        skip = 0; padding = limit
        while(skip < lenght):
            data = self.process_root_xml_data(root,skip, limit)
            self.save_json_file(data,xml_output_file)
            skip = limit
            limit = (limit + padding) if (limit + padding) < lenght else lenght
        # return True    
    
    def process_root_xml_data(self, root, skip, limit):
        data =  []
        for i in range(skip, limit):
            element = root[i]
            # attr = strip_all_fields(element.attrib)
            attr = self.formaterRule.format(element.attrib)
            d = self.dict_to_json(attr)
            data.append(d)
        return data
    
    def dict_to_json(self, dict_data) :
        return json.JSONEncoder(ensure_ascii=False,indent=2).encode(dict_data)

    def save_json_file(self, json_data,json_file='file.json'):
        print('save at: {}'.format(json_file))
        with codecs.open(json_file,encoding='utf-8',mode='a') as file :
            for d in json_data:
                file.write(d)
            return True

if __name__ == '__main__' :
    # self.dirXML = './download'
    # self.dirJSON = './data'
    hd = Handler()
    hd.start()
    
