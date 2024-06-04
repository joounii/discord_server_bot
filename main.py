import io
import discord
from discord import app_commands
from dotenv import load_dotenv
import os
import random_animal_pictures
import usless_facts
import donald_trump
import generate_qr_code
import bacon_ipsum

load_dotenv()

discord_client_token = os.getenv("DISCORD_CLIENT_TOKEN")
discord_guild_id = os.getenv("DISCORD_TEST_GUILD_ID")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(
    name="cat",
    description="get a picture of a cat",
    guild=discord.Object(id=discord_guild_id)
)
async def cat(interaction):
    await interaction.response.send_message(random_animal_pictures.get_cat_image())
    
@tree.command(
    name="dog",
    description="get a picture of a dog",
    guild=discord.Object(id=discord_guild_id)
)
async def cat(interaction):
    await interaction.response.send_message(random_animal_pictures.get_dog_image())
    
@tree.command(
    name="duck",
    description="get a picture of a duck",
    guild=discord.Object(id=discord_guild_id)
)
async def cat(interaction):
    await interaction.response.send_message(random_animal_pictures.get_duck_image())
    
@tree.command(
    name="uslessfact",
    description="get a ussles fact",
    guild=discord.Object(id=discord_guild_id)
)
async def usless_fact(interaction):
    text, source_url = usless_facts.get_usless_fact()
    embedVar = discord.Embed(title="Usless Fact", description=text, colour=0x00ff00)
    # embedVar.add_field(name="Source", value=source_url, inline=False)
    await interaction.response.send_message(embed=embedVar)
    
@tree.command(
    name="trump",
    description="get a stupid quote from trump",
    guild=discord.Object(id=discord_guild_id)
)
async def usless_fact(interaction):
    quote = donald_trump.get_donald_trump()
    embedVar = discord.Embed(title="Donald Trump", description=quote, colour=0x00ff00)
    # embedVar.add_field(name="Source", value=source_url, inline=False)
    await interaction.response.send_message(embed=embedVar)


app_commands.Parameter("test", command="qrcode")
@tree.command(
    name="qrcode",
    description="create a qr for a link or text",
    guild=discord.Object(id=discord_guild_id)
)
async def cat(interaction: discord.Interaction, link: str):
    qr_code = generate_qr_code.generate_qr_code(link)
    with io.BytesIO(qr_code) as image_binary:
        await interaction.response.send_message(file=discord.File(fp=image_binary, filename='image.png'))
        
@tree.command(
    name="baconipsum",
    description="get some bacon ipsum",
    guild=discord.Object(id=discord_guild_id)
)
async def usless_fact(interaction):
    bacon = bacon_ipsum.get_bacon_ipsum()
    embedVar = discord.Embed(title="Here is your bacon impsum", description=bacon, colour=0x00ff00)
    # embedVar.add_field(name="Source", value=source_url, inline=False)
    await interaction.response.send_message(embed=embedVar)
    
    
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=discord_guild_id))
    print("Ready!")
    
client.run(discord_client_token)