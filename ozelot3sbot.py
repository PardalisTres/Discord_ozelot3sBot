import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


description = "Ozelot_3's discord bot."

startup_extensions = ["blaetterrauschen", "heroquest", "tucana"]

bot = commands.Bot(command_prefix='?', description=description)


@bot.event
async def on_ready():
    print('Logged in as {} with id {}'.format(bot.user.name, bot.user.id))


@bot.command()
async def load(ctx, extension_name: str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
        print('Loaded extension {}.'.format(extension))
    except (AttributeError, ImportError) as e:
        await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await ctx.send("{} loaded.".format(extension_name))


@bot.command()
async def unload(ctx, extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    print('Unloaded extension {}.'.format(extension))
    await ctx.send("{} unloaded.".format(extension_name))


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    if "TOKEN" in os.environ.keys():
        token = os.getenv("TOKEN")
        bot.run(token)
    else:
        print("token not found!")
