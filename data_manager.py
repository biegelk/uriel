import os
import pandas
import yaml


class DataManager(object):
    def __init__(self, file_dict):
        if "sequences" in file_dict.keys():
            self.stree_data = self.initialize_sequences(file_dict["sequences"])
        if "log" in file_dict.keys():
            self.logfile = file_dict["log"]
            self.initialize_logfile()


    def initialize_sequences(self, sequences_file):
        stree_data = yaml.load(
                         open(sequences_file, "r"),
                         Loader=yaml.FullLoader
                     )

        return stree_data


    def initialize_logfile(self):
        if os.path.exists(self.logfile):
            os.remove(self.logfile)

        with open(self.logfile, "a") as outfile:
            outfile.write("Log file:\n")
