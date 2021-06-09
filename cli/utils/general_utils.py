import jsonpickle
import os

base_dir = os.path.dirname(os.path.realpath('__file__'))

def to_json(input):
    return jsonpickle.encode(input, unpicklable=False, indent=4)

def save_to_file(file_name, json_to_save):
    full_file_path = os.path.join(base_dir, "data/" + file_name)
    with open(full_file_path, "w") as file:
        file.write(json_to_save)
