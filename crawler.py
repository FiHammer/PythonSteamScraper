from urllib import request
from urllib import parse
import re

# x = request.urlopen("https://dro1de1.tk")
# if x.code==200
# print(x)
# steamWebsite = request.urlopen("https://steamcommunity.com/")
# steamObject = steamWebsite.read()
# steamText = steamObject.decode("utf-8")
# print(steamText)
SteamURLStart = "https://steamcommunity.com/market/listings/730/Sticker%20%7c%20"
SteamURLEnd = "%20%7c%20London%202018"
steamStickerName = [
    "BIG",
    "Ninjas%20in%20Pyjamas",
    "Astralis",
    "Team%20Liquid",
    "Team%20Spirit",
    "FACEIT",
    "HellRaisers",
    "Cloud9",
    "Winstrike%20Team",
    "Rogue",
    "FaZe%20Clan"
]
def generateURL(a):
    url = SteamURLStart+steamStickerName[(a)]+SteamURLEnd
    resp = request.urlopen(url)
    respData = resp.read()
    # print(respData)
    saveFile = open('steamsticker_'+steamStickerName[a]+'.html','w')
    saveFile.write(str(respData))
    saveFile.close()
    quicksellPrice = re.findall(r'<span class="market_commodity_orders_header_promote">(.*?)</span>', str(respData))
    print(quicksellPrice)
for x in range(0, len(steamStickerName)):
    generateURL(x)
# def getPriceFromURL():
    
#     return
# def getURL(a):
#     SteamSite=request.urlopen(generateURL(a)).decode("UTF-8").search()
#     '<span class="market_commodity_orders_header_promote">0,18€</span>'
#     return


# print(myFunction(3))
# steamURL = "https://steamcommunity.com/market/listings/730/"
# steamWebsite = request.urlopen("https://steamcommunity.com/market/listings/730/")
# 