import curses

w_width = 80
mw_height = 30
tw_height = 10
sw_height = 1


class Interface(object):

    def __init__(self, stdscr):
        self.stdscr = stdscr

        self.show_splash()

        self.create_windows()

        self.mw.refmsg("this is the map window", where="center")
        self.tw.refmsg("this is the text window", where="top_center")
        self.sw.refmsg("this is the status window", where="center")


    def hold(self):
        try:
            # Preserve the status window's original contents
            prev_msg = self.sw.w.instr(0, 0, w_width-2)

            # Wait for the user to prompt execution to continue
            self.sw.refmsg("HOLD: press k to move on")
            c = None
            while c != "k":
                c = self.stdscr.getkey()

            # Restore the status window's original contents
            self.sw.refmsg(prev_msg)

        except AttributeError:
            c = None
            while c != "k":
                c = self.stdscr.getkey()
        except Exception as err:
            raise EOFError


    def show_splash(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "interface initialized")
        self.stdscr.addstr(1, 0, "press k to move on")
        self.stdscr.refresh()

        self.hold()


    def create_windows(self):
        cline = 0

        self.d0 = cursesWindow(1, w_width, cline, 0)
        self.d0.refmsg("-"*(w_width - 1))
        cline += 1

        self.mw = cursesWindow(mw_height, w_width, cline, 0)
        cline += mw_height

        self.d1 = cursesWindow(1, w_width, cline, 0)
        self.d1.refmsg("-"*(w_width - 1))
        cline += 1

        self.tw = cursesWindow(tw_height, w_width, cline, 0)
        cline += tw_height

        self.d2 = cursesWindow(1, w_width, cline, 0)
        self.d2.refmsg("-"*(w_width - 1))
        cline += 1

        self.sw = cursesWindow(sw_height, w_width, cline, 0)
        cline += sw_height

        self.d3 = cursesWindow(1, w_width, cline, 0)
        self.d3.refmsg("-"*(w_width - 1))


    def show_menu(self):
        self.mw.refmsg("This is the menu.", where="center")

        self.hold()


    def prompt_quit_game(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "Would you really like to quit? (press 'q' again)")
        self.stdscr.refresh()

        rc = 0

        c = self.stdscr.getkey()
        if c == "q":
            rc = -1

        return -1


class cursesWindow(object):

    def __init__(self, height, width, y_start, x_start):
        self.height = height
        self.width = width
        self.y_start = y_start
        self.x_start = x_start

        self.w = curses.newwin(height, width, y_start, x_start)


    def refmsg(self, msg, where="upper_left"):
        y_start = 0
        x_start = 0

        if where == "center":
            y_start = int(self.height / 2)

            if len(msg) < self.width:
                x_start = int((self.width - len(msg)) / 2)
        elif where == "top_center":
            y_start = 0
            if len(msg) < self.width:
                x_start = int((self.width - len(msg)) / 2)

        self.w.clear()
        self.w.addstr(y_start, x_start, msg)
        self.w.refresh()

