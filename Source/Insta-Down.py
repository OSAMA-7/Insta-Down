#
# This Is Free Tool By Soud Alanzi AKA @8Y
# Dont Try Sell It Cuz It's Fucking Free
# Github: https://github.com/Soud69
# Instagram: https://instagram.com/8Y
# Telegram: https://t.me/Soud69
# Discord: Soud#5866
#

try:
    import os
    import requests
    import re
    from PIL import Image
    from os import system
    system("title " + "Soud Was Here - @8Y - Soud#5866")
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)

except Exception as m:
    print("Something Went Wrong\n")
    print(m)
    input()
    exit()
logo = f"""
{Fore.CYAN}         _______   __  {Fore.GREEN}______                    
{Fore.CYAN}   ____ |  _  \ \ / /  {Fore.GREEN}|  _  \ 
{Fore.CYAN}  / __ \ \ V / \ V /   {Fore.GREEN}| | | |_____      ___ __
{Fore.CYAN} / / _` |/ _ \  \ /    {Fore.GREEN}| | | / _ \ \ /\ / / '_ \ 
{Fore.CYAN}| | (_| | |_| | | |    {Fore.GREEN}| |/ / (_) \ V  V /| | | | 
{Fore.CYAN} \ \__,_\_____/ \_/    {Fore.GREEN}|___/ \___/ \_/\_/ |_| |_| 
{Fore.CYAN}  \____/
"""
print(logo)
print(f"{Fore.RED}This Is Free Tool By Soud Alanzi And Not For Sale\n\n{Fore.RESET}{Fore.GREEN}Instagram: @8Y + @_agf\nDiscord: Soud#5866\n")
headers = {
    "Host": "www.instagram.com",
    "Accept": "*/*",
	"Cookie": "csrftoken=rbAddmyx7MTEAGFc7X5yRxQWy4kmRNLf; ig_did=90144668-C94F-4EE5-B2D8-E6814767E6BE; ig_nrcb=1; mid=YB_cHgAEAAHIKknfB-NyN6JwpxU3",
	"User-Agent": "@8Y/Soud69",
	"Accept-Language": "en-us",
	"Accept-Encoding": "gzip, deflate, br",
	"Connection": "keep-alive"
}
try:
    req = requests.get(input("Enter Instagram Video URL: "), headers=headers)
    image = re.compile('property="og:image" content="(.*?)" />').findall(req.text)[0]
    image_result = requests.get(image, stream=True)
    video_info = re.compile('og:description" content="(.*?)" />').findall(req.text)[0]
    video = re.compile('property="og:video" content="(.*?)" />').findall(req.text)[0]
    video_result = requests.get(video, stream=True)
    q = Image.open(image_result.raw)
    print("\n\n------------------------------\n\n- Video Thumbnail\n")
    q.show()
    print("\n\n- Video Caption\n")
    print(video_info)
    with open("@8Y.mp4", "wb") as result:
        result.write(video_result.content)
    print("\n\n[+] Done Downloading Video (@8Y.MP4)\n\n------------------------------\n")
    input()
    exit()


except Exception as i:
    print("Something Went Wrong\n")
    print(i)
    input()
    exit()
