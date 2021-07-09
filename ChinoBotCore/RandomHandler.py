import random

class RandomHandler:
    @staticmethod
    def roll_dice(dice_count: int):
        for i in range(dice_count): yield str(random.randint(1, 6))
    
    @staticmethod
    def random_number(a: int, b: int) -> int:
        return random.randint(a, b)
    
    @staticmethod
    def random_pick(items: list) -> str:
        return str(random.choice(items))
