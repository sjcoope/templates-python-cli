from __future__ import annotations

class Entity1:
    def __init__(self) -> None:
        self.id = ""
        self.name = ""

    @staticmethod
    def map(cli_object) -> Entity1:
        entity = Entity1()
        entity.id = cli_object["Id"]
        entity.name = cli_object["Name"]
        return entity
