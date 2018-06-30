# v0.0.5

def show_theme_message(dotted_line, width):
    # TODO:

# TODO: show_game_mission()

def reset_health_meter(health_meter):
    """Reset the values of health_meter dict to the original ones"""
    health_meter['player'] = 40
    health_meter['enemy'] = 30

# TODO: occupy_huts()

# TODO: process_user_choice()

def print_bold(msg, end='\n'):
    """Print a string in 'bold' font"""
    print("\033[1m" + msg + "\033[0m", end=end)

def print_dotted_line(width):
    """Print a dotted line (rather 'dashed') line"""
    print('-' * width)

# TODO: reset_health_meter()

def show_health(health_meter):
    # TODO:

def play_game(health_meter):
    huts = occupy_huts()
    idx = process_user_choice()
    reveal_occupants(idx, huts)

    if huts[idx - 1] != 'enemy':
        print_bold("Congratulations! YOU WIN!")
    else:
        print_bold("ENEMY SIGHTED! ", end='')
        show_health(health_meter, bold=True)
        continue_attack = True

        while continue_attack:
            continue_attack = input("......continue attack? (y/n): ")

# TODO: attack()

def reveal_occupants(idx, huts):
    """"Print the occupants of the hut"""
    msg = ""
    print("Revealing occupants...")
    for i in range(len(huts)):
        occupant_info ="<%d:%s>" % (i+1, huts[i])
        if i + 1 == idx:
            occupant_info = "\033[1m" + occupant_info + "\033[0m"
        msg += occupant_info + " "
    print("\t" + msg)
    print_dotted_line()

# TODO: enter_hut

def run_application():
    """Top level control function for running the application"""
    width = 72
    keep_playing = 'y'
    health_meter = {}
    reset_health_meter(health_meter)
    show_game_mission()

    while keep_playing == 'y':
        reset_health_meter(health_meter)
        play_game(health_meter)
        keep_playing = input("\nPlay again? Yes(y)/No(n): ")

if __name__ == '__main__':
    run_application()
