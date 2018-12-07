import config
import os

TYPE = 'MESSAGE'
HOOK = 'music'
HELP = config.H(HOOK, ": Returns a song from a small music DB.")

writers = ["failure", "pheni", "xorswap", "markthenerd", "riversofstars"]
songs = []

if not os.path.isfile("data/music.txt"):
    with open("data/music.txt", "w") as f: f.close()
with open("data/music.txt") as f:
    for song in f.readlines():
        if song.rstrip(): songs.append(song.rstrip())

def Main(self, line, user):
    if len(line) <= 4:
        return random.choice(songs)
    elif user.lower() in writers:
        with open("data/music.txt", "a") as f:
            f.write(line[4]+"\n")
            f.close()
        songs.append(line[4])
        return "Song added."
