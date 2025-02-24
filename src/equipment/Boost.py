# Import parent path
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Import local libraries
from equipment.Equipment import Equipment

class Boost(Equipment):
    def __init__(self, id, name, wiki_file_name=None):
        if wiki_file_name is None:
            wiki_file_name = name

        file_extension = "svg"

        super().__init__(
            id, 
            name, 
            wiki_file_name=f"{wiki_file_name} Booster Icon.{file_extension}", 
            file_extension=file_extension,
            parent_dirs="boosts".lower().replace(" ", "-")
            )

