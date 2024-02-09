class MapLoader(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def load_map(self):
        file = open(self.file_path)
        file_map = file.readlines()
        file.close()
        return file_map
