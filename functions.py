import requests
import json

#request url
url = "https://api.tibiadata.com"

def get_players_guerribro():
    response = requests.get(url+"/v4/guild/Guerribro")
    data = json.loads(response.content) 
    players = data["guild"]["members"]
    onlineplayers = []
    for player in players:
        if player["status"] == "online":
            onlineplayers.append({"name":player["name"],"level":player["level"],"vocation":player["vocation"],"guild":"Guerribro"})
    onlineplayers.sort(reverse=True,key=lambda x: x["level"])
    return onlineplayers

def get_all_players_with_guilds():
    response = requests.get(url+"/v4/world/Guerribra")
    data = json.loads(response.content) 
    players = data["world"]["online_players"]
    players.sort(reverse=True,key=lambda x: x["level"])
    for player in players:
        formattedname = player["name"].replace(" ","%20")
        response = requests.get(url+"/v4/character/"+formattedname)
        data = json.loads(response.content) 
        player_guild = data["character"]["character"]["guild"]
        if player_guild:
            player["guild"] = player_guild["name"]
        else:
            player["guild"] = "none"
    return players

def get_all_players():
    response = requests.get(url+"/v4/world/Guerribra")
    data = json.loads(response.content) 
    players = data["world"]["online_players"]
    players.sort(reverse=True,key=lambda x: x["level"])
    return players