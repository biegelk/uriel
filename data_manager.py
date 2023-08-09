import os
import pandas
import yaml
import game_objects
import game_entities


class DataManager(object):
    def __init__(self, file_dict):
        self.file_dict = file_dict

        if "sequences" in self.file_dict.keys():
            self.stree_data = self.initialize_sequences()
        if "log" in self.file_dict.keys():
            self.initialize_logfile()
        if "object_library" in self.file_dict.keys():
            self.initialize_object_library()
        if "entities" in self.file_dict.keys():
            self.initialize_entity_universe()


    def initialize_sequences(self):
        stree_data = yaml.load(
                         open(self.file_dict["sequences"], "r"),
                         Loader=yaml.FullLoader
                     )

        return stree_data


    def initialize_logfile(self):
        self.logfile = self.file_dict["log"]

        if os.path.exists(self.logfile):
            os.remove(self.logfile)

        with open(self.logfile, "a") as outfile:
            outfile.write("Log file:\n")


    def initialize_object_library(self):
        self.o = game_objects.ObjectUniverse(self.file_dict["object_library"])


    def initialize_entity_universe(self):
        self.eu = game_entities.EntityUniverse(self.file_dict["entities"])
