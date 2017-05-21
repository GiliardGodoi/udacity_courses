import urllib

file=urllib.urlopen('http://servicos.tce.pr.gov.br/TCEPR/Tribunal/Relacon/Arquivos/2016/2016_410280_Contrato.zip')

with open('x.zip', 'wb') as output:
    output.write(file.read())
