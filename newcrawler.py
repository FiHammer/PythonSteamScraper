from urllib import parse
from urllib import request

#http://api.steampowered.com/<interface name>/<method name>/v<version>/?key=<api key>&format=<format>

#https://steamcommunity.com/market/search/render/?query=&start=0&norender=1&count=10

#https://steamcommunity.com/market/priceoverview/?currency=<currencyno€=3>&appid=<csgo=730>&market_hash_name=<name of he skin with urlencode>

# %28   =   (
# %29   =   )
# %20   =   <Space>
# %7C   =   |
# %e2 %84 %a2 wird zu kleinem tm
# https://steamcommunity.com/market/priceoverview/?currency=1&appid=730&market_hash_name=AWP | Atheris (Field-Tested)
# https://steamcommunity.com/market/priceoverview/?currency=1&appid=730&market_hash_name=AWP%20%7C%20Atheris%20%28Field-Tested%29


# steamURLStart = "https://steamcommunity.com/market/priceoverfiew/currency="+ +"&appid="+ +"&market_hash_name="+ steamStickerHash +""
steamStickerHash =""
steamCurrency = "3" # 1=$, 2=£, 3=€
steamAppid = "730" # CSGO=730
steamStickerId = [
    "BIG",
    "Ninjas in Pyjamas",
    "Astralis",
    "Team Liquid",
    "Team Spirit",
    "FACEIT",
    "HellRaisers",
    "Cloud9",
    "Winstrike Team",
    "Rogue",
    "FaZe Clan"
]
params = {
        'https://Steamcommunity.com/market/priceoverfiew/':'',
        'currency': '3',
        'appid': '730',
        'market_hash_name':''
    }

steamStickerId = ["BIG","Ninjas in Pyjamas","Astralis","Team Liquid","Team Spirit","FACEIT","HellRaisers","Cloud9","Winstrike Team","Rogue","FaZe Clan"]

def AssembleStickerHash(n):
    steamStickerHash = "Sticker | "+ steamStickerId[n] +" | London 2018"
    print(steamStickerHash)
    return steamStickerHash

stickerNr = 3
def RequestPrice(n):
    # steamURLStart = "https=//steamcommunity.com/market/priceoverfiew/currency="+ steamCurrency +"&appid="+ steamAppid +"&market_hash_name="+ AssembleStickerHash(n)
    inter = ""+AssembleStickerHash(stickerNr)
    interC = ""+parse.urlencode(inter)
    steamStickerHash=params + interC
    print(steamStickerHash)
    steamItemPriceR = request.urlopen(steamStickerHash)
    print(steamItemPriceR.read())

RequestPrice(2)