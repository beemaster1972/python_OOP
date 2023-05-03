class Model:

    def __init__(self):
        self.__queries = {}
    def query(self, *args, **kwargs):
        self.__queries = kwargs

    def __str__(self):
        res = "Model " if not self.__queries else "Model:"
        for key, val in self.__queries.items():
            res = res + ' ' + key + ' = ' + str(val) + ','
        return res[:-1]


model = Model()
print(model)
model.query(id=1, fio='Sergey', old=33)
print(model)