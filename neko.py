from discord.ext import commands
import aiohttp
import discord
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

description = """
I am a bot made to show nekos from nekos.life
"""
bot = commands.Bot(command_prefix="!", description=description)


 
@bot.event
async def on_ready():
    print('Logged in as:')
    print('Username: ' + bot.user.name)
    print('ID: ' + bot.user.id)
    print('------')

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
        await self.bot.say(embed=embed)


n = neko(bot)
bot.add_cog(n)
bot.run("token")
