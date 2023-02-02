class CPU:

    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class Motheboard:



    def __init__(self, name, cpu, *mem):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = []
        if len(mem) > self.total_mem_slots:
            mem = mem[:self.total_mem_slots]
        for mem_slot in mem:
            self.mem_slots.append(mem_slot)

    def get_config(self):
        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                f'Память: {";".join(map(lambda x:f"{x.name}  - {x.volume}", self.mem_slots))}']

cpu = CPU('Intel', 3000)
mem1 = Memory('Kingstone', 8192)
mem2 = Memory('Kingstone', 8192)
mem3 = Memory('Kingstone', 8192)
mem4 = Memory('AMD', 8192)
mem5 = Memory('Patriot', 8192)
mb = Motheboard('Gigabyte', cpu, mem1, mem2,mem3,mem4,mem5)

print(mb.get_config())
#'Память: <наименование_1> - <объем_1>; <наименование_2> - <объем_2>; ...; <наименование_N> - <объем_N>']