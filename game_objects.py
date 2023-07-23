import yaml

class ObjectUniverse(object):
    def __init__(self, library):
        self.library = {}
        self.manifest = {}

        if type(library) == str:
            library_data = yaml.load(open(library, "r"), Loader=yaml.FullLoader)
        elif type(library) == dict:
            library_data = library

        for key in library_data.keys():
            self.library[key] = GameObject(library_data[key])



class GameObject(object):
    def __init__(self, input_dict):
        self.name = input_dict["name"]
        self.short_desc = input_dict["short_desc"]
        self.long_desc = input_dict["long_desc"]
        self.weight = input_dict["weight"]

        self.exists = True


    def describe(self, mode="short"):
        if not self.exists:
            msg = f"The {self.name} doesn't exist."
        elif mode == "long":
            msg = self.long_desc
        else:
            msg = self.short_desc

        print(msg)

    def destroy(self):
        self.exists = False

        print(f"You have destroyed the {self.name}.")
