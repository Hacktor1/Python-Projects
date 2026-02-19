import discord
from discord.ext import commands
from discord import app_commands
import json
import os


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


FILE = "config.json"

DEFAULT_MESSAGE = "👋 Welcome to **{server}**, {user}!"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def is_admin(interaction: discord.Interaction) -> bool:
    return interaction.user.guild_permissions.manage_guild


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")


hello = app_commands.Group(
    name="hello",
    description="Welcome system configuration"
)


@hello.command(name="add", description="Set this channel as welcome channel")
async def hello_add(interaction: discord.Interaction):
    if not is_admin(interaction):
        await interaction.response.send_message(
            "❌ You need **Manage Server** permission.",
            ephemeral=True
        )
        return

    data = load_data()
    gid = str(interaction.guild.id)

    if gid not in data:
        data[gid] = {}

    data[gid]["channel"] = interaction.channel.id
    data[gid].setdefault("message", DEFAULT_MESSAGE)
    save_data(data)

    await interaction.response.send_message(
        "✅ This channel is now the welcome channel.",
        ephemeral=True
    )


@hello.command(name="remove", description="Disable welcome messages")
async def hello_remove(interaction: discord.Interaction):
    if not is_admin(interaction):
        await interaction.response.send_message(
            "❌ You need **Manage Server** permission.",
            ephemeral=True
        )
        return

    data = load_data()
    gid = str(interaction.guild.id)

    if gid in data:
        del data[gid]
        save_data(data)

        await interaction.response.send_message(
            "❌ Welcome system disabled.",
            ephemeral=True
        )
    else:
        await interaction.response.send_message(
            "ℹ️ Welcome system is not configured.",
            ephemeral=True
        )


@hello.command(name="setmessage", description="Set custom welcome message")
@app_commands.describe(message="Use {user} and {server}")
async def hello_setmessage(interaction: discord.Interaction, message: str):
    if not is_admin(interaction):
        await interaction.response.send_message(
            "❌ You need **Manage Server** permission.",
            ephemeral=True
        )
        return

    data = load_data()
    gid = str(interaction.guild.id)

    if gid not in data or "channel" not in data[gid]:
        await interaction.response.send_message(
            "⚠️ Set a welcome channel first using `/hello add`.",
            ephemeral=True
        )
        return

    data[gid]["message"] = message
    save_data(data)

    await interaction.response.send_message(
        "✅ Welcome message updated.",
        ephemeral=True
    )


@hello.command(name="show", description="Show current welcome configuration")
async def hello_show(interaction: discord.Interaction):
    data = load_data()
    gid = str(interaction.guild.id)

    if gid not in data:
        await interaction.response.send_message(
            "ℹ️ Welcome system is not configured.",
            ephemeral=True
        )
        return

    channel = interaction.guild.get_channel(data[gid]["channel"])
    message = data[gid]["message"]

    embed = discord.Embed(
        title="👋 Welcome Configuration",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="Channel",
        value=channel.mention if channel else "Unknown",
        inline=False
    )
    embed.add_field(
        name="Message",
        value=message,
        inline=False
    )

    await interaction.response.send_message(embed=embed, ephemeral=True)

bot.tree.add_command(hello)


@bot.event
async def on_member_join(member):
    data = load_data()
    gid = str(member.guild.id)

    if gid not in data:
        return

    channel = member.guild.get_channel(data[gid]["channel"])
    if not channel:
        return

    msg = data[gid]["message"]
    msg = msg.replace("{user}", member.mention)
    msg = msg.replace("{server}", member.guild.name)

    embed = discord.Embed(
        description=msg,
        color=discord.Color.green()
    )
    embed.set_thumbnail(url=member.display_avatar.url)

    await channel.send(embed=embed)


bot.run("BOT_TOKEN")