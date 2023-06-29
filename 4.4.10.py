CURRENT_OS = 'linux'   # 'windows', 'linux'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


# здесь объявляйте класс FileDialogFactory
class FileDialogFactory:

    def __new__(cls, *args, **kwargs):
        if CURRENT_OS.lower() == "windows":
            return cls.create_windows_filedialog(*args, **kwargs)
        elif CURRENT_OS.lower() == "linux":
            return cls.create_linux_filedialog(*args, **kwargs)

    @staticmethod
    def create_windows_filedialog(*args, **kwargs):
        return WindowsFileDialog(*args, **kwargs)

    @staticmethod
    def create_linux_filedialog(*args, **kwargs):
        return LinuxFileDialog(*args, **kwargs)


if __name__ == '__main__':
    dlg = FileDialogFactory('Изображения', 'd:/images/', ('jpg', 'gif', 'bmp', 'png'))
    print(type(dlg))