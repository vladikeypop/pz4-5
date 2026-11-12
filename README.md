# Практическое занятие №4-5 (ПЗ 4-5)

Проект на Django, демонстрирующий применение порождающих паттернов проектирования **Singleton** (Одиночка) и **Factory Method** (Фабричный метод).

## Реализованные паттерны

### 1. Singleton (Одиночка)
- **Файл:** `servers/singleton.py` (`DatabaseConnectionManager`)
- **Описание:** Гарантирует наличие единственного экземпляра менеджера подключений к базам данных и предоставляет глобальную точку доступа к нему.
- **Тест:** `servers/test_singleton.py`

### 2. Factory Method (Фабричный метод)
- **Файл:** `servers/models.py` (`ServerFactory`, `PostgreSQLServer`, `MySQLServer`, `OracleServer`)
- **Описание:** Позволяет создавать объекты серверов различных типов СУБД через единый интерфейс фабрики без привязки клиентского кода к конкретным классам.
- **Тест:** `servers/test_factory.py`

---

## Запуск тестов

Выполнять из корневой директории проекта:

```bash
# Тест паттерна Singleton
python -m servers.test_singleton

# Тест паттерна Factory Method
python -m servers.test_factory
```

## Запуск веб-сервера

```bash
python manage.py runserver
```

Маршруты:
- `http://127.0.0.1:8000/` — демонстрация работы Singleton и Factory Method
- `http://127.0.0.1:8000/connections/` — активные подключения к СУБД
