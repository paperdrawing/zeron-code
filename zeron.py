import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import union

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
       await self.wait_unril_ready()
       if not self.synced:
           await tree.sync(guild = discord.Object(id = 1014461147816140870))
           self.synced = True
       print(f'{self.user}에 로그인 돼었습니다')

client = aclient()
tree = app_commands.CommandTree(client)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='제론아 ', intents=intents)
token = 'MTAxNDgyOTkzMDA0MDgwNzQ4NQ.Gssbaf.61Rl-Ek47DJeWdxxKfKhsnoubkRsqAopanwKwc'

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(str('\'제론아\'라고 불러주시면 언제든 대답하겠습니다.')))

@tree.command(name = 'test', description = 'just test and !s', guild = discord.Object(id = 1014461147816140870))
async def self(interaction:discord.Interaction, name: str):
    await (f'{name}님 테스트가 완료되었습니다.')

@bot.command()
async def 자기소개(ctx):
    await ctx.send('저는 python의 discord.py패키지를 기반으로 만들어진 유틸리티 챗봇입니다.')
    await ctx.typing()
    await asyncio.sleep(5)
    await ctx.send('...너무 자세하다고요?')

bot.run(token)
