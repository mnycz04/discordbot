"""
Calculates the type of voice change that was detected and executes respective actions
"""

import time
import logger as log

current_member = None


class InvalidUserError(Exception):
    """
    Error when an Invalid User is tried to be logged. A bot normally
    """
    pass


def voip_change_main(member, before, after, guild, server):
    """
    checks if user was a bot
    :param member: member object
    :param before: voice state before change
    :param after: voice state after change
    :param guild: guild change was detected in
    :param server: server object
    :return: returns either a new command to execute action to log, or does nothing
    """
    if not member.bot:
        return voip_change_logic(member, before, after, guild, server)
    else:
        raise InvalidUserError


def voip_change_logic(member, before, after, guild, server):
    """
    Detects the type of voice state change that was detected
    :param member: member object
    :param before: voice state before change
    :param after: voice state after change
    :param guild: guild change was detected in
    :param server: server object
    :return: Returns the respective action based on the change that was detected
    """
    if str(before.channel) == str(after.channel):
        return None
    elif str(before.channel) == 'None' and str(after.channel) != 'None':
        return voip_change_join(member, guild, server)
    elif str(before.channel) != 'None' and str(after.channel) == 'None':
        return voip_change_leave(member, guild, server)
    elif str(before.channel) != 'None' and str(after.channel) == 'AFK':
        return voip_change_goafk(member, guild, server)
    elif str(before.channel) == 'AFK' and str(after.channel) != 'None':
        return voip_change_returnafk(member, guild, server)


def voip_change_join(member, guild, server):
    """
    If the change was a user joining a voice channel, runs logic to log the users join time
    :param member: member object
    :param guild: guild change was detected in
    :param server: server object
    :return:
    """
    global current_member
    join_time = time.time()
    for i in range(len(guild.members)):
        if int(member.id) == int(server.guild_members[i].id):
            current_member = server.guild_members[i]
            break
        else:
            continue
    print(f'{current_member.name} has joined. {time.strftime("%a %b %d %H:%M:%S", time.localtime())}')
    current_member.join_time = join_time
    return current_member


def voip_change_leave(member, guild, server):  # Logs if user leaves VOIP
    """
    If the change was a user leaving, logs the leave time and runs a log function
    :param member: member object
    :param guild: guild change was detected in
    :param server: server object
    :return:
    """
    global current_member
    leave_time = time.time()
    for i in range(len(guild.members)):
        if int(member.id) == int(server.guild_members[i].id):
            current_member = server.guild_members[i]
            break
        else:
            continue
    print(f'{current_member.name} has left. {time.strftime("%a %b %d %H:%M:%S", time.localtime())}')
    current_member.leave_time = leave_time
    log.log(current_member)
    return current_member


def voip_change_goafk(member, guild, server):  # Logs when user goes AFK
    """
    If user went AFk, logs action.
    :param member: member object
    :param guild: guild change was detected in
    :param server: server object
    :return:
    """
    global current_member
    leave_time = time.time()
    for i in range(len(guild.members)):
        if int(member.id) == int(server.guild_members[i].id):
            current_member = server.guild_members[i]
            break
        else:
            continue
    print(f'{current_member.name} has gone AFK. {time.strftime("%a %b %d %H:%M:%S", time.localtime())}')
    current_member.leave_time = leave_time
    log.log(current_member)
    return current_member


def voip_change_returnafk(member, guild, server):  # Logs when user returns from AFK
    """
    If a user returns from AFK, logs action
    :param member: member object
    :param guild: guild change was detected in
    :param server: server object
    :return:
    """
    global current_member
    join_time = time.time()
    for i in range(len(guild.members)):
        if int(member.id) == int(server.guild_members[i].id):
            current_member = server.guild_members[i]
            break
        else:
            continue
    print(f'{current_member.name} has returned from being AFK. {time.strftime("%a %b %d %H:%M:%S", time.localtime())}')
    current_member.join_time = join_time
    return current_member
