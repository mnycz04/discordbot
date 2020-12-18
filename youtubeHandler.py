"""
Searches Youtube and downloads a video in .mp3 format.
"""

import youtube_dl

YTDL_OPTIONS = {'format': 'bestaudio/best',
                'extractaudio': True,
                'restrictfilenames': True,
                'outtmpl': 'music/%(id)s',
                'quiet': True,
                'noplaylist': True,
                'default_search': 'auto'}

ytdl = youtube_dl.YoutubeDL(YTDL_OPTIONS)


def download_song(query):
    """Searches youtube for a song to download"""

    song = ytdl.extract_info(query)
    song_info = []

    if 'entries' in song:
        if 'title' in song['entries'][0]:
            song_info.append(song['entries'][0]['title'])
            song_info.append(song['entries'][0]['id'])
    elif 'title' in song:
        song_info.append(song['title'])
        song_info.append(song['id'])

    return song_info
