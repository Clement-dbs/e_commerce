import csv
class WriteInFile():
    
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data

    def write(self):
        with open(self.filename,"w",encoding='utf-8') as data_file:
            write = csv.writer(data_file, delimiter=',')
            write.writerow(self.data)