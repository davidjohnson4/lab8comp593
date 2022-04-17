import requests

def get_pokemon_info(name):
    """
    Gets all information about a specified Pokemon retrieved from the PokeAPI
    :param name: Pokemon name
    :returns: Dictionary of Pokemon info, if successful. None, if not.
    """
    print("Getting Pokemon info...", end='')
    url = "https://pokeapi.co/api/v2/pokemon/" + name
    resp_msg = requests.get(url)
    if resp_msg.status_code == 200:
        print('success')
        return resp_msg.json()
    else:
        print('failed. Code:', resp_msg.status_code)
        return

#x = get_pokemon_info("mewtwo")
pass