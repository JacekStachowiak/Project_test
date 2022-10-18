import csv

def getCSVData(fileName):
    # create empty list
    rows = []
    # open the csv file
    dataFile = open(fileName, 'r')
    # read from file csv
    reader = csv.reader(dataFile)
    next(reader)
    #add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows
    