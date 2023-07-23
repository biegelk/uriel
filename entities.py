import pandas as pd
import game_objects as go

class InteractableEntity(object):
    def __init__(self, name, init_sentiment):
        self.name = name
        self.sentiment = init_sentiment

        self.hist = pd.DataFrame(columns=["num", "sentiment_effect"])

        self.inventory = []


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
