from steam import *
from flask import Flask



app = Flask(__name__)

@app.route('/')
@app.route('/<steam_id>')
def index(steam_id="76561197960435530"):
    return 'Hello {}'.format(get_persona_name(steam_id))



app.run(debug = True, port = 8080, host = '127.0.0.1')



# # prime steam user ID with Robin Walker the ID used in API docs
# steam_username = "76561197960435530"
#
# # while user doesn't use 'exit' continue prompting for user IDs and returning user info
# while (steam_username.lower() != "exit"):
#     # get steam info for current username
#     friends_list = get_friends_list(steam_username)
#     game_list = get_game_list(steam_username)["games"]
#     game_count = get_game_list(steam_username)["count"]
#     # ouptut username
#     print("Username -> ".format(steam_username) + get_persona_name(steam_username))
#     # ouput 10 friends
#     print("Here are some of your friends:")
#     for friends in friends_list[:10]:
#         print("{0} or -> ".format(friends["steamid"]) + get_persona_name(friends["steamid"]))
#     # ouput 10 games
#     print("Here are some of your games:")
#     for game in game_list[:10]:
#         print("{0} -> {1} hours played".format(game["name"], game["playtime_forever"]/60))
#     steam_username = input("What is your steam ID? ")