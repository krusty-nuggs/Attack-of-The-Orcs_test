# v1.0.0

import random
import textwrap

class AttackOfTheOrcs():
    """docstring for AttackOfTheOrcs."""
    def __init__(self):
        self.huts = []
        self.player = None

    def get_occupants(self):

    def show_game_mission(self):

    def _process_user_choice(self):

    def _occupy_huts(self):
        """Randomly occupy the huts with one of: friend, enemy, or 'None'"""
        for i in range(5):
            choice_lst = ['enemy', 'friend', None]
            computer_choice = random.choice(choice_lst)
            if computer_choice == 'enemy':
                name = 'enemy-' + str(i+1)
                self.huts.append(Hut(i+1, OrcRider(name)))
            elif computer_choice == 'friend':
                name = 'knight-' + str(i+1)
                self.huts.append(Hut(i+1, Knight(name)))
            else:
                self.huts.append(Hut(i+1, computer_choice))

    def play(self):
        self.player = Knight()
        self._occupy_huts()
        acquired_hut_counter = 0

        self.show_game_mission()
        self.player.show_health(bold=True)

        while acquired_hut_counter < 5:
            idx = self._process_user_choice()
            self.player.acquire_hut(self.huts[idx-1])

            if self.player.health_meter <= 0:
                print_bold("YOU LOSE :( Better luck next time")
                break

            if self.huts[idx-1].is_acquired:
                acquired_hut_counter +=1

        if acquired_hut_counter == 5:
            print_bold("Congratulations! YOU WIN!!!")

class Knight():
    """docstring for Knight"""
    def __init__(self):
        self.health_meter = []

    def show_health():
        # TODO:

    def acquire_hut():
        # TODO:

class Hut():
    """docstring for Hut."""
    def __init__(self, number, occupant):


    def acquire(self, new_occupant):

    def get_occupant_type(self):

def print_bold(msg, end='\n'):
    """Print a string in 'bold' font"""
    print("\033[1m" + msg + "\033[0m", end=end)

def print_dotted_line(width):
    """Print a dotted line (rather 'dashed') line"""
    print('-' * width)

def show_theme_message(width):
    print_dotted_line(width)
    print_bold("Attack of The Orcs v0.0.5: ")
    msg = (
        "The war between humans and their arch enemies, Orcs, was in the "
        "offing. Sir Foo, one of the brave knights guarding the southern "
        "plains began a long journey towards the east through an unknown "
        "dense forest. On his way, he spotted a small isolated settlement."
        " Tired and hoping to replenish his food stock, he decided to take"
        " a detour. As he approached the village, he saw five huts. There "
        "was no one to be seen around. Hesitantly, he decided to enter..")
    print(textwrap.fill(msg, width=width))

def show_game_mission(width):
    print_bold("Mission:")
    print("\tChoose a hut where Sir Foo can rest...")
    print_bold("TIP:")
    print("Be careful as there are enemies lurking around!")
    print_dotted_line(width)

def reset_health_meter(health_meter):
    """Reset the values of health_meter dict to the original ones"""
    health_meter['player'] = 40
    health_meter['enemy'] = 30

def show_health(health_meter):
        print('Health: Sir Foo: '+ health_meter['player'] + ', Enemy: ' + health_meter['enemy'])

def occupy_huts():
    huts = []
    while len(huts) < 5:
        computer_choice = random.choice(occupants)
        huts.append(computer_choice)

def process_user_choice():
    """Takes user choice and returns an integer value"""
    msg = "\033[1m" + "Choose a hut number to enter (1-5): " + "\033[0m"
    user_choice = input('\n' + msg)
    idx = int(user_choice)
    return idx

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

def attack(health_meter):
    hit_list = 4 * ['player'] + 6 * ['enemy']
    injured_unit = random.choice(hit_list)
    hit_points = health_meter[injured_unit]
    injury = random.randint(10, 15)
    health_meter[injured_unit] = max(hit_points - injury, 0)
    print("ATTACK! ", end='')
    show_health(health_meter)

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
            if continue_attack == 'n':
                print_bold("RUNNING AWAY with following health status...")
                show_health(health_meter, bold=True)
                print_bold("GAME OVER!")
                break

            attack(health_meter)

            if health_meter['enemy'] <= 0:
                print_bold("GOOD JOB! Enemy defeated! YOU WIN!!!")
                break

            if health_meter['player'] <= 0:
                print_bold("YOU LOSE :( Better luck next time")
                break

def run_application():
    """Top level control function for running the application"""
    width = 72
    keep_playing = 'y'
    health_meter = {}
    reset_health_meter(health_meter)
    show_theme_message(width)
    show_game_mission(width)

    while keep_playing == 'y':
        reset_health_meter(health_meter)
        play_game(health_meter)
        keep_playing = input("\nPlay again? Yes(y)/No(n): ")

if __name__ == '__main__':
    game = AttackOfTheOrcs()
    game.play()
