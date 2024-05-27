import discord
from discord import app_commands
from dotenv import load_dotenv
import os

load_dotenv()

discord_client_token = os.getenv("DISCORD_CLIENT_TOKEN")
discord_guild_id = os.getenv("DISCORD_TEST_GUILD_ID")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(
    name="commandname",
    description="My first application Command",
    guild=discord.Object(id=discord_guild_id)
)
async def first_command(interaction):
    embedVar = discord.Embed(title="Title", description="Desc", colour=0x00ff00)
    await interaction.response.send_message(embedVar)
    
@tree.command(
    name="secondcommand",
    description="test",
    guild=discord.Object(id=discord_guild_id)
)
async def secondcommand(interaction):
    embedVar = discord.Embed(title="Title", description="Desc", colour=0x00ff00)
    embedVar.add_field(name="Field1", value="hi", inline=False)
    embedVar.add_field(name="Field2", value="hi2", inline=False)
    await interaction.response.send_message(embed=embedVar)
    
    
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=discord_guild_id))
    print("Ready!")
    
client.run(discord_client_token)