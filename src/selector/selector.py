import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(parent_dir)

from src.selector.build import Build

# Args are received to sys.argv
build_name = sys.argv[1] if len(sys.argv) > 1 else "build1"

build_path = f"F:/Repositories/HellDivers2-Loadouts/src/builds/{build_name}.json"

build = Build(build_path)

build.print_keybinds()


