# Import parent path
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(parent_dir)

# Import external libraries
import json

# Import local libraries
from src.selector.build import Build

# Args are received to sys.argv
build_name = sys.argv[1] if len(sys.argv) > 1 else "build1"
build_path = f"src/builds/{build_name}.json"
build = Build(build_path)

keybind_config_path = f"src/selector/keybind_config.json"
with open(keybind_config_path, "r", encoding='utf-8') as file:
    keybind_config = json.load(file)

build.write_cache(keybind_config)