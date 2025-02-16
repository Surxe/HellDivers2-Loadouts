import json

class Build():
    def __init__(self, build_path):
        self.build_path = build_path
        self.keybinds = []
        self.gear_options = self.read_gear_options()
        self.build_name, self.build_array = self.read_build()
        self.process_keybinds()

    def read_gear_options(self):
        # Read json file with gear options
        with open("src/gear-options/unlocked_options.json", "r", encoding='utf-8') as file:
            gear_options = json.load(file)
        
        return gear_options
    
    def read_build(self):
        # Read json file with build
        with open(self.build_path, "r", encoding='utf-8') as file:
            build_array = json.load(file)
            build_name = build_array["Build_Name"]
            loadout = build_array["Loadout"]
        
        return build_name, loadout
    
    def get_build_name(self):
        return self.build_array["Build_Name"]
    
    def __str__(self):
        # Dict to string with indent
        string = json.dumps(self.build_array, indent=4)
        return string

    def print_keybinds(self):
        for keybind in self.keybinds:
            print(keybind)

    # Add keybind <keybind> <amount> times
    def add_keybind(self, keybind, amount=1):
        if amount >= 1:
            self.keybinds.append(keybind)
            self.add_keybind(keybind, amount-1)

    def process_keybinds(self):
        self.add_keybind("Select") #select strata1

        # Function to find index of value in 2d array
        def find_index(array, value):
            for i, row in enumerate(array):
                for j, element in enumerate(row):
                    if element.lower() == value.lower():
                        return i, j
            raise Exception(f"Stratagem {stratagem_name} not found in gear options, ensure its spelled correctly.")
        
        def add_keybinds(num_down, num_right):
            self.add_keybind("Down", num_down)
            self.add_keybind("Right", num_right)
            self.add_keybind("Select")

        # Iterate stratagems
        for _, stratagem_name in self.build_array["Stratagems"].items():
            print(stratagem_name)
            stratagem_options_array = self.gear_options["Stratagems"]
            add_keybinds(*find_index(stratagem_options_array, stratagem_name))

        # Iterate weapons
        for weapon_type, weapon_name in self.build_array["Weapons"].items():
            weapon_options_array = self.gear_options[weapon_type]
            add_keybinds(*find_index(weapon_options_array, weapon_name))

        # Iterate boosts
        for _, boost_name in self.build_array["Boosts"].items():
            boost_options_array = self.gear_options["Boosts"]
            add_keybinds(*find_index(boost_options_array, boost_name))

        self.add_keybind("Select")

                        
            
        

    #def read_build_file(self):
