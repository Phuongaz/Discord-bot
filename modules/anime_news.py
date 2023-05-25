import asyncio
from bs4 import BeautifulSoup
import discord
import requests

temp_animes = {}

async def listen_anime47(anime_channel):
    
    white_list = [
        "https://anime47.com/phim/kimi-wa-houkago-insomnia/m8993.html",
        "https://anime47.com/phim/dead-mount-death-play/m9000.html",
        "https://anime47.com/phim/kimetsu-no-yaiba-katanakaji-no-sato-hen/m8978.html",
        "https://anime47.com/phim/tensei-kizoku-no-isekai-boukenroku-jichou-wo-shiranai-kamigami-no-shito/m8998.html",
        "https://anime47.com/phim/niehime-to-kemono-no-ou/m9008.html",
        "https://anime47.com/phim/yamada-kun-to-lv999-no-koi-wo-suru/m8984.html",
        "https://anime47.com/phim/isekai-de-cheat-skill-wo-te-ni-shita-ore-wa-genjitsu-sekai-wo-mo-musou-suru-level-up-wa-jinsei-wo-kaeta/m8988.html",
        "https://anime47.com/phim/jigokuraku/m8980.html",
        "https://anime47.com/phim/mahoutsukai-no-yome-season-2/m8987.html",
        "https://anime47.com/phim/dr-stone-new-world/m8979.html",
        "https://anime47.com/phim/mashle/m8985.html"
    ]
    
    url = "https://animevietsub.im/lich-chieu-phim.html"
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'html.parser')
    
    for anime in white_list:
        url = anime
        content = requests.get(url).content
        soup = BeautifulSoup(content, 'html.parser')
        movie_info = soup.find("div", {"class": "movie-info"})
        title = movie_info.find("span", {"class": "title-1"}).text
        status = movie_info.find("dd", {"class": "movie-dd imdb"}).text
        image = movie_info.find("div", {"class": "movie-l-img"}).find("img")["src"]
        if anime not in temp_animes:
            temp_animes[anime] = []
            temp_animes[anime].append({
                "title": title,
                "status": status,
                "image": image,
            })
        else:
            status = movie_info.find("dd", {"class": "movie-dd imdb"}).text
            if temp_animes[anime][0]["status"] == status:
                continue
            else:
                temp_animes[anime][0]["status"] = status
                embed = discord.Embed(title=title)
                embed.set_image(url=image)
                embed.add_field(name="Cập nhật tập mới", value=status.replace("/??", ""))
                await anime_channel.send(embed=embed)
        
async def listen(anime_channel):
    while True:
        await listen_anime47(anime_channel)
        await asyncio.sleep(60 * 60)
