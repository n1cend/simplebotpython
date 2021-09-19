#имортишь всю iyzue чтобы не залететь в ModuleNotFoundError
import discord
from discord.ext import commands
from discord_buttons_plugin import *
import os

client = commands.Bot(command_prefix=commands.when_mentioned_or("!"))
buttons = ButtonsClient(client)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

#командыкнопочкикнопочкикнопочки
@buttons.click
async def services(ctx):
    await ctx.reply("Все что Вам требуется")

@buttons.click
async def rec(ctx):
    await ctx.reply("""Прекрасная ныне погода

        """)

@buttons.click
async def fisting(ctx):
    await ctx.reply("Next door")

@buttons.click
async def gay_sex(ctx):
    await ctx.reply("lan")
    
#кнопочкикнопочкикнопочки
@client.command()
async def hi(ctx):
    await buttons.send(
        content="Hey there",
        channel = ctx.channel.id,
        components = [
            ActionRow([
                Button(
                    style = ButtonType().Success,
                    label = "Услуги",
                    custom_id = "services"
                    )
            ])
        ]
    )

@client.command()
async def ass(ctx):
    await buttons.send(
        content = "реквизиты или fisting",
        channel = ctx.channel.id,
        components = [
            ActionRow([
                Button(
                    style = ButtonType().Success,
                    label = "Ввести реквизиты",
                    custom_id = "rec"

                ),

                Button (
                    style = ButtonType().Danger,
                    label = "fisting",
                    custom_id = "fisting"
                    )    
                ])
        ]
        )

client.run(cen)
#https://www.tiktok.com/@anastasia_yseeva_17/video/7005267461754850562?is_copy_url=0&is_from_webapp=v1&sender_device=pc&sender_web_id=6953694988597822982
