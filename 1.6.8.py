TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


# здесь объявляйте класс Dialog
class Dialog:

    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            dw = super().__new__(DialogWindows)
        else:
            dw = super().__new__(DialogLinux)
        setattr(dw, 'name', args[0])
        return dw




dlg = Dialog('Windows')
print(dlg.name, type(dlg), dlg.name_class)
TYPE_OS = 2
dlg1 = Dialog('Linux')
print(dlg1.name, type(dlg1))