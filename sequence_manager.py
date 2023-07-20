class SequenceManager(object):
    def __init__(self, stdscr, win, stree_data):
        self.stdscr = stdscr
        self.win = win
        self.stree_data = stree_data

        self.cnode = None
        self.valid_inputs = {}
        self.status = 0

    def run_sequence(self, stree_name, stree_start=None):
        # Get tree data
        stree = self.stree_data[stree_name]

        # Decide where to start the sequence
        if stree_start is not None:
            # If a specific starting node is given, use it
            self.cnode = stree[stree_start]
        else:
            # If no specific starting node is given, find the node in the
            #   tree labeled with type "start"
            self.cnode = stree["start"]

        while not (self.status == -1):
            self.show_prompt_msg()

            c = ""
            while c not in self.valid_inputs.keys():
                c = self.stdscr.getkey()
                try:
                    c = int(c)
                except:
                    pass

            if c == "k":
                break
            else:
                self.cnode = stree[self.valid_inputs[c]]

        self.win.w.clear()
        self.win.w.refresh()


    def show_prompt_msg(self):
        self.win.w.clear()
        self.win.w.addstr(0, 0, self.cnode["msg"])

        cline = 2

        links = {}

        if "destinations" in self.cnode.keys():
            i = 0
            for node, nmsg in self.cnode["destinations"].items():
                links[i] = node
                fullmsg = f"{i}. {nmsg}"
                self.win.w.addstr(cline, 0, fullmsg)
                i += 1
                cline += 1

        else:
            self.win.w.addstr(cline, 0, "[press k to move on]")
            links["k"] = None
            self.status = -1

        self.valid_inputs = links
        with open("log.out", "a") as outfile:
            outfile.write(str(self.valid_inputs))

        self.win.w.refresh()


