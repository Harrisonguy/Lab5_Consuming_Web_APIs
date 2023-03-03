from pastbin_api import post_new_paste
from poke_api import get_poke
import sys

def main():
    pokemon = get_search_term()
    pokemon_info = get_poke(pokemon)
    if pokemon_info:
        title, body_text = get_paste_content(pokemon_info, pokemon,)
        paste_url = post_new_paste(title, body_text, expiration='1M', listed=False)
        print(paste_url)
    return

def get_search_term():
    num_params = len(sys.argv) -1
    if num_params >0:
        return sys.argv[1]
    else:
        print('error')
        sys.exit(1)

def get_paste_content(pokemon_info, pokemon):
    title = f"{pokemon.capitalize()}'s Abilities"
    abilities = pokemon_info["abilities"]
    body_text = ""
    for ability in abilities:
        body_text += "- " + ability["ability"]["name"] + "\n"
    return title, body_text

    

if __name__=="__main__":
    main()
