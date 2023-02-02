class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'

p1 = Person()
check_attrib = bool(p1.__dict__.get('job',False))
print(check_attrib)