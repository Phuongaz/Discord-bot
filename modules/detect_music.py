from youtube_search import YoutubeSearch
import json
from util import string

def detect_music(lyric):
    videos = YoutubeSearch(lyric, max_results=30).to_json()
    videos = json.loads(videos)
    titles = []
    if len (videos['videos']) == 0:
        return "Không tìm thấy bài hát nào"
    for video in videos['videos']:
        titles.append(video['title'])
    common_strings = string.find_most_common_strings(titles)

    return common_strings[0][0]
