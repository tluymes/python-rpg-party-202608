from paladin import Paladin
from tank import Tank
from healer import Healer
from warrior import Warrior
from mage import Mage

def main():
    print("=== RPG PARTY BATTLE SIMULATOR ===")
    party = [Paladin("Ocean"),Tank("Alex",100,50),Healer("Frank"),Mage("Mr.L"),Warrior("Tommy")]
  
    for hero in party:
        print(f"\nHero: {hero.name} (HP: {hero.hp})")
        print(hero.use_special_ability())

if __name__ == "__main__":
    main()
