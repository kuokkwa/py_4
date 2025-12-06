class ScientificEvent:
    def __init__(self, name: str, topic: str, date: str, price: float):
        self.name = name
        self.topic = topic
        self.date = date
        self._price = None
        self.price = price
        self.registered = 0
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        try:
            val = float(value)
        except (ValueError, TypeError):
            raise ValueError("Ціна має бути числовим значенням.")
        if val < 0:
            raise ValueError("Ціна не може бути від’ємною.")
        self._price = val
    
    def add_registered(self, n: int = 1):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Кількість учасників повинна бути невід'ємним цілим числом.")
        self.registered += n

class Conference(ScientificEvent):
    ALLOWED_PLACES = [
        "Актовий зал", "Конференц-зал A", "Конференц-зал B", "Онлайн (Zoom)", "Аудиторія 101"
    ]
    count = 0
    
    def __init__(self, name: str, topic: str, date: str, price: float, place: str = None):
        super().__init__(name, topic, date, price)
        self._place = None
        if place is not None:
            self.place = place
        Conference.count += 1

    def add_place(self, place: str):
        self.place = place

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, value):
        if value not in Conference.ALLOWED_PLACES:
            raise ValueError(f"Некоректне місце! Доступні: {', '.join(Conference.ALLOWED_PLACES)}")
        self._place = value

    def __str__(self):
        return (f"[Конференція] '{self.name}' | Тема: {self.topic} | Дата: {self.date} | "
                f"Ціна: {self.price} грн | Місце: {self.place or 'не вказано'} | Учасників: {self.registered}")

class Webinar(ScientificEvent):
    count = 0
    
    def __init__(self, name: str, topic: str, date: str, price: float, main_speaker: str = None):
        super().__init__(name, topic, date, price)
        self.main_speaker = None
        if main_speaker:
            self.add_speaker(main_speaker)
        Webinar.count += 1

    def add_speaker(self, speaker: str):
        if not isinstance(speaker, str) or not speaker.strip():
            raise ValueError("Ім'я головного доповідача має бути непорожнім рядком.")
        self.main_speaker = speaker.strip()

    def __str__(self):
        return (f"[Вебінар]     '{self.name}' | Тема: {self.topic} | Дата: {self.date} | "
                f"Ціна: {self.price} грн | Спікер: {self.main_speaker or 'не вказано'} | Учасників: {self.registered}")


events = []

print("=== Система обліку наукових заходів ===")

while True:
    print("\nМеню:")
    print("1. Додати Конференцію")
    print("2. Додати Вебінар")
    print("3. Завершити введення та показати звіт")
    
    choice = input("Ваш вибір (1-3): ")
    
    if choice == '3':
        break
    
    if choice not in ('1', '2'):
        print("Помилка: Невірний вибір. Спробуйте ще раз.")
        continue

    try:
        print("\n--- Введіть дані про захід ---")
        name = input("Назва заходу: ")
        topic = input("Тема: ")
        date = input("Дата (РРРР-ММ-ДД): ")
        price_input = input("Ціна участі: ")

        if choice == '1':
            print(f"Доступні місця: {', '.join(Conference.ALLOWED_PLACES)}")
            place = input("Місце проведення (з переліку вище): ")
            
            event = Conference(name, topic, date, float(price_input), place)
            
        elif choice == '2':
            speaker = input("Головний доповідач: ")
            
            event = Webinar(name, topic, date, float(price_input), speaker)
        
        reg_input = input("Кількість зареєстрованих учасників (0 за замовчуванням): ")
        if reg_input.isdigit():
            event.add_registered(int(reg_input))
            
        events.append(event)
        print(">>> Захід успішно додано!")

    except ValueError as e:
        print(f"!!! Помилка даних: {e}")
        continue


print("\n" + "="*40)
print("ПІДСУМКОВИЙ СПИСОК ЗАХОДІВ")
print("="*40)

if not events:
    print("Список порожній.")
else:
    for i, e in enumerate(events, start=1):
        print(f"{i}. {e}")

print("-" * 40)
print(f"Всього конференцій: {Conference.count}")
print(f"Всього вебінарів:   {Webinar.count}")
print("="*40)