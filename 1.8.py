class Server:
    __CUR_IP = 1

    def __init__(self):
        self.buffer = []
        self.ip = Server.__CUR_IP
        self.router = None
        Server.__CUR_IP += 1

    def get_ip(self):
        return self.ip

    def send_data(self, data):
        if self.router is not None:
            self.router.buffer.append(data)
        else:
            raise ValueError("Сервер не подключен ни к одному роутеру!!!")

    def get_data(self):
        res = self.buffer[:]
        self.buffer.clear()
        return res


class Router:

    def __init__(self):
        self.buffer = []
        self.servers = dict()

    def link(self, server):
        self.servers[server.ip] = server
        server.router = self

    def unlink(self, server):
        self.servers[server.ip].router = None
        del self.servers[server.ip]

    def send_data(self):
        for i, data in enumerate(self.buffer):
            if data.ip in self.servers:
                self.servers[data.ip].buffer.append(data)
        self.buffer.clear()


class Data:

    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip


if __name__ == "__main__":
    assert hasattr(Router, 'link') and hasattr(Router, 'unlink') and hasattr(Router,
                                                                             'send_data'), "в классе Router присутсвутю не все методы, указанные в задании"
    assert hasattr(Server, 'send_data') and hasattr(Server, 'get_data') and hasattr(Server,
                                                                                    'get_ip'), "в классе Server присутсвутю не все методы, указанные в задании"

    router = Router()
    sv_from = Server()
    sv_from2 = Server()
    router.link(sv_from)
    router.link(sv_from2)
    router.link(Server())
    router.link(Server())
    sv_to = Server()
    router.link(sv_to)
    sv_from.send_data(Data("Hello", sv_to.get_ip()))
    sv_from2.send_data(Data("Hello", sv_to.get_ip()))
    sv_to.send_data(Data("Hi", sv_from.get_ip()))
    router.send_data()
    msg_lst_from = sv_from.get_data()
    msg_lst_to = sv_to.get_data()

    assert len(router.buffer) == 0, "после отправки сообщений буфер в роутере должен очищаться"
    assert len(sv_from.buffer) == 0, "после получения сообщений буфер сервера должен очищаться"

    assert len(msg_lst_to) == 2, "метод get_data вернул неверное число пакетов"

    assert msg_lst_from[0].data == "Hi" and msg_lst_to[
        0].data == "Hello", "данные не прошли по сети, классы не функционируют должным образом"

    assert hasattr(router, 'buffer') and hasattr(sv_to,
                                                 'buffer'), "в объектах классов Router и/или Server отсутствует локальный атрибут buffer"

    router.unlink(sv_to)
    sv_from.send_data(Data("Hello", sv_to.get_ip()))
    router.send_data()
    msg_lst_to = sv_to.get_data()
    assert msg_lst_to == [], "метод get_data() вернул неверные данные, возможно, неправильно работает метод unlink()"
