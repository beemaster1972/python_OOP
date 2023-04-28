class HandlerGET:

    def __init__(self, fn):
        self.__fn = fn

    def __call__(self, *args, **kwargs):
        return self.get(self.__fn, *args, **kwargs)

    def get(self, fn, request, *args, **kwargs):

        try:
            method = request['method']
        except KeyError:
            method = 'GET'

        if method != 'GET':
            return None
        return method + ': '+fn(request)


@HandlerGET
def contact(request):
    return "Сергей Балакирев"

res = contact({"method": "GET", "url": "contact.html"})
print(res)