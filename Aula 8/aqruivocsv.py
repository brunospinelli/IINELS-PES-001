import csv

with open('csv-file.csv', 'w', newline = '') as arquivoCSV:
    spamWriter = csv.writer(arquivoCSV, delimiter = ' ', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    spamWriter.writerow(['Ola']*5+['mundo'])