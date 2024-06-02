import os
import time
from datetime import datetime

import dotenv
import hikari
import lightbulb
from hikari import Intents

dotenv.load_dotenv()

INTENTS = Intents.GUILD_MEMBERS | Intents.GUILDS

bot = lightbulb.BotApp(
    token= os.environ["TOKEN"],
    default_enabled_guilds=int(os.environ["GUILD_ID"]),
    owner_ids=os.environ["OWNER_ID"],
    help_slash_command=True,
    banner= None,
)

# Checks if the bot is alive and response time
@bot.command
@lightbulb.command("ping", "messure the ping of the bot", auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    heartbeat=ctx.bot.heartbeat_latency*1000
    txt=":ping pong: Pong!"

    if heartbeat >  1000:
        colour = hikari.Colour(0xFF0000)
    elif heartbeat > 500:
        colour = hikari.Colour(0xFFFF00)
    else:
        colour = hikari.Colour(0x26D934)
    
    emebed = hikari.Embed(
        title="__Current Ping__",
        description=f"```💓:{heartbeat:,.2f}ms.```",
        timestamp=datetime.now().astimezone(),
        colour=colour,
    )
    await ctx.respond(emebed=emebed, content=txt)

@bot.command
@lightbulb.command(
    name="pong",
    description="Displays the ping/latency of the bot",
)
@lightbulb.implements(lightbulb.SlashCommand)
async def pong(ctx: lightbulb.Context) -> None:
    # Check the heartbeat latency of the bot
    start = time.perf_counter()
    message = await ctx.respond(
        f"Pong! 🏓 \n" f"Ws Latency: **{ctx.bot.heartbeat_latency * 1000:.0f}ms**"
    )
    end = time.perf_counter()

    await message.edit(
        f"Pong! 🏓 \n"
        f"Gateway: **{ctx.bot.heartbeat_latency * 1000:,.0f}ms**\n"
        f"REST: **{(end-start)*1000:,.0f}ms**"
    )







# loads all extensions files
bot.load_extensions_from("./extensions/")

# this secontion hanndle all command errors
@bot.listen(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:
    exception=event.exception.__cause__ or event.exception
    if isinstance(exception, lightbulb.CommandInvocationEvent):
        await event.context.respond(f"Something went wrong during invocation of command `{event.context.command.name}`.")
    elif isinstance(exception, lightbulb.CommandIsOnCooldown):
        await event.context.respond(f"This command is on cooldown. Retry in `{exception.retry_after:.2f}` seconds.")
    # covers error for user missing a permission
    elif isinstance(exception, lightbulb.MissingRequiredPermission):
        await event.context.respond("You are missing one or more permissions to use this command.")
    # covers error for bot missing a permission
    elif isinstance(exception, lightbulb.BotMissingRequiredPermission):
        await event.context.respond("The bot is missing one ore more permissions to preform this commnad.")
    # covers error for owner only commad
    elif isinstance(exception, lightbulb.NotOwner):
        await event.context.respond("This command is only able to be used by the bot owner")
    else:
        raise exception
    
if __name__ == "__main__":
    bot.run(
        status = hikari.Status.IDLE,
        # sets the status for the bot
        activity = hikari.Activity(
            name="for the longest nap",
            type=5,
            # type controls the activity type
            # 0 is playing(shows as 'Playing....')
            # 1 is streaming (shows as 'Streaming ...')
            # 2 is listening (shows as 'Listening to....')
            # 4 is custom (does not work with bots)
            # 5 is competing(shows as 'Listening to')
            #url = "https://www.twitch.tv/neverendingchapters" # have to provide a youtube or twitch link for streaming)
        )
        )