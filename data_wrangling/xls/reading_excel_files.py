#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    data = [[sheet.cell_value(r, col)
                for col in range(sheet.ncols)]
                    for r in range(sheet.nrows)]

    dados = {
            'maxtime': (0, 0, 0, 0, 0, 0),
            'maxvalue': 0,
            'mintime': (0, 0, 0, 0, 0, 0),
            'minvalue': 0,
            'avgcoast': 0
    }

    dados['maxtime'] = data[1][0]
    dados['maxvalue'] = data[1][1]
    dados['mintime'] = data[1][0]
    dados['minvalue'] = data[1][1]
    soma = 0
    count = 0
    for row in range(sheet.nrows):
        if sheet.cell_type(row,1) == 2 :
            soma += sheet.cell_value(row, 1)
            count += 1
            if sheet.cell_value(row, 1) < dados['minvalue'] :
                dados['minvalue'] = sheet.cell_value(row, 1)
                dados['mintime'] = xlrd.xldate_as_tuple( sheet.cell_value(row,0) , 0)
            if sheet.cell_value(row, 1) > dados['maxvalue']:
                dados['maxvalue'] = sheet.cell_value(row, 1)
                dados['maxtime'] = xlrd.xldate_as_tuple( sheet.cell_value(row,0) , 0)

    dados['avgcoast'] = soma / count


    return dados



def test():
    open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()
