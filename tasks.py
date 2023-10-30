print('Задача 1: Наследование и отображение информации')
class ItemDiscount:
    """ Класс для представления скидки на товар. """

    def __init__(self, name, price):
        """ Инициализация с названием и ценой товара. """
        self.name = name
        self.price = price

class ItemDiscountReport(ItemDiscount):
    """ Класс для отчёта о товаре, расширяющий ItemDiscount. """

    def get_parent_data(self):
        """ Возвращает строку с информацией о товаре. """
        return f"Товар: {self.name}, Цена: {self.price}"

# Клиентский код для проверки
item = ItemDiscountReport("Телевизор", 25000)
print(item.get_parent_data())

print("-" * 50)


print('Задача 2: Инкапсуляция и доступ к приватным атрибутам')
class ItemDiscount:
    """ Класс с инкапсулированными атрибутами товара. """

    def __init__(self, name, price):
        """ Инициализация с названием и ценой товара. """
        self.__name = name
        self.__price = price

    @property
    def name(self):
        """ Возвращает название товара. """
        return self.__name

    @property
    def price(self):
        """ Возвращает цену товара. """
        return self.__price

class ItemDiscountReport(ItemDiscount):
    """ Класс для отчёта о товаре с приватными атрибутами. """

    def get_parent_data(self):
        """ Возвращает строку с информацией о товаре. """
        return f"Товар: {self.name}, Цена: {self.price}"

# Клиентский код для проверки
item = ItemDiscountReport("Телевизор", 25000)
print(item.get_parent_data())

print("-" * 50)


print('Задача 3: Переустановка Цены')
class ItemDiscount:
    """ Класс товара с возможностью изменения цены. """

    def __init__(self, name, price):
        """ Инициализация с названием и ценой товара. """
        self.__name = name
        self.__price = price

    @property
    def name(self):
        """ Возвращает название товара. """
        return self.__name

    @property
    def price(self):
        """ Возвращает цену товара. """
        return self.__price

    @price.setter
    def price(self, new_price):
        """ Устанавливает новую цену товара. Проверяет, что цена положительная. """
        if new_price < 0:
            raise ValueError("Цена не может быть отрицательной.")
        self.__price = new_price

class ItemDiscountReport(ItemDiscount):
    """ Класс отчёта о товаре с изменяемой ценой. """

    def get_parent_data(self):
        """ Возвращает строку с информацией о товаре. """
        return f"Товар: {self.name}, Цена: {self.price}"

# Клиентский код для проверки
item = ItemDiscountReport("Телевизор", 25000)
print(item.get_parent_data())
try:
    item.price = -100  # Попытка установить отрицательную цену
except ValueError as e:
    print(f"Ошибка: {e}")

item.price = 20000  # Установка новой цены
print(item.get_parent_data())

print("-" * 50)


print('Задача 4: Расчёт цены товара со Скидкой')
class ItemDiscount:
    """ Класс товара с основной ценой. """

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

class ItemDiscountReport(ItemDiscount):
    """ Класс отчёта о товаре со скидкой. """

    def __init__(self, name, price, discount):
        if discount < 0 or discount > 100:
            raise ValueError("Скидка должна быть в диапазоне от 0 до 100.")
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        final_price = self.price - (self.price * self.discount / 100)
        return f"Товар: {self.name}, Исходная цена: {self.price}, Цена со скидкой {self.discount}%: {final_price:.2f}"

# Клиентский код для проверки
item = ItemDiscountReport("Ноутбук", 50000, 10)
print(item)
try:
    item = ItemDiscountReport("Ноутбук", 50000, 110)
    print(item)
except ValueError as e:
    print(f"Ошибка: {e}")

print("-" * 50)

print('Задача 5: Полиморфизм и Разделение Классов')
class ItemNameReport(ItemDiscount):
    """ Класс для отображения названия товара. """

    def get_info(self):
        return f"Название товара: {self.name}"

class ItemPriceReport(ItemDiscount):
    """ Класс для отображения цены товара. """

    def get_info(self):
        return f"Цена товара: {self.price}"

# Клиентский код для проверки
name_report = ItemNameReport("Планшет", 30000)
price_report = ItemPriceReport("Планшет", 30000)

print(name_report.get_info())
print(price_report.get_info())

