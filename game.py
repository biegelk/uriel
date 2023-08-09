import curses
import yaml
import data_manager
import interface
import sequence_manager
import game_entities


def run_game(settings, dm, gi, sm):
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
            sm.run_sequence("entering_inn_conv")



def main(stdscr):
    # Load the game's settings
    settings = yaml.load(open("./settings.yml", "r"), Loader=yaml.FullLoader)

    # Initialize the game's data manager
    dm = data_manager.DataManager(settings["files"])

    # Initialize the interface object
    gi = interface.Interface(stdscr, settings["display"])

    # Initialize the sequence manager
    sm = sequence_manager.SequenceManager(stdscr, gi.tw, dm.stree_data)

    # Run the game
    run_game(settings, dm, gi, sm)


if __name__ == "__main__":
    curses.wrapper(main)
