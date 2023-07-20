import pandas
import yaml


class DataManager(object):
    def __init__(self, file_dict):
        if "map" in file_dict.keys():
            map_array = initialize_map(file_dict["map"])
        if "sequences" in file_dict.keys():
            self.stree_data = self.initialize_sequences(file_dict["sequences"])



    def initialize_map(self, map_file):
        map_array = None

        return map_array


    def initialize_sequences(self, sequences_file):
        stree_data = yaml.load(
                         open(sequences_file, "r"),
                         Loader=yaml.FullLoader
                     )

        return stree_data
