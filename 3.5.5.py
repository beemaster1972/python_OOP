class StringText:
    EXTRA_CHARACTERS = "–?!,.; "
    def __init__(self, *args):
        self.words_list = []
        if isinstance(args[0], list):
            self.words_list = args[0]
        elif isinstance(args[0], str):
            self.words_list = args[0].strip(self.EXTRA_CHARACTERS).split()

    def __len__(self):
        return len(self.words_list)

    def __gt__(self, other):
        return len(self) > len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __str__(self):
        return " ".join(self.words_list)

stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

lst_text = [StringText(s) for s in stich]
lst_text_sorted = sorted(lst_text, key=lambda x: len(x), reverse=True)
lst_text_sorted =[str(x) for x in lst_text_sorted]
print(*lst_text, sep='\n')
print('*********************')
print(*lst_text_sorted, sep='\n')
