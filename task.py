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
            raise ValueError("Кількість доданих учасників повинна бути невід'ємним цілим числом.")
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
            raise ValueError(f"Місце проведення має бути одним з: {', '.join(Conference.ALLOWED_PLACES)}")
        self._place = value
    def __str__(self):
        return (f"Conference: {self.name} | Тема: {self.topic} | Дата: {self.date} | "
                f"Ціна: {self.price} | Місце: {self.place or 'не вказано'} | Зареєстровано: {self.registered}")

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
        return (f"Webinar: {self.name} | Тема: {self.topic} | Дата: {self.date} | "
                f"Ціна: {self.price} | Доповідач: {self.main_speaker or 'не вказано'} | Зареєстровано: {self.registered}")

# Прикладні об'єкти (якщо вводу немає)
events = [
    Conference(name="Кібербезпека 2025", topic="Сучасні виклики кібербезпеки", date="2025-11-10", price=25.0, place="Актовий зал"),
    Conference(name="Небезпека ШІ", topic="Використання ШІ зловмисниками", date="2025-12-05", price=200.0, place="Конференц-зал A"),
    Webinar(name="Python та дані", topic="Використання Python для обробки даних", date="2025-09-20", price=100.0, main_speaker="Dr. Kovalenko"),
    Webinar(name="Веб-загрози", topic="Огляд веб-загроз", date="2025-10-01", price=0.0, main_speaker="Prof. Ivanenko"),
]

events[0].add_registered(30)
events[1].add_registered(12)
events[2].add_registered(85)
events[3].add_registered(40)

print("Заходи:")
for i, e in enumerate(events, start=1):
    print(f"{i}. {e}")

conf_count = sum(1 for e in events if isinstance(e, Conference))
web_count = sum(1 for e in events if isinstance(e, Webinar))
print(f"\nКількість конференцій: {conf_count}")
print(f"Кількість вебінарів: {web_count}")