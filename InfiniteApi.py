import requests
from PIL import Image
from io import BytesIO


def get_player_last_game_id(pseudo):
    game_stat = requests.get(f"https://sr-nextjs.vercel.app/api/halodotapi?path=%2Fgames%2Fhalo-infinite%2Fstats%2Fmultiplayer%2Fplayers%2F{pseudo}%2Fmatches%3Ftype%3Dmatchmaking%26count%3D1%26offset%3D0")
    result = game_stat.json()["data"][0]["id"]
    return result


def get_last_game_info(game_id):
    game_info = requests.get(f"https://sr-nextjs.vercel.app/api/halodotapi?path=%2Fgames%2Fhalo-infinite%2Fstats%2Fmultiplayer%2Fmatches%2F{game_id}")
    return game_info.json()["data"]


def get_last_game_info_of_pseudo(pseudo):
    game_id = get_player_last_game_id(pseudo)
    return get_last_game_info(game_id)


def get_last_game_medals_list(pseudo):
    game_stat = get_last_game_info_of_pseudo(pseudo)["players"]
    for player in game_stat:
        if player["name"] == pseudo:
            return player["stats"]["core"]["breakdown"]["medals"]


def medal_image_url(medal_id, size=96):
    return f"https://etxvqmdrjezgtwgueiar.supabase.co/storage/v1/render/image/public/assets/games/halo-infinite/metadata/multiplayer/medals/{medal_id}.png?width={size}&height={size}"


def get_medal_image(medal_id, size=96):
    return Image.open(BytesIO(requests.get(medal_image_url(medal_id, size)).content))


print(get_last_game_medals_list("IceCurim"))
