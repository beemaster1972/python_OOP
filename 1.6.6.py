class AbstractClass:
    __instance = None
    def __new__(cls,*args, **kwargs):
        return "Ошибка: нельзя создавать объекты абстрактного класса"


obj = AbstractClass()
obj1 = AbstractClass()
print(obj, obj1)
print(id(obj), id(obj1))
