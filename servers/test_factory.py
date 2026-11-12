

from servers.models import ServerFactory

print("=" * 60)
print("ТЕСТ FACTORY")
print("=" * 60)

print("\n1. Создаём серверы разных типов через Factory:")

# Создаём PostgreSQL
pg_server = ServerFactory.create_server(
    server_type="postgresql",
    name="prod-db-01",
    ip_address="192.168.1.10"
)
print(f"\n✓ Создан: {pg_server}")
print(pg_server.get_info())

# Создаём MySQL
mysql_server = ServerFactory.create_server(
    server_type="mysql",
    name="dev-db-02",
    ip_address="192.168.1.20",
    port=3307  # Нестандартный порт
)
print(f"\n✓ Создан: {mysql_server}")
print(mysql_server.get_info())

# Создаём Oracle
oracle_server = ServerFactory.create_server(
    server_type="oracle",
    name="finance-db-03",
    ip_address="192.168.1.30"
)
print(f"\n✓ Создан: {oracle_server}")
print(oracle_server.get_info())

print("\n2. Проверяем доступные типы:")
print(f"   Доступные типы: {ServerFactory.get_available_types()}")

print("\n3. Проверяем обработку ошибок:")
try:
    bad_server = ServerFactory.create_server("mongodb", "test", "192.168.1.99")
except ValueError as e:
    print(f"Ошибка перехвачена: {e}")

print("\n4. Вывод:")
print("Factory создаёт объекты разных типов")
print("Клиентский код не знает о конкретных классах")
print("Обработка ошибок работает")