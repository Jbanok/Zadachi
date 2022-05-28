# Теплица с помидорами у бабушки в деревне
class Tomato:
    # Стадии созревания помидора
    states = {'nothing': 0, 'flower': 1, 'green_tomato': 2, 'red_tomato': 3}
    def __init__(self, index):
        self._index = index
        self._state = self.states['nothing']
    # Переход к следующей стадии созревания
    def grow(self):
        if self._state < 3:
            self._state += 1
    # Проверка, созрел ли томат
    def is_ripe(self):
        if self._state == 3:
            return True
        return False
class TomatoBush:
    # Создаем список из объектов класса Tomato
    def __init__(self, num):
        self.tomatoes = [Tomato(i) for i in range(num)]
    # Переводим все томаты из списка на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
    # Проверяем, все ли помидоры созрели
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])
    # Собираем урожай
    def give_away_all(self):
        self.tomatoes = []
class Gardener:
    # Выдаем садовнику растение для ухода
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
    # Ухаживаем за растением
    def work(self):
        print('Gardener is working...')
        self._plant.grow_all()
        print('Gardener finished')
    # Собираем урожай
    def harvest(self):
        print('Gardener is harvesting...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Harvesting is finished')
        else:
            print('Too early! Your plant is green and not ripe.')
    # Статический метод
    # Выводит справку по садоводству. Скажу честно , подсмотрел
    @staticmethod
    def knowledge_base():
        print('Gardener work!')
# Тесты
Gardener.knowledge_base()
great_tomato_bush = TomatoBush(4)
gardener = Gardener('Emilio', great_tomato_bush)
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()



