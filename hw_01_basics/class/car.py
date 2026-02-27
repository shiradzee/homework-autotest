class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.engine_started = False
    def start_engine(self):
            print(f"Двигатель {self.brand} {self.model} запущен")
    def stop_engine(self):
            self.engine_started = False
            print(f"Двигатель {self.brand} {self.model} остановлен")
    def get_info(self):
        engine_status = "запущен" if self.engine_started else "остановлен"
        print(f"Информация об автомобиле:")
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Год: {self.year}")
        print(f"Цвет: {self.color}")
        print(f"Состояние двигателя: {engine_status}")

car1 = Car("Mazda","rx-7",2001,"red")
car2 = Car("Bmw","m3",2021,"black")
car3 = Car("Lexus","es250",2021,"silver")
car1.get_info()
car1.start_engine()
car1.get_info()
car1.stop_engine()
car1.get_info()
print("=" * 30)
car2.get_info()
car2.start_engine()
car2.get_info()
car2.stop_engine()
car2.get_info()
print("=" * 30)
car3.get_info()
car3.start_engine()
car3.get_info()
car3.stop_engine()
car3.get_info()
