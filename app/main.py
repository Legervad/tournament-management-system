import asyncio

import discord
import requests

from discord.ext import commands
users = []
bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=discord.Intents.all())
def get_quote():
    response = requests.get(url="https://zenquotes.io/api/random")
    quote = response.json()[0]['q']
    print(quote)
    return quote

@bot.event
async def on_ready():  # When the bot is ready
    print("We have logged in as {0.user}".format(bot))


@bot.event
async def on_message(message):
    print("User sent a message")
    if message.author == bot.user:
        return

    if message.content.startswith("!hello"):
        await message.channel.send("Hello!")
    elif message.content.startswith("!inspire"):
        await message.channel.send(get_quote())

participants = ["emre", "emre2", "emre3", "emre4", "emre5", "emre6", "emre7"]

@bot.slash_command(name='greet', description='Greet a user')
async def greet(ctx: discord.ApplicationContext,
                user: discord.Option(str, choices=participants, description="The user's name"),
                message: discord.Option(str, "Your message", required=False, default="Hello!")):
    """A command to greet a user with an optional message."""
    currentUser = ctx.user
    greeting = f"{currentUser.name} greets you {user}, with the message {message}!"
    await currentUser.send(greeting)
    await ctx.respond(greeting, ephemeral=True)

bot.run("")

