from hero import Hero

class Ranger(Hero):
    def __init__(self, name: str, hp: int = 85, arrow_damage: int = 40):
        super().__init__(name, hp)
        self.arrow_damage = arrow_damage

    def use_special_ability(self) -> str:
        return f"{self.name} fires Multi-Shot, dealing {self.arrow_damage} arrow damage!"