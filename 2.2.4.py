class Car:

    def __init__(self):
        self.__model = None

    @staticmethod
    def check_model(model):
        return type(model) is str and 2 <= len(model) <= 100

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self,model):
        if self.check_model(model):
            self.__model = model


auto = Car()
assert '_Car__model' in auto.__dict__, 'В объекте класса нет приватного атрибута __model'
auto.model = 'Toyota'
assert auto.model == 'Toyota', 'Некорректно работает записать данных в __model'
assert auto._Car__model == "Toyota", 'Некоректно работает считывание значения с защищенного приватного свойства'
assert len(auto.__dict__) == 1, 'Объект класса должен содержать всего один защищённый атрибут'