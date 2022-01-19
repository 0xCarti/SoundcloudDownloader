from sclib import SoundcloudAPI
import sys

if len(sys.argv) == 0:
    print("Please enter a URL to download.")
    sys.exit(0)

track = SoundcloudAPI().resolve(str(sys.argv[0]))
filename = f'D:/Plex-Media/Music/{track.artist} - {track.title}.mp3'
with open(filename, 'wb+') as fp:
    track.write_mp3_to(fp)
    print("Track finished downloading.")
