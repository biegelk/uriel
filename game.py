import curses
import interface



def run_game(gi):
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



def main(stdscr):
    # Initialize the interface object
    gi = interface.Interface(stdscr)

    run_game(gi)


if __name__ == "__main__":
    curses.wrapper(main)
