import pandas as pd
import game_objects as go

class EntityUniverse(object):
    def __init__(self, library):
        self.library = {}
        self.manifest = {}

        if type(library) == str:
            library_data = yaml.load(open(library, "r"), Loader=yaml.FullLoader)
        elif type(library) == dict:
            library_data = library

        for key in library_data.keys():
            self.library[key] = InteractableEntity(library_data[key])



class InteractableEntity(object):
    def __init__(self, input_data):
        self.name = input_data["name"]
        self.sentiment = input_data["init_sentiment"]

        if "inventory" in input_data.keys():
            self.inventory = input_data["inventory"]
        else:
            self.inventory = []

        self.hist = pd.DataFrame(columns=["num", "sentiment_effect"])


    def log_interaction(self, sentiment_effect):
        self.hist.loc[len(self.hist)] = {
            "num": len(self.hist),
            "sentiment_effect": sentiment_effect
        }



    def compliment(self):
        self.sentiment += 1

        self.log_interaction(1)

        msg = "wow, thanks!"

        print(msg)


    def insult(self):
        self.sentiment -= 1

        self.log_interaction(-1)

        msg = "hey, fuck you"

        print(msg)


    def give(self, thing):
        self.log_interaction(0)

        if type(thing) == go.GameObject and thing.exists:
            self.inventory.append(thing)
            msg = "hmm, interesting"
        else:
            msg = "sorry, I'm not licensed to handle non-corporeal objects."

        print(msg)
