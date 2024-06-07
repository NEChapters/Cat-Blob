import hikari
import lightbulb

sudo_plugin = lightbulb.Plugin("sudo", "Commands only super users can use")
sudo_plugin.add_checks(
    lightbulb.owner_only
)

@sudo_plugin.command
@lightbulb.command("naptime","tell catblob to take a nap")
@lightbulb.implements(lightbulb.SlashCommand)
async def naptime(ctx: lightbulb.Context) -> None:
    await ctx.respond("Cat blob is laying down for a nap now <3")
    await ctx.bot.close()
   
@sudo_plugin.command
#@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.command("test", "tells cat blob to post the announcement")
@lightbulb.implements(lightbulb.SlashCommand)
async def test(ctx: lightbulb.Context) -> None:
    embed = (
        hikari.Embed(
            title=":tada: Announcement time :tada:",
            description="Hey everyone Chapters here to come tell you happy news. Cat Blob is officially being hosted 24/7 and the basics are now set up for it. The main future plan for it is to be a bot to help us get the game servers whitelist done easier so you guys don't have to wait for one of us to be free.",
            color=0xf8f1ae,
        )
        .set_footer(
            text="Announcement from the team behind cat blob",
            icon=ctx.author.display_avatar_url,
        )
    )

    await ctx.respond(embed)

def load(bot: lightbulb.BotApp):
    bot.add_plugin(sudo_plugin)

def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(sudo_plugin)