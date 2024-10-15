class Tomato:
    # Статическое свойство, содержащее все стадии созревания помидора
    states = ['absent', 'flowering', 'green', 'red']

    def __init__(self, index):
        # Динамические свойства: _index (индекс) и _state (стадия созревания)
        self._index = index
        self._state = self.states[0]  # Начальная стадия - отсутствует

    def grow(self):
        # Переход на следующую стадию созревания
        current_state_index = self.states.index(self._state)
        if current_state_index < len(self.states) - 1:
            self._state = self.states[current_state_index + 1]

    def is_ripe(self):
        # Проверка что томат созрел
        return self._state == 'red'


class TomatoBush:
    def __init__(self, tomato_count):
        # Динамическое свойство: tomatoes (список томатов)
        self.tomatoes = [Tomato(i) for i in range(tomato_count)]

    def grow_all(self):
        # Переход всех томатов на следующий этап созревания
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        # Проверка, созрели ли все томаты
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        # Удаление всех томатов после сбора урожая
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name, plant):
        # Динамические свойства: name (имя садовника) и _plant (куст помидоров)
        self.name = name
        self._plant = plant

    def work(self):
        # Ухаживание за растением, приводит к росту томатов
        self._plant.grow_all()

    def harvest(self):
        # Проверка, все ли плоды созрели
        if self._plant.all_are_ripe():
            print(f"{self.name} собрал все помидоры!")
            self._plant.give_away_all()
        else:
            print(f"{self.name} говорит: Еще не все помидоры созрели!")

    @staticmethod
    def knowledge_base():
        # Справка по садоводству
        print("База знаний по садоводству:")
        print("1. Регулярно поливайте растения.")
        print("2. Обеспечьте им достаточное количество солнечного света.")
        print("3. Удалите все отмершие листья и вредителей.")
        print("4. Будьте терпеливы, ведь растениям требуется время, чтобы вырасти.")


# Тесты
Gardener.knowledge_base()  # Вызов справки по садоводству

# Создание объектов классов
bush = TomatoBush(5)  # Создаем куст с 5 помидорами
gardener = Gardener("Максим", bush)  # Создаем садовника с именем "Максим" и кустом

# Уход за кустом
gardener.work()  # Ухаживаем за кустом с помидорами
gardener.harvest()  # Пытаемся собрать урожай, когда томаты еще не дозрели

# Продолжаем ухаживать
gardener.work()  # Ухаживаем за кустом снова
gardener.harvest()  # Пытаемся собрать урожай снова

# Ухаживаем до полного созревания
for _ in range(3):
    gardener.work()  # Ухаживаем за кустом

gardener.harvest()  # Собираем урожай
