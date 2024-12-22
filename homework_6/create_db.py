import sqlite3

def create_database():
    # Подключение к базе данных (создание, если не существует)
    conn = sqlite3.connect('gifts.db')
    cursor = conn.cursor()

    # Создание таблицы
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gifts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            gift TEXT NOT NULL,
            price REAL NOT NULL,
            status TEXT NOT NULL
        )
    ''')

    # Вставка данных
    gifts_data = [
        ('Иванов Иван', 'Книга', 500, 'не куплен'),
        ('Петров Петр', 'Часы', 1500, 'куплен'),
        ('Сидоров Сидор', 'Игрушка', 300, 'не куплен'),
        ('Михайлов Михаил', 'Кофеварка', 2500, 'куплен'),
        ('Федоров Федор', 'Наушники', 2000, 'не куплен'),
        ('Смирнова Анна', 'Плед', 800, 'куплен'),
        ('Кузнецова Ольга', 'Блокнот', 150, 'не куплен'),
        ('Тихонов Алексей', 'Ручка', 50, 'куплен'),
        ('Григорьева Светлана', 'Сумка', 1200, 'не куплен'),
        ('Николаев Николай', 'Подарочная карта', 1000, 'куплен'),
        ('Романов Роман', 'Книга коллекционная', 750, 'куплен')
    ]

    cursor.executemany('INSERT INTO gifts (name, gift, price, status) VALUES (?, ?, ?, ?)', gifts_data)

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
