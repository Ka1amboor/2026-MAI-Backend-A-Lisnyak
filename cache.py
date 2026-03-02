class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.data: dict[str, str] = {}

    def get(self, key: str) -> str:
        if key not in self.data:
            return ""

        # перемещаем ключ в конец (как недавно использованный)
        value = self.data.pop(key)
        self.data[key] = value
        return value

    def set(self, key: str, value: str) -> None:
        # если ключ уже есть — удалить, чтобы обновить порядок
        if key in self.data:
            self.data.pop(key)

        self.data[key] = value

        # если превышена ёмкость — удалить самый старый
        if len(self.data) > self.capacity:
            oldest_key = next(iter(self.data))
            self.data.pop(oldest_key)

    def rem(self, key: str) -> None:
        if key in self.data:
            self.data.pop(key)