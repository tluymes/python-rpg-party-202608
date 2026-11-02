class Hero:
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp

    def take_damage(self, damage: int) -> int:
        self.hp = max(0, self.hp - damage)
        return self.hp

    def is_alive(self) -> bool:
        return self.hp > 0

    def use_special_ability(self) -> str:
        return f"{self.name} uses a basic attack!"
