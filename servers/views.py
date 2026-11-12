from django.http import HttpResponse
from .singleton import DatabaseConnectionManager
from .models import ServerFactory


def index(request):
    manager1 = DatabaseConnectionManager()
    manager2 = DatabaseConnectionManager()

    html = ["<h1>Система учёта серверов СУБД</h1>"]

    html.append("<h2>Singleton:</h2>")
    html.append(f"<p>id(manager1) = {id(manager1)}</p>")
    html.append(f"<p>id(manager2) = {id(manager2)}</p>")
    html.append(f"<p>id(manager1) == id(manager2): {id(manager1) == id(manager2)}</p>")

    html.append("<h2>Factory:</h2><ul>")
    try:
        pg_server = ServerFactory.create_server("postgresql", "prod-db-01", "192.168.1.10")
        info = pg_server.get_info()
        manager1.get_connection("postgresql")
        html.append(f"<li>{info}</li>")

        mysql_server = ServerFactory.create_server("mysql", "dev-db-02", "192.168.1.20", 3307)
        info = mysql_server.get_info()
        manager1.get_connection("mysql")
        html.append(f"<li>{info}</li>")

        oracle_server = ServerFactory.create_server("oracle", "finance-db-03", "192.168.1.30")
        info = oracle_server.get_info()
        manager1.get_connection("oracle")
        html.append(f"<li>{info}</li>")

    except ValueError as e:
        html.append(f"<li>{e}</li>")
    html.append("</ul>")

    return HttpResponse("".join(html))


def connections_view(request):
    manager = DatabaseConnectionManager()
    connections = manager.get_all_connections()

    html = ["<h1>Активные подключения к СУБД</h1>"]

    if connections:
        html.append("<p>Данные успешно сохранены в памяти Singleton-объекта между запросами:</p>")
        html.append("<ol>")
        for db_type, conn in connections.items():
            html.append(f"<li><code>{db_type}: {conn}</code></li>")
        html.append("</ol>")
    else:
        html.append(
            "<p>Список подключений пуст. Сначала зайдите на главную страницу!</p>")

    return HttpResponse("".join(html))