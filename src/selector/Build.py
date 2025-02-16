class Build():
    def __init__(self, build_path):
        self.build_path = build_path
        self.keybinds = []

    def print_keybinds(self):
        for keybind in self.keybinds:
            print(keybind)

    def read_build_file(self):
        self.keybinds = ["keybind1", "keybind2", "keybind3", "keybind4"]

    #def read_build_file(self):
