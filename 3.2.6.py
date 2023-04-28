class RenderList:

    def __init__(self, type_lst='ul'):
        self.type_lst = type_lst if type_lst == 'ol' else 'ul'

    def __call__(self, *args, **kwargs):
        res = f'<{self.type_lst}>\n'
        try:
            for i, el in enumerate(args[0]):
                res += f'<li>{el}</li>\n'
            res += f'</{self.type_lst}>'
            return res
        except:

            return None


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(1)
print(html)
