TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


# здесь объявляйте класс Dialog
class Dialog:

    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            return super().__new__(DialogWindows)
        return super().__new__(DialogLinux)

    def __init__(self, name):
        self.name = name


dlg = Dialog('Windows')
print(dlg.name, type(dlg), dlg.name_class)
TYPE_OS = 2
dlg1 = Dialog('Linux')
print(dlg1.name, type(dlg1))