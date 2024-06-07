import datetime

import hikari
import lightbulb

import config

join_plugin = lightbulb.Plugin("join", "plugin that hanndles welcome and leave embeds")

async def log_embed_join(event,member):
    guild_id = event.guild_id
    member_count = join_plugin.bot.rest.fetch_members(guild_id)
    member_count_int = await member_count.count()

    log_join_embed = hikari.Embed(
        title= event.guild_id,
        description=f"**User:** {member.mention} | {member.username}\n**ID:** {member.id}\n**Count:** {member_count_int}",
        colour=hikari.Colour(0x4cbb64),
    )
    log_join_embed.set_footer(
        text=(f"Time: {datetime.datetime.now().strftime('%H:%M')}"))
    
    #log_channel = await join_plugin.bot.rest.fetch_channel(config.log_channel_id)
    await join_plugin.bot.rest.create_message(channel=config.log_channel_id,embed=log_join_embed)


async def log_embed_leave(event, member):
    guild_id = event.guild_id
    member_count = join_plugin.bot.rest.fetch_members(guild_id)
    member_count_int = await member_count.count()

    log_join_embed = hikari.Embed(
        title="User Leave",
        description=f"**User:** {member.mention} | {member.username}\n**ID:** {member.id}\n**Count:** {member_count_int}",
        color="#ff6669",
    )
    log_join_embed.set_footer(
        text=(f"Uhrzeit: {datetime.datetime.now().strftime('%H:%M')}"))

    #log_channel = await fetch_channel_from_id(log_channel_id)
    await join_plugin.bot.rest.create_message(channel=config.log_channel_id, embed=log_join_embed)


def load(bot: lightbulb.BotApp):
    bot.add_plugin(join_plugin)

def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(join_plugin)

