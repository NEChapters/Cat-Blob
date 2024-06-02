import random
import hikari
import lightbulb

fun_plugin = lightbulb.Plugin("Fun", "Commands that are fun")

@fun_plugin.command
@lightbulb.command("hugs", "A command group that deals with hugs")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def hugs(ctx):
    pass

@hugs.child
@lightbulb.add_cooldown(5, 1, lightbulb.UserBucket)
@lightbulb.command("get","Get a hug from Vat Blob")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def get(ctx: lightbulb.Context) -> None:
    x_hugs = str(random.randint(1,10000))
    bot_mention = fun_plugin.bot.get_me().mention
    await ctx.respond(f"{bot_mention} hugged you {x_hugs} times", user_mentions= True)

@hugs.child
@lightbulb.add_cooldown(5, 1, lightbulb.UserBucket)
@lightbulb.option("who", "Who do you want to hug?", hikari.User, required=True)
@lightbulb.command("give", "Give a hug to someone <3")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def give_hug(ctx: lightbulb.Context) -> None:
    hugger = ctx.member.mention
    hugged = ctx.get_guild().get_member(ctx.options.who).mention
    x_hugs = str(random.randint(1, 10000))
    await ctx.respond(f"{hugger} gave {hugged} {x_hugs} hugs.", user_mentions = True)

@fun_plugin.command
@lightbulb.command("tickle", "tickle the bot")
@lightbulb.implements(lightbulb.SlashCommand)
async def tickle(ctx: lightbulb.Context) -> None:
    randomize = random.randint(1, 5)
    if ctx.author.id in fun_plugin.bot.owner_ids:
        await ctx.respond("hey you should know better than to tickle me")
    elif randomize == 1:
        await ctx.respond("oi stop")
    elif randomize != 1:
        await ctx.respond(":joy_cat::joy_cat::joy_cat:")

def load(bot: lightbulb.BotApp):
    bot.add_plugin(fun_plugin)

def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(fun_plugin)