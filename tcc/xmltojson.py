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

def start():
    diretorio = os.getcwd()
    criardiretorio('json')
    print('dir atual: {}'.format(diretorio))
    output = os.path.join(diretorio,'json')
    print('salvar arquivos em: {}'.format(output))
    file_handler(diretorio,output)

def criardiretorio(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        return
        
def file_handler(folder, output_dir):
    os.chdir(folder)
    files = os.listdir(os.getcwd())
    for f in files:
        if(os.path.isfile(f) and f.endswith('.xml') ):
            process_xml_file(f,output_dir)
        elif(os.path.isdir(f)) :
            new_folder = os.path.join(os.getcwd(), f)
            file_handler(new_folder,output_dir)
            os.chdir(folder)

def process_xml_file(xml_file, output_dir):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    lenght = len(root)
    print(lenght)
    limit = 500 if 500 < lenght else lenght
    skip = 0; padding = limit
    output_file = generate_output_file(xml_file, output_dir)
    while(skip < lenght):
        data = process_root_xml_data(root,skip, limit)
        save_json_file(data,output_file)
        skip = limit
        limit = (limit + padding) if (limit + padding) < lenght else lenght

def process_root_xml_data(root, skip, limit):
    data =  []
    for i in range(skip, limit):
        element = root[i]
        d = validate_dict_data(element.attrib)
        data.append(d)
    return data

def generate_output_file(input_file = '',output_dir = ''):
    if not input_file:
        raise TypeError('Input_file is not defined')
    if not type(input_file) is str:
        raise TypeError('Input_file must be string, but is {}'.format(type(input_file)))
    if input_file.find('.xml') < 0 :
        raise TypeError('Input_file must to be a xml file')
    input_file = input_file.lower().replace('.xml', '.json')
    return os.path.join(output_dir, input_file)

def validate_dict_data(data):
    if not data:
        raise SyntaxError('data is not defined')
    data = strip_all_fields(data)
    data = ensure_fields_float(data)
    data = ensure_fields_int(data)
    data = dict_to_json(data)
    return data

def strip_all_fields(dictionary):
    keys = dictionary.keys()
    for k in keys:
        if( type(dictionary[k]) is str ):
            dictionary[k] = dictionary[k].strip()
    return dictionary

def ensure_fields_float(data):
    keys = ['vlLicitacao', 'nrQuantidade', 'vlMinimoUnitarioItem', 'vlMinimoTotal', 'vlMaximoUnitarioitem', 'vlMaximoTotal',
            'nrQuantidadePropostaLicitacao', 'vlPropostaItem','nrPrazoLimiteEntrega', 'nrQuantidadeVencedorLicitacao', 
            'vlLicitacaoVencedorLicitacao']
    for k in keys:
        if k in data:
            data[k] = to_float(data[k])
    return data

def ensure_fields_int(data):
    keys = ['nrClassificacao']
    for k in keys:
        if k in data:
            data[k] = to_int(data[k])
    return data

def to_float(nro):
    try:
        return float(nro)
    except ValueError:
        print('to_float not parse ',nro)
        return 0.0

def to_int(nro):
    try:
        return int(nro)
    except ValueError:
        print('to_int_not parse ', nro)
        return 0

if __name__ == '__main__' :
    start()