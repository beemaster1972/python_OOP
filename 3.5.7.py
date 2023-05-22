class FileAcceptor:

    def __init__(self, *args):
        self.__extentions = list(args)

    @staticmethod
    def get_other(other):
        return other.__extentions if isinstance(other, FileAcceptor) else [other]

    def __add__(self, other):
        extentions = self.get_other(other)
        self.__extentions.extend(extentions)
        return FileAcceptor(*self.__extentions)

    def __rsub__(self, other):
        return self + other

    def __call__(self, *args, **kwargs):
        ext = args[0].split('.')[-1]
        return ext in self.__extentions


filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg",
             "forest.jpeg", "eq_1.png", "eq_2.xls", "9val.bmp", 'zabor.ext', 'wall.mp3']
acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))
print(*filenames)
