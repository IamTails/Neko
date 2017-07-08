from discord.ext import commands
import aiohttp
import discord
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

description = """
I am a bot made to show nekos from nekos.life
"""
bot = commands.AutoShardedBot(command_prefix="!", description=description)


 
@bot.event
async def on_ready():
    print('Logged in as:')
    print('Username: ' + bot.user.name)
    print('ID: ' + bot.user.id)
    print('------')
    guilds = str(len(bot.guilds))
    users = str(len(set(bot.get_all_members())))
    for x in range(bot.shard_count):
        message = 'shard {}/{} | {} guilds | {} users'.format(x+1,bot.shard_count,guilds, users)
        game = discord.Game(name=message)
        print(message)
        await bot.change_presence(game=game,shard_id=x)

@bot.command()
async def shard(ctx):
    """Shard info."""
    shard = ctx.message.guild.shard_id + 1
    em = discord.Embed(title="Your Guild is on shard:", description='{}/{}'.format(shard,bot.shard_count),color=discord.Color.blue())
    await ctx.channel.send(embed=em)

class neko:

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)

    @commands.command(pass_context=True, no_pm=True)
    async def dio(self, ctx):
        """nekos\o/"""
        async with self.session.get("https://nekos.life/api/neko") as resp:
            nekos = await resp.json()

        embed = discord.Embed(colour=discord.Colour.blue())
        embed.set_image(url=nekos['neko'])
        await ctx.send(embed=embed)


n = neko(bot)
bot.add_cog(n)
bot.run("token")
