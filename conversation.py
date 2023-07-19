


class Conversation(object):
    def __init__(self, win, starting_node_id):
        self.win = win
        self.nodelist = []
        self.state = starting_node_id





class ConversationNode(object):
    def __init__(self, node_id, msg, destinations):
        self.id = node_id
        self.msg = msg
        self.destinations = destinations
