"""
A Bot for tracking who joins/leaves a discord voice channel,
as well as adding a several other functions such as weather tracking and morse code transcription.
"""

import random as rand
import time

import discord
from discord.ext import commands

import logger
import members as persons
import morsecode
import reddit
import voipstates
import weather as weth
from mytoken import TOKEN
import youtubeHandler
from schedule import check_time

__author__ = 'Michael Nycz'
__version__ = '5.2.2'

print(f'{__author__} [{__version__}]')

server = None
guild = None
local_time = time.strftime("%a %b %d %H:%M:%S", time.localtime())
intents = discord.Intents.default()
intents.members = True
intents.messages = True
client = commands.Bot(command_prefix='$', intents=intents)
degree_sign = u'\N{DEGREE SIGN}'


@client.event
async def on_ready():
    """
    Prompts Discords API for Bot connection
    """
    try:
        global server, guild
        guild = client.get_guild(576195727974203413)
        print('Bot is ready.')
        server = persons.get_server_members(guild)
    except RuntimeError:
        raise RuntimeError('Unable to initialize guild.')


@client.command(aliases=['r', 'sub'])
async def red(ctx, sub='memes'):
    """
    Gets a random post from a designated subreddit

    :param ctx: Text channel command was used in
    :param sub: Subreddit to get post from
    """
    await ctx.message.delete()
    logger.log_actions(f'{ctx.message.author.name} requested a reddit post from the r/{sub} subreddit.')

    try:
        post = await reddit.reddit_post(sub)
    except ConnectionRefusedError:
        await ctx.send('Invalid sub name. Try again', delete_after=3.0)
        logger.log_actions(f'{ctx.author.name} entered an invalid name.')
        return None
    except discord.ext.commands.errors.CommandInvokeError:
        await ctx.send('Invalid sub name. Try again', delete_after=3.0)
        logger.log_actions(f'{ctx.author.name} entered an invalid name.')
        return None
    try:
        video = False
        embed = discord.Embed(title=post.title, url=post.shortlink)
        if '.jpg' in post.url:
            embed.set_image(url=post.url)
        elif ('v.redd.it' in post.url) or ('youtu' in post.url):
            video = True
        embed.set_author(name=post.author.name)
        embed.set_footer(text=f'r/{sub}')
        await ctx.send(embed=embed)
        if video:
            await ctx.send(post.url)
    except Exception:
        await ctx.send('Invalid sub name. Try again', delete_after=3.0)
        logger.log_actions(f'{ctx.author.name} entered an invalid name.')
        return None


@client.command()
async def test(ctx, arg="I'm Ready!"):
    await ctx.send(arg, delete_after=3.0)
    await ctx.message.delete(delay=3.0)


@client.event
async def on_voice_state_update(member, before, after):
    """
    Detects a voice state update in the guild's voice channels

    :param member: An object with the users name, discord id, and other information
    :param before: An object with the previous voice state of the user
    :param after: An object with the final end state of the user
    """
    global server, guild
    try:
        voipstates.voip_change_main(member, before, after, guild, server)
    except RuntimeError:
        logger.log_actions(RuntimeWarning('Failed to log.'))
    except voipstates.InvalidUserError:
        pass


@client.command(aliases=['w'])
async def weather(ctx, *args):
    """
    Triggers command to retrieve weather information from Open Weather Maps API
    :param ctx: context
    """

    city_name: str = ' '.join(args[:])
    if not city_name:
        city_name = 'Toms River'
    city_name = city_name.title()

    logger.log_actions(f'Weather report requested by {ctx.author.name}, for {city_name}')
    await ctx.message.delete()

    try:
        city = weth.get_weather_for_city(city_name)
    except ConnectionRefusedError:
        await ctx.send('Unable to retrieve information, please check your spelling and try again.', delete_after=5.00)
        return None
    except RuntimeError:
        await ctx.send('Internal Error. Please try again. If this continues to happen, contact the author.',
                       delete_after=5.0)
        return None

    embed = discord.Embed(title=f'{city.city_name}',
                          description=f'''
                                        :thermometer: Temperature: {city.temperature} F
                                        :gloves: Feels Like: {city.feels_like} F
                                        :droplet: Humidity: {city.humidity}%
                                        :compression: Pressure: {city.pressure} hPa
                                        
                                        Wind:
                                        :wind_blowing_face: Speed: {city.wind_speed} mph
                                        :compass: Direction: {city.wind_direction}{degree_sign}
                                        
                                        Report:
                                        {city.report.capitalize()}''')
    await ctx.send(embed=embed)


@client.command(aliases=['rand'])
async def random(ctx, lower_bound=0.0, upper_bound=100.0):
    """
    returns a random integer value between the two bounds
    :param ctx: context of command
    :param lower_bound: int that specifies the lower bound of the random function
    :param upper_bound: int the specifies the upper bound of the random function
    """
    await ctx.message.delete()

    logger.log_actions(f'{ctx.author.name} requested a random number between {lower_bound} and {upper_bound}.')
    try:
        if (int(lower_bound) != lower_bound) or (int(upper_bound) != upper_bound):
            raise ValueError
        else:
            number = rand.randint(int(lower_bound), int(upper_bound))
        await ctx.send(f'Your number is {number}.')
    except ValueError:
        await ctx.send('Error: you entered an invalid number. Make sure you enter two integers.', delete_after=3.0)
        return None
    except RuntimeError:
        await ctx.send('Unknown error: try again.', delete_after=3.0)
        return None


@client.command(aliases=['sar'])
async def sarcasm(ctx, *, args=None):
    """
    Makes a phrase look sarcastic
    :param ctx: Context
    :param args: The phrase
    """
    try:
        await ctx.message.delete()
        logger.log_actions(f'{ctx.author.name} used the sarcasm command.')
        phrase = """""".join(args[:])
        new_phrase = """"""

        for char in phrase:
            chance = rand.random()
            if chance >= .5:
                new_phrase += char.lower()
            else:
                new_phrase += char.upper()

        await ctx.send(new_phrase)
    except Exception:
        await ctx.send('Error sending message.')


@client.event
async def on_message(message):
    """
    Mocks Bryan
    :param message: the message object
    """
    chance = rand.random()
    reply = """"""
    if chance <= 1.0:
        if message.author.name == 'Breezus':
            await message.delete()
            logger.log_actions('Bryan has been mocked.')
            string_message = f"""{message.content}"""
            string_message = string_message.strip()
            for char in string_message:
                chance = rand.random()
                if chance > .5:
                    reply += char.lower()
                else:
                    reply += char.upper()

            await message.channel.send(f'{reply} -Breezus 2020')
        else:
            pass
    else:
        pass

    await client.process_commands(message)


@client.command(aliases=['purge'])
async def delete(ctx, messages=100):
    """
 Bulk deletes messages
    :param ctx: Context
    :param messages: number of messages to delete
    """
    await ctx.message.delete()

    try:
        logger.log_actions(f'{ctx.author.name} used bulk delete in {ctx.channel.name} for {messages} messages.')
        await ctx.channel.purge(limit=messages, bulk=True)
    except Exception:
        await ctx.send('Unable to purge messages')


@client.command(aliases=['m', 'morsecode'])
async def morse(ctx, *, phrase=None):
    """
    Converts a string to morse code

    :param ctx: context
    :param phrase: The Phrase to translate
    :return: Returns a morse code translation
    """

    await ctx.message.delete()

    phrase = """ """.join(phrase[:])
    phrase = phrase.upper()
    logger.log_actions(f'{ctx.message.author.name} has requested morse code for {phrase}.')

    morse_code = morsecode.convert_to_morse_code(phrase)
    await ctx.send(morse_code)


@client.command(aliases=['mcc', 'halo'])
async def masterchief(ctx):
    """
    Plays the halo theme song in a voice channel
    """
    await ctx.message.delete()
    logger.log_actions(f'{ctx.author.name} has played the Halo Theme Song')
    if client.voice_clients:
        return None

    channel = ctx.author.voice.channel
    await channel.connect()

    voice_client = discord.utils.get(client.voice_clients)
    audio_source = discord.FFmpegPCMAudio('mcc.mp3')
    voice_client.play(audio_source)


@client.command(aliases=['join'])
async def summon(ctx):
    """Joins a voice channel as a voice client."""

    await ctx.message.delete()

    if client.voice_clients:
        return None

    channel = ctx.author.voice.channel
    await channel.connect()


@client.command(aliases=['p'])
async def play(ctx, *, query=None):
    """
    Finds a music youtube video and downloads it using FFmpeg
    """
    await ctx.message.delete()

    if client.voice_clients:
        pass
    else:
        channel = ctx.author.voice.channel
        await channel.connect()

    voice_client = discord.utils.get(client.voice_clients)
    if not voice_client.is_playing():
        query = """""".join(query[:])
        song_info = youtubeHandler.download_song(query)
        logger.log_actions(f'{ctx.message.author.name} has played {song_info[0]}.')
        song_location = discord.FFmpegPCMAudio(f"music/{song_info[1]}.webm")
        voice_client.play(song_location)
    else:
        await ctx.send('Playing song already', delete_after=2.0)


@client.command(aliases=['shed'])
async def schedule(ctx):
    """Returns an image of our school Hybrid Schedule"""

    await ctx.message.delete()
    logger.log_actions(f'{ctx.message.author.name} requested the schedule.')

    embed = discord.Embed(title=f'{check_time().current_period}')
    embed.set_image(url="https://i.imgur.com/IdLNJW0.png")
    embed.set_footer(text=f'{check_time().next_period}')

    await ctx.send(embed=embed, delete_after=10)


client.run(TOKEN)
