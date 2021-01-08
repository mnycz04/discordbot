"""
Contains Function to log members
"""
import datetime


def log(member):
    """
    Logs the Epoch time that the user was active in a voice channel
    :param member: member object
    """
    elap_time: str = str(round((member.leave_time - member.join_time), 0))
    user_log_title = f"logs/log_{member.name}.txt"
    user_log = open(user_log_title, 'a')
    user_log.write(elap_time + ',\n')
    user_log.close()


def log_actions(text):
    """logs all bot actions to a file"""

    print(text)
    with open('logs/bot_log.txt', 'a') as log_file:
        log_file.write(f'\n[{datetime.datetime.now()}] {text}')
        log_file.close()
