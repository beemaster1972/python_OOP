class Handler:

    def __init__(self, methods=('GET',)):

        self.__methods = methods

    def __call__(self, func, *args, **kwargs):
        def wrapper(request):
            method = request.get('method', 'GET')
            if method not in self.__methods:
                return None
            return self.__getattribute__(method.lower())(func, request)
        return wrapper

    def get(self, fn, request, *args, **kwargs):
        return f'GET: {fn(request)}'

    def post(self, fn, request, *args, **kwargs):
        return f'POST: {fn(request)}'


@Handler(methods=('GET', 'POST'))
def contact(request):
    return "Сергей Балакирев"

res = contact({"method": "GET", "url": "contact.html"})
print(res)
res = contact({"method": "POST", "url": "contact.html"})
print(res)
res = contact({"method": "DELETE", "url": "contact.html"})
print(res)