from .RandomHandler import RandomHandler

class CoreProxy:
    @staticmethod
    def roll_dice(dice_count: int, rolls: int) -> str:
        result = ''
        for i in range(rolls):
            rolls = ' ,'.join(list(RandomHandler.roll_dice(dice_count)))
            result += 'Roll #{}: {}\n'.format(i+1, rolls)
        return result
    
