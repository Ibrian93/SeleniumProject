import json
import pathlib


class EnvironmentLoader(object):

    def __init__(self, file):
        path_to_file = str(pathlib.Path(__file__).parent.absolute())
        json_to_open = path_to_file + '/' + file + '.json'
        print(json_to_open)
        f = open(path_to_file + '/' + file +'.json')
        self.json_file = f.read()

    def loader(self):
        return json.loads(self.json_file)
