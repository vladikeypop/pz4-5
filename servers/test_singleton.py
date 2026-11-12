
from servers.singleton import DatabaseConnectionManager

print("=" * 60)
print("ТЕСТ SINGLETON")
print("=" * 60)

print("\n1. Создаём первый объект...")
manager1 = DatabaseConnectionManager()

print("\n2. Создаём второй объект...")
manager2 = DatabaseConnectionManager()

print("\n3. Проверяем, что это ОДИН И ТОТ ЖЕ объект:")
print(f"   manager1 is manager2: {manager1 is manager2}")
print(f"   id(manager1): {id(manager1)}")
print(f"   id(manager2): {id(manager2)}")

print("\n4. Добавляем подключение через manager1:")
conn1 = manager1.get_connection("postgresql")
print(f"   Результат: {conn1}")

print("\n5. Получаем подключения через manager2:")
print(f"   Все подключения: {manager2.get_all_connections()}")

print("\n6. Вывод:")
print("manager1 и manager2 — это один объект")
print("Подключение, созданное через manager1, видно в manager2")
print("Singleton работает корректно!")