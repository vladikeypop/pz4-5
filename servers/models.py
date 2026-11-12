class DatabaseServer:
    def __init__(self, name: str, ip_address: str, port: int = None):
        self.name = name
        self.ip_address = ip_address
        self.port = port

    def get_info(self) -> str:
        raise NotImplementedError()


class PostgreSQLServer(DatabaseServer):
    def __init__(self, name: str, ip_address: str, port: int = 5432):
        super().__init__(name, ip_address, port or 5432)

    def get_info(self) -> str:
        return f"PostgreSQL: {self.name} ({self.ip_address}:{self.port})"


class MySQLServer(DatabaseServer):
    def __init__(self, name: str, ip_address: str, port: int = 3306):
        super().__init__(name, ip_address, port or 3306)

    def get_info(self) -> str:
        return f"MySQL: {self.name} ({self.ip_address}:{self.port})"


class OracleServer(DatabaseServer):
    def __init__(self, name: str, ip_address: str, port: int = 1521):
        super().__init__(name, ip_address, port or 1521)

    def get_info(self) -> str:
        return f"Oracle: {self.name} ({self.ip_address}:{self.port})"


class ServerFactory:
    _registry = {
        "postgresql": PostgreSQLServer,
        "mysql": MySQLServer,
        "oracle": OracleServer,
    }

    @classmethod
    def create_server(cls, server_type: str, name: str, ip_address: str, port: int = None):
        key = server_type.lower().strip()
        if key not in cls._registry:
            raise ValueError(f"Неизвестный тип: {server_type}")
        if port is not None:
            return cls._registry[key](name, ip_address, port)
        return cls._registry[key](name, ip_address)

    @classmethod
    def create(cls, server_type: str, *args, **kwargs):
        return cls.create_server(server_type, *args, **kwargs)

    @classmethod
    def get_available_types(cls):
        return list(cls._registry.keys())
