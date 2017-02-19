import json
import requests
import requests_cache
from sys import platform

requests_cache.install_cache('api_cache')


if platform == "win32":
    APIPATH = r'C:\api_keys.json'
elif platform == "darwin":
    APIPATH = r'/api_keys.json'



cred = json.load(open(APIPATH))
STEAM_API_KEY = cred["STEAM_API_KEY"]
STEAM_USER_URL = "http://api.steampowered.com/ISteamUser/{}/{}/"
STEAM_PLAYER_URL = "http://api.steampowered.com/IPlayerService/{}/{}/"
VERSION = 'v0002'



def make_steam_request(steam_url, endpoint, version, payload):
    """
    Make a GET request to a steam endpoint with the provided version.

    :param endpoint: string endpoint attached to STEAM_USER_URL
    :param version: string 'v0001' or 'v0002'
    :param payload: dictionary of GET params to send to endpoint
    :return: json response from server
    """

    url = steam_url.format(endpoint, version)
    try:
        response = requests.get(url, params=payload).json()
        return response
    except Exception:
        raise ValueError('Data not found')

def get_persona(steam_id):
    """
    Get custom player summary using provided steam ID and return
    the persona name.

    :param steam_id: string steam id
    :return: string persona name
    """

    # get custom player summary using key and provided user ID
    payload = {
       'key': STEAM_API_KEY,
       'steamids': steam_id,
    }
    json_response = make_steam_request(
       steam_url = STEAM_USER_URL,
       endpoint = "GetPlayerSummaries",
       version = VERSION,
       payload = payload,
    )
    # drill down into player summary JSON and get persona name
    try:
        persona_name = json_response["response"]["players"][0]["personaname"]
        # return the persona name
        return persona_name
    except IndexError:
        raise ValueError('Unable to find persona. Invalid Index.')
    except KeyError:
        raise ValueError('Unable to find persona. Invalid Key.')

def get_avatar(steam_id):
    """
    Get custom player summary using provided steam ID and return
    the avatar.

    :param steam_id: string steam id
    :return: string link to avatar
    """
    # get custom player summary using key and provided user ID
    payload = {
       'key': STEAM_API_KEY,
       'steamids': steam_id,
    }
    json_response = make_steam_request(
       steam_url = STEAM_USER_URL,
       endpoint = "GetPlayerSummaries",
       version = VERSION,
       payload = payload,
    )
    try:
        # drill down into player summary JSON and get avatar
        avatar = json_response["response"]["players"][0]["avatarfull"]
        # return the avatar
        return avatar
    except IndexError:
        raise ValueError('Unable to find avatar. Invalid Index.')
    except KeyError:
        raise ValueError('Unable to find avatar. Invalid Key.')


def get_friends(steam_id):
    """
    Get custom friends list using provided steam ID and return
    the friends list.

    :param steam_id: string steam id
    :return: list of dictionaries representing friends
    """
    # get custom friends list using key and provided user ID
    payload = {
       'key': STEAM_API_KEY,
       'steamid': steam_id,
       'relationship': 'friend',
    }
    json_response = make_steam_request(
       steam_url = STEAM_USER_URL,
       endpoint = "GetFriendList",
       version = 'v0001',
       payload = payload,
    )
    try:
        # drill down into JSON and get friends list
        friends_list = json_response["friendslist"]["friends"]
        # return the friends list
        return friends_list
    except IndexError:
        raise ValueError('Unable to find friends. Invalid Index.')
    except KeyError:
        raise ValueError('Unable to find friends. Invalid Key.')


def get_games(steam_id):
    """
    Get custom games list using provided steam ID and return
    the games list and games count.

    :param steam_id: string steam id
    :return: list of dictionaries representing games list and string games count
    """
    # get custom games list using key and provided user ID
    payload = {
        'key': STEAM_API_KEY,
        'steamid': steam_id,
        'include_appinfo': 1,
        'include_played_free_games':1,

    }
    json_response = make_steam_request(
        steam_url = STEAM_PLAYER_URL,
        endpoint = "GetOwnedGames",
        version = 'v0001',
        payload = payload,
    )
    try:
        # drill down into JSON and get games list and count
        game_list = json_response["response"]["games"]
        game_count = json_response["response"]["game_count"]
        # return the games list
        return {'count': game_count ,'games': game_list}
    except IndexError:
        raise ValueError('Unable to find games. Invalid Index.')
    except KeyError:
        raise ValueError('Unable to find games. Invalid Key.')