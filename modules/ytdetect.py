import datetime
import time
import youtube_dl
import re
import config

TYPE="NOHOOK"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0 PaleMoon/27.5.1"}

def Parser(user, url):
    ytdl = youtube_dl.YoutubeDL({})
    y = ytdl.extract_info(url, download=False)
    t= datetime.datetime.min.strptime(y['upload_date'], "%Y%m%d").strftime("%x")
    return "<%s> \x02%s\x02 - %s - \x02%s\x02 - %s - \x02%s views\x02 - (\x0303+%d\x03 \x0304-%d\x03)" %\
           (user, y['title'], time.strftime('%H:%M:%S', time.gmtime(y['duration'])), y['uploader'], t, y["view_count"], y['like_count'], y['dislike_count'])

def Main(self, line, user):
    match = re.search(r"(?:youtube\.com|youtu\.be|hooktube\.com)\/(?:watch\?v=)?([A-Za-z0-9_-]{11})", " ".join(line[3:]))
    if match:
        parsed = Parser(user, match.group(1))
        self.SendMsg(line[2], parsed)
