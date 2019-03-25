import requests
import datetime

stickers = [
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


def make_url(stick: str):
    """
    gibt den Link der Steamapi zurück

    :param stick: der Sticker name
    :return: gibt den Link zurück
    """
    url = "https://steamcommunity.com/market/priceoverview/?currency=1&appid=730&market_hash_name=Sticker%20|%20" + \
          stick + "%20|%20London%202018"
    return url


def return_dir(url: str):
    """
    gibt das dir mit den Daten der Website zurück

    :param url: url der API (+Info)
    :return: dir der Daten
    """

    return requests.get(url).json()


print(datetime.datetime.now().strftime("%H:%S:%M") + ": ")
for stick in stickers:
    myDir = return_dir(make_url(stick))
    if myDir and myDir.get("success"):
        print(stick.title() + ": " + myDir["lowest_price"])
    else:
        print(stick.title() + ": NICHT GEFUNDEN!")

