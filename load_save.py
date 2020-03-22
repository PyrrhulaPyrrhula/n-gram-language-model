import json

def save_model(path, file):
    with open(path, "w") as write_file:
        json.dump(file, write_file)


def load_model(path):
    with open(path, "r") as read_file:
        return json.load(read_file)
