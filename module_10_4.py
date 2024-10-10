from threading import Thread
from queue import Queue
import random
import time


class Table:
    def __init__(self, number):

        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        #print(f"{self.name} сел(-а) за стол номер {self.table_number}")
        st_= random.randint(3, 10)
        time.sleep(st_)
        #print(f"{self.name} покушал(-а) и ушёл(ушла)")


class Cafe:
    def __init__(self,*tables):
        self.queue = Queue()
        self.tables = list(tables)
    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:

                if table.guest == None:

                    table.guest = guest
                    table.guest.start()
                    table.guest.join()
                    print(f'{table.guest.name} сел(-а) за стол {table.number}')
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        for table in self.tables:
            if not table.guest or not (table.guest.is_alive()):
                print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                print(f'Стол номер {table.number} свободен')
            if not self.queue.empty() and not (table.guest is None):
                table.guest = self.queue.get()
                print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                table.guest.start()
                table.guest.join()

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()




