class DataBase:

    def __init__(self, path):
        self.path = path
        self.__dict_db = {}

    def write(self,record):
        try:
            self.__dict_db[record].append(record)
        except:
            self.__dict_db[record] = [record]

    def read(self, pk):
        pass


class Record:
    INDEX = 0

    def __init__(self, fio, descr, old):
        self.__pk = Record.INDEX
        Record.INDEX += 1
        self.__fio = fio
        self.__descr = descr
        self.__old = old
        