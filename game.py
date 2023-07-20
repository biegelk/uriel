import curses
import yaml
import data_manager as dm
import interface as intf
import sequence_manager as sm


def run_game(settings, gdm, gi, gsm):
    # Set our starting state variable ("return code") to 0
    rc = 0

    # If the state variable ever equals -1, end the program
    while rc != -1:
        # Get the user's input
        c = gi.stdscr.getkey()

        # q: quit
        if c == "q":
            rc = gi.prompt_quit_game()

        if c == "m":
            rc = gi.show_menu()

        if c == "t":
            gsm.run_sequence("entering_inn_conv")



def main(stdscr):
    # Load the game's settings
    settings = yaml.load(open("./settings.yml", "r"), Loader=yaml.FullLoader)

    # Initialize the game's data manager
    gdm = dm.DataManager(settings["files"])

    # Initialize the interface object
    gi = intf.Interface(stdscr, settings["display"])

    # Initialize the sequence manager
    gsm = sm.SequenceManager(stdscr, gi.tw, gdm.stree_data)

    # Run the game
    run_game(settings, gdm, gi, gsm)


if __name__ == "__main__":
    curses.wrapper(main)
