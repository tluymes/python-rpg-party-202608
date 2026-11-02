from hero import Hero


class Tank(Hero):
    def __init__(self, name: str, hp: int, shield: int = 20):
        super().__init__(name, hp)
        self.shield_strength = shield
        self.shield = shield

    def use_special_ability(self) -> str:
        self.shield = self.shield_strength
        return f"{self.name}: Shield activated"

    def shield_damage(self, damage: int):
        self.shield = max(0, self.shield - damage)

    def take_damage(self, damage: int) -> int:
        if damage <= self.shield:
            self.shield_damage(damage)
            return self.hp
        else:
            remaining_damage = damage - self.shield
            self.shield_damage(self.shield)
            self.shield = 0
            return super().take_damage(remaining_damage)
