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
       await self.wait_unril_ready()
       if not self.synced:
           await tree.sync()
           self.synced = True
       print(f'{self.user}에 로그인 돼었습니다')

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = 'test', description = 'just test and ereers')
async def self(interaction:discord.Interaction, name: str):
    await interaction.response.send_message(f'{name}님 테스트가 완료되었습니다.')

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
