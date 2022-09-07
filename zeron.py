import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import union
import os

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
       await self.wait_until_ready()
       await client.change_presence(status=discord.Status.online, activity=discord.Game(str('\'제론아\'라고 불러주시면 언제든 대답하겠습니다.')))
       if not self.synced:
           await tree.sync(guild=discord.Object(id=1013096945155321907))
           self.synced = True
       print(f'{self.user}에 로그인 돼었습니다')

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = '테스트', description = '이름과 메시지를 출력합니다.', guild=discord.Object(id=1013096945155321907))
async def self(interaction:discord.Interaction, name: str):
    await interaction.response.send_message(f'{name}님 테스트가 완료되었습니다.')

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
