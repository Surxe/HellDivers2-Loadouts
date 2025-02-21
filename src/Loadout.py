import json
import os

class Loadout():
    def __init__(self, loadout_path):
        self.loadout_path = loadout_path
        self.keybinds = []
        self.gear_options = self.read_gear_options()
        loadout_name, self.loadout_array = self.read_loadout()
        self.loadout_name = self.clean_loadout_name(loadout_name)
        self.process_keybinds()
        self.cache_dir = "src/equip/cache"
        self.cache_path = f"{self.cache_dir}/{self.loadout_name}.txt"

    def clean_loadout_name(self, loadout_name):
        # Remove special characters from loadout name
        loadout_name = loadout_name.replace(" ", "_")
        loadout_name = ''.join(e for e in loadout_name if e.isalnum() or e == "_")
        return loadout_name

    def read_gear_options(self):
        # Read json file with gear options
        with open("src/gear-options/unlocked_options.json", "r", encoding='utf-8') as file:
            gear_options = json.load(file)
        
        return gear_options
    
    def read_loadout(self):
        # Read json file with loadout
        with open(self.loadout_path, "r", encoding='utf-8') as file:
            loadout_array = json.load(file)
            loadout_name = loadout_array["Loadout_Name"]
            loadout = loadout_array["Loadout"]
        
        return loadout_name, loadout
    
    def __str__(self):
        # Dict to string with indent
        string = json.dumps(self.loadout_array, indent=4)
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
        for _, stratagem_name in self.loadout_array["Stratagems"].items():
            print(stratagem_name)
            stratagem_options_array = self.gear_options["Stratagems"]
            add_keybinds(*find_index(stratagem_options_array, stratagem_name))

        # Iterate weapons
        for weapon_type, weapon_name in self.loadout_array["Weapons"].items():
            weapon_options_array = self.gear_options[weapon_type]
            add_keybinds(*find_index(weapon_options_array, weapon_name))

        # Iterate boosts
        for _, boost_name in self.loadout_array["Boosts"].items():
            boost_options_array = self.gear_options["Boosts"]
            add_keybinds(*find_index(boost_options_array, boost_name))

        self.add_keybind("Select")

    def write_cache(self, keybind_config):
        os.makedirs(self.cache_dir, exist_ok=True)
        mapped_keybinds = [keybind_config[keybind] for keybind in self.keybinds]
        mapped_keybinds_str = " ".join(mapped_keybinds)
        with open(self.cache_path, "w", encoding='utf-8') as file:
            file.write(mapped_keybinds_str)