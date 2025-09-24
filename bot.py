import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import pyjokes

# Setup logging
logging.basicConfig(
    handlers=[logging.FileHandler('discord.log', 'w', 'utf-8')],
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Load environment variables-
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

if not token:
    raise ValueError("DISCORD_TOKEN not found in .env file")

#roles-
secret_role = "Gamer"#exanple

# Setup intents- 
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Create bot instance- 
bot = commands.Bot(command_prefix='/', intents=intents)


#for loading the extension
async def setup_hook():
    await bot.load_extension("spam_prevention")
bot.setup_hook = setup_hook

#some events here- 
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_member_join(member):
    print(f"{member} has joined the server. :)")

@bot.event
async def on_member_remove(member):
    print(f"{member} has left the server. :(")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # bad word filter
    bad_words = ["shit", "fuck", "motherfucker", "uncleTom", "fucker"]
    if any(word in message.content.lower() for word in bad_words):
        await message.delete()
        await message.channel.send(f"{message.author.mention}, Don't use that word!")

    # make sure commands still work
    await bot.process_commands(message)

    # forward message to SpamPrevention cog (so both filters work)
    sp = bot.get_cog("SpamPrevention")
    if sp:
        await sp.check_message(message)  

#commands here-
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello,{ctx.author.mention}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def joke(ctx):
    joke = pyjokes.get_joke()
    await ctx.send(f'joke - {joke}')

#had to rewrite this command to learn about it
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Bot Information", description="This is a sample Discord bot.", color=0x00ff00)
    embed.add_field(name="Author", value="Your Name", inline=False)
    embed.add_field(name="Version", value="1.0.0", inline=False)
    await ctx.send(embed=embed)
        
@bot.command()
async def helpme(ctx):
    help_text = """
    Here are the available commands:
    /hello - Greet the bot
    /ping - Check bot's responsiveness
    /joke - Get a random joke
    /info - Get information about the bot
    /assign - Assign yourself a secret role
    /poll - Create a yes/no poll
    """
    await ctx.send(help_text)

@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=secret_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"Role '{secret_role}' has been assigned to you, {ctx.author.mention}!")
    
    else:
        await ctx.send(f"Role does not exist. :(")

@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=secret_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"Role '{secret_role}' has been removed from you, {ctx.author.mention}!")
    else:
        await ctx.send(f"Role does not exist. :(")

@bot.command()
async def dm(ctx, *,msg):
    await ctx.author.send(f"You said: {msg}")

@bot.command()
async def reply(ctx):
    await ctx.reply("This is a reply to your message.")

@bot.command()
async def botinfo(ctx):
    await ctx.send(f"This bot was created by github-`cognitioo`.")
    await ctx.send(f"Bot's latency is {round(bot.latency * 1000)}ms.")
    await ctx.send(f"Bot is running on {len(bot.guilds)} servers.")
    await ctx.send(f"Bot version is 1.0.0.")    

@bot.command()
async def poll(ctx, *, question: str):
    """Creates a simple yes/no poll."""
    try:
        embed = discord.Embed(
            title="Poll",
            description=question,
            color=discord.Color.blurple()
        )
        poll_message = await ctx.send(embed=embed)
        await poll_message.add_reaction("👍")
        await poll_message.add_reaction("👎")
        
    except discord.Forbidden:
        await ctx.send("I don't have permission to add reactions or send embeds in this channel.")
    except discord.HTTPException as e:
        await ctx.send(f"Failed to create poll: {e}")
    except Exception as e:
        await ctx.send(f"An unexpected error occurred: {e}")
        logging.error(f"Poll command error: {e}")



# run this bot 
bot.run(token, log_level=logging.DEBUG)
