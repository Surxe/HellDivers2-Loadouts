# Import parent path
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(parent_dir)

# Import external libraries
import os

class Equipment:
    def __init__(self, id, name, wiki_file_name, file_extension='png', parent_dirs=""):
        self.id = id
        self.name = name
        self.wiki_file_name = wiki_file_name
        self.parent_dirs = parent_dirs
        self.file_extension = file_extension

    def asset_exists(self):
        path = os.path.join("src/assets", self.parent_dirs, f"{self.id}.{self.file_extension}")
        return os.path.exists(path)