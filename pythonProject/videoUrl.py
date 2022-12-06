import urllib.request
import re
from urllib.parse import quote

class VideoUrl:

    def get_video_url(keyword):
        youtube_query = 'https://www.youtube.com/results?search_query='
        search_keyword = keyword.decode('utf-8')
        search_keyword = search_keyword.replace(" ", "+")
        url = youtube_query + quote(search_keyword)

        html = urllib.request.urlopen(url)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

        video_url = "https://www.youtube.com/watch?v=" + video_ids[0]

        return video_url
