#створюємо класс машин
class Car:
    def __init__(self, brand, model, price, fuel_consumption, max_speed):
        if price < 0 or fuel_consumption < 0 or max_speed < 0:
            raise ValueError("Параметри автомобіля не можуть бути від'ємними.")
#властивості машини
        self.brand = brand
        self.model = model
        self.price = price
        self.fuel_consumption = fuel_consumption
        self.max_speed = max_speed

#показує, як буде виглядати наш автомобіль
    def __str__(self):
        return f"{self.brand} {self.model}: Ціна=${self.price}, Розхід={self.fuel_consumption}л, Швидкість={self.max_speed}км/год"


#наслідує поведінку класу car
class EconomyCar(Car):
    def __init__(self, brand, model, price, fuel_consumption, max_speed):
        super().__init__(brand, model, price, fuel_consumption, max_speed)
# властивість, яка розрізнює ці класи
        self.category = "Економ"


#наслідує поведінку класу car
class StandardCar(Car):
    def __init__(self, brand, model, price, fuel_consumption, max_speed):
        super().__init__(brand, model, price, fuel_consumption, max_speed)
#властивість, яка розрізнює ці класи
        self.category = "Стандарт"


#наслідує поведінку класу car
class LuxuryCar(Car):
    def __init__(self, brand, model, price, fuel_consumption, max_speed):
        super().__init__(brand, model, price, fuel_consumption, max_speed)
# властивість, яка розрізнює ці класи
        self.category = "Люкс"


#це наш таксопарк
class TaxiPark:
    def __init__(self, cars=None):
        if cars is None:
            self.cars = []
        else:
            self.cars = cars

#підраховує вартість всіх машин за price
    def calculate_total_price(self):
        return sum(car.price for car in self.cars)

#сортує за кількістю палива, що розходить автомобіль
    def sort_by_fuel_consumption(self):
        self.cars.sort(key=lambda car: car.fuel_consumption)

#перевірка кожної машини
    def find_car_by_speed_range(self, min_speed, max_speed):
        if min_speed > max_speed:
            raise ValueError("Мінімальна швидкість не може бути більшою за максимальну.")
        return [car for car in self.cars if min_speed <= car.max_speed <= max_speed]

    def display_cars(self):
        for car in self.cars:
            print(car)


def main():
    try:
        car1 = EconomyCar("Renault", "Logan", 12000, 6.5, 160)
        car2 = StandardCar("Toyota", "Camry", 25000, 8.2, 210)
        car3 = LuxuryCar("Mercedes", "S-Class", 90000, 12.5, 250)
        car4 = EconomyCar("Skoda", "Fabia", 10000, 5.8, 155)

        my_taxi_park = TaxiPark([car1, car2, car3, car4])

        print("Весь таксопарк")
        my_taxi_park.display_cars()

#загальна варість
        total_value = my_taxi_park.calculate_total_price()
        print(f"\nЗагальна вартість автопарку: ${total_value}")

#відсортований за витратами палива
        print("\nСортування за витратами палива")
        my_taxi_park.sort_by_fuel_consumption()
        my_taxi_park.display_cars()

        low, high = 180, 260
        print(f"\nАвтомобілі зі швидкістю в діапазоні, {low}-{high} км/год")
        results = my_taxi_park.find_car_by_speed_range(low, high)
        if not results:
            print("Нічого не знайдено.")
        else:
            for car in results:
                print(car)

    except ValueError as e:
        print(f"Помилка: {e}")
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    main()
