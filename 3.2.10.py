class InputValues:
    def __init__(self, render):     # render - ссылка на функцию или объект для преобразования
        # здесь строчки программы
        self.__render = render

    def __call__(self, func):     # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            # здесь строчки программы

            return list(map(self.__render, func(*args, **kwargs).split()))
        return wrapper


class RenderDigit:

    def __call__(self, *args, **kwargs):

        try:
            return int(args[0])
        except:
            return None


render = RenderDigit()
input_dg = InputValues(render)(input)
res = input_dg()
print(res)
