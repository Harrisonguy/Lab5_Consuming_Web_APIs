import sys



def main():
    get_pokemon_name()
    con_paste_title()
    con_paste_body_text()
    pass

def get_pokemon_name():
    num_params = len(sys.argv) -1
    if num_params == 1:
        pokemon_name = sys.argv[1]
        return pokemon_name
    else:
        print("error")
        sys.exit(1)

def con_paste_title(pokemon_name):
    paste_title = {}




    return paste_title

def con_paste_body_text():







    return






if __name__ == '__main__':
    main()