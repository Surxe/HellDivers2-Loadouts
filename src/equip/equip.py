# Import parent path
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(parent_dir)

# Import external libraries
import json

# Import local libraries
from src.Loadout import Loadout

# Args are received to sys.argv
loadout_name = sys.argv[1] if len(sys.argv) > 1 else "loadout1"
loadout_path = f"src/loadouts/{loadout_name}.json"
loadout = Loadout(loadout_path)

keybind_config_path = f"src/equip/keybind_config.json"
with open(keybind_config_path, "r", encoding='utf-8') as file:
    keybind_config = json.load(file)

loadout.write_cache(keybind_config)