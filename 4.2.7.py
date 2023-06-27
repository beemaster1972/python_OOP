class VideoItem:

    __slots__ = 'title', 'descr', 'path', 'rating'

    def __init__(self, title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:

    __slots__ = '__rating'

    def __init__(self):
        self.__rating = 0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        conditions = [isinstance(rating, int), 0 <= rating <= 5]
        if not all(conditions):
            raise ValueError(f'неверное присваиваемое значение: {rating}')
        self.__rating = rating


if __name__ == '__main__':
    v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
    print(v.rating.rating)  # 0
    v.rating.rating = 5
    print(v.rating.rating)  # 5
    title = v.title
    descr = v.descr
    v.rating.rating = 6  # ValueError