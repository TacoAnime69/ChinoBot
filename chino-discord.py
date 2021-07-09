from discord.ext import commands
from dotenv import load_dotenv
import datetime, os
from ChinoBotCore.CoreProxy import CoreProxy

# Load Environment Variable
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('PREFIX')

bot = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
    now = datetime.datetime.now().strftime('%H:%M:%S on %A, %B the %dth, %Y')
    print('Logged in as {0.user} at {1}'.format(bot, now))

# Random Commands
class RancomComs(commands.Cog):
    @commands.command()
    async def RollDice(self, ctx, *args):
        dices = 1
        rolls = 1
        if len(args) > 0:
            dices = int(args[0])
        
        if len(args) > 1:
            rolls = int(args[1])
        if len(args) > 2:
            await ctx.send('Onii-chan, that\'s too many arguments. ｡ﾟ･ (>﹏<) ･ﾟ｡')
        else: await ctx.send(CoreProxy.roll_dice(dice_count=dices, rolls=rolls))

# Run Bot
bot.add_cog(RancomComs())

bot.run(TOKEN)
