"""
Module for getting the information of guild members
"""

import discord
import time
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='$', intents=intents)
channels = None


class Person:
    """
    Creates a object for members of a discord guild
    """
    def __init__(self, name, id_num, is_bot,  join_time=None, leave_time=None):
        self.name = name
        self.id = id_num
        self.is_bot = is_bot
        self.join_time = join_time
        self.leave_time = leave_time

    def __hash__(self):
        return hash(self)


class GuildInfo:
    """
    Creates object that contains all of the info of the guild, such as:
        ids of all members
        names of all members
        the members object
    """
    def __init__(self, guild_ids, guild_names, guild_members):
        self.guild_ids = guild_ids
        self.guild_names = guild_names
        self.guild_members = guild_members

    def __hash__(self):
        return hash(self)


def get_server_members(guild):
    """
    Function that gets a list of all server members:
        ids
        names
        objects
    :param guild: guild id
    :return: Returns an object containing lists of all the guild members info
    """
    global channels
    join_time = time.time()
    guild_members = []
    guild_ids = []
    guild_names = []
    for member in guild.members:
        guild_names.append(str(member.name))
        guild_ids.append(int(member.id))
        continue
    for i in range(len(guild_names)):
        guild_person = Person(guild_names[i], guild_ids[i], guild.members[i].bot)
        guild_members.append(guild_person)
        continue
    for i in range(len(guild.channels)):
        channels = [channel for channel in guild.voice_channels]
    for i in range(len(channels)):
        channel = channels[i]
        channel_members = channel.members
        if channel_members:
            for j in range(len(channel_members)):
                member = channel_members[j].name
                for k in range(len(guild_members)):
                    if member == guild_members[k].name:
                        guild_members[k].join_time = join_time
                        break
    guild_current = GuildInfo(guild_ids, guild_names, guild_members)
    return guild_current

