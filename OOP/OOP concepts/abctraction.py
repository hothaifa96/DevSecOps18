from abc import abstractclassmethod, ABC


#           -------
#           Friends
#           -------
#
#  -------          -------
#   Joey            chandler
#  -------          -------


class Friend(ABC):
    def __init__(self, name, catchphrase):
        self.name = name
        self.catchphrase = catchphrase
        self.acting_job = []
        self.sandwich_count = 0

    @abstractclassmethod
    def say_the_catchphrase(self):
        pass


class JoyLikeFriend(Friend):
    def __init__(self, name, catchphrase):
        super().__init__(name, catchphrase)

    def say_the_catchphrase(self):
        print(f'scream {self.catchphrase}')


class ChandlerLikeFriend(Friend):
    def __init__(self, name, catchphrase, jokes):
        super().__init__(name, catchphrase)
        self.jokes = jokes

    def say_the_catchphrase(self):
        print(f'tell a joke and , {self.catchphrase}')

    def tell_a_joke(self, joke):
        self.jokes.append(joke)
        print(self.jokes)


hassan = JoyLikeFriend('hassan','Dr drake remory')
ishay = ChandlerLikeFriend('ishay','could i be any more sad ?',['monkey joke'])


# hodi = Friend('hodi','oh my God') # X






import time
from abc import abstractclassmethod, ABC


class Server(ABC):
    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip
        self.active = False

    @abstractclassmethod
    def start(self):
        pass

    def __str__(self):
        return f'hostname {self.hostname} ip {self.ip} , staus {self.active}'


class WebServer(Server):
    def __init__(self, hostname, ip, port, protocol):
        super().__init__(hostname, ip)
        self.port = port
        self.protocol = protocol

    def start(self):
        self.active = False
        time.sleep(4)
        self.active = True
        print(f'{self.hostname} Rebooted .......')


class DBServer(Server):
    def __init__(self, hostname, ip, db_engin, databases):
        super().__init__(hostname, ip)
        self.db_engin = db_engin
        self.databases = databases

    def start(self):
        print('connecting to the sql server ')


srv1 = Server('web1.server.1', '100.200.230.155')
# srv2 = Server('web1.server.2', '100.52.92.44')
cocopops = WebServer('web2.server.ui', '10.10.5.4', 3000, 'https')
RDS = DBServer('rds1.server.db', '10.55.23.23', 'postgresql', {'users': 3, 'products': 10})

# print(srv1)
print(cocopops)
print(RDS)
# srv1.start()
cocopops.start()

# print(srv1)
print(cocopops)
print(RDS)