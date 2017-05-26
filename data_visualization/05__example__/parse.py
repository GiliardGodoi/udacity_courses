import codecs
import xlrd
import datetime, time

def parse_file(input_file):

    workbook = xlrd.open_workbook(input_file)
    sheet = workbook.sheet_by_index(0)

    data = [[ ensure_type(sheet.cell_value(row, col) , col)
                for col in range(sheet.ncols)]
                    for row in range(sheet.nrows)]
    return data

def save_csv_file(data, output_file):
    delimited = '\t'
    with codecs.open(output_file,encoding='utf-8',mode='w') as file:
        for row in data:
            line = delimited.join(row) + '\n'
            file.write(line)

def ensure_type(value, index):
    index_to_date = [1, 5,6,7,8,9,10]
    index_to_string = [0, 2, 11, 12, 13]
    if index in index_to_date:
        return convert_to_date(value)
    elif index in index_to_string:
        return convert_to_string(value)
    elif type(value) is str:
        return value
    else:
        print('value: {0} \t {1}'.format(value,type(value)))
        return value


def convert_to_date(float_date):
    try:
        temp = xlrd.xldate.xldate_as_datetime(float_date,0)
        return temp.strftime('%d/%m/%Y')
    except TypeError:
        return float_date

def convert_to_string(d):
    try:
        return str(int(d))
    except ValueError:
        return d
    
if __name__ == '__main__':
    data = parse_file('leis_2016.xls')
    save_csv_file(data,'projetos.csv')