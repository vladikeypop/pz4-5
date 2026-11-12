class DatabaseConnectionManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connections = {}
        return cls._instance

    def get_connection(self, db_type: str) -> str:
        if db_type not in self.connections:
            self.connections[db_type] = f"Connection to {db_type}"
        return self.connections[db_type]

    def get_all_connections(self) -> dict:
        return self.connections
