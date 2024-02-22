import datetime
import discord
from discord import ui
from discord import Member
from discord.ext import commands
from discord.ext.commands import has_role, MissingPermissions

import Manager as mgr

# Point Bot Main Class

# test

# Role that is allowed to use the Point Bot
pointRole = 'POINT_GOD'

# =======================================================================
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or('pb.'), intents=intents)


class UserList(discord.ui.UserSelect):
    def __init__(self, event, indicator):
        self.event = event
        self.indicator = indicator
        # The placeholder is what will be shown when no option is chosen
        super().__init__(placeholder='Select Users', min_values=0, max_values=100)

    async def callback(self, interaction: discord.Interaction):
        pass


class UserListView(discord.ui.View):
    def __init__(self, eventName, indicator):
        super().__init__()
        # Adds the dropdown to the view object.
        self.add_item(UserList(eventName, indicator))


# ======================================================================


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command(description="Sends Point Bot latency")
async def ping(ctx):
    await ctx.send(f"Pong! Latency is {bot.latency}")


@bot.command(name='menu', description='Opens the UI for the Point Bot.')
@commands.has_any_role(pointRole)
async def menu(ctx):
    pass


@bot.command(name='point-event', description='Creates a new event.')
@commands.has_any_role(pointRole)
async def point_event(ctx, eventName: str):
    await ctx.send(f'Creating event {eventName}...')
    await ctx.send(f'Who is participating in {eventName}?')
    view = UserListView(eventName, 'participating')
    await ctx.send('Select users:', view=view)

# =======================================================================
with open('token.txt', 'r') as file:
    token = file.readline().strip()
bot.run(token)
# =======================================================================
