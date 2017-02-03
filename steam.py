import json
import requests
import requests_cache
from decimal import *
getcontext().prec = 2

requests_cache.install_cache('api_cache')

APIPATH = r'C:\api_keys.json'
cred = json.load(open(APIPATH))

STEAM_API_URL = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002"
STEAM_API_KEY = cred["STEAM_API_KEY"]


def get_persona_name(username):
   # get custom player summary using key and provided user ID
   player_summary =  requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={0}&steamids={1}".format( STEAM_API_KEY, username)).json()
   # drill down into player summary JSON and get persona name
   persona_name = player_summary["response"]["players"][0]["personaname"]
   # return the persona name
   return persona_name

def get_avatar(username):
   # get custom player summary using key and provided user ID
   player_summary =  requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={0}&steamids={1}".format( STEAM_API_KEY, username)).json()
   # drill down into player summary JSON and get persona name
   avatar = player_summary["response"]["players"][0]["avatarfull"]
   # return the persona name
   return avatar


def get_friends_list(username):
   # get custom friends list using key and provided user ID
   friends_json =  requests.get("http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={0}&steamid={1}&relationship=friend".format( STEAM_API_KEY, username)).json()
   # drill down into JSON and get friends list
   friends_list = friends_json["friendslist"]["friends"]
   # return the friends list
   return friends_list


def get_game_list(username):
   # get custom games list using key and provided user ID
   games_json =  requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={0}&steamid={1}&include_appinfo=1".format( STEAM_API_KEY, username)).json()
   # drill down into JSON and get games list and count
   game_list = games_json["response"]["games"]
   game_count = games_json["response"]["game_count"]
   # return the games list
   return {'count': game_count ,'games': game_list}