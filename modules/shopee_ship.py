import asyncio
from modules import driver_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import discord
from config import *

temp_items = {}

async def listen_shopee(message):
    user_name = SHOPEE_USER_NAME
    password = SHOPEE_PASSWORD
    try:
        driver = driver_browser.get_driver()
        url_purchases = "https://shopee.vn/user/purchase/"
        driver.get(url_purchases)
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[2]/div[1]/input").send_keys(user_name)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[3]/div[1]/input").send_keys(password)
        await asyncio.sleep(10)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div/div[2]/button").click()

        wait = WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div/div[5]/div[1]")))
    except:
        await message.channel.send(f"{message.author.mention}!, somthing error, try again with command !runshopee after 5 minutes")
        return
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    rows = soup.find_all("div", {"class": "hiXKxx"})

    while True:
        embed = discord.Embed(title="DANH HÀNG ĐANG ĐƯỢC GIAO")
        for row in rows:
            status = row.find("div", {"class": "V+w7Xs"}).text
            name = row.find("span", {"class": "x5GTyN"}).text
            try:
                location = row.find("span", {"class": "nkmfr2"}).text
            except:
                location = ""
            if(status == "Đã hủy" or status == "Hoành thành"):
                continue
            if name not in temp_items:
                embed.add_field(name=name, value=location, inline=False)
                temp_items[name] = location
            else:
                if temp_items[name] == location:
                    continue
                else:
                    await message.channel.send(f"Kiểm tra đơn hàng nàyyy, <@{message.author.id}>!")
                    embed.add_field(name=name, value=location, inline=False)
                    temp_items[name] = location
                
        if len(embed.fields) > 0:
            await message.channel.send(embed=embed)
        driver.refresh()
        await asyncio.sleep(60)

async def run_shopee_thread(message):
    await listen_shopee(message)