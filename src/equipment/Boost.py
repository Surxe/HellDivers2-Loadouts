# Import parent path
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Import external libraries
import json

# Import local libraries
from equipment.Equipment import Equipment

class Boost(Equipment):
    path = "src/equipment/data/boosts.json"
    objs = {}

    def __init__(self, id, name, wiki_file_name=None, file_extension="svg"):
        if wiki_file_name is None:
            wiki_file_name = name

        super().__init__(
            id, 
            name, 
            wiki_file_name=f"{wiki_file_name} Booster Icon.{file_extension}", 
            file_extension=file_extension,
            parent_dirs="boosts".lower().replace(" ", "-")
            )
        
        Boost.objs[id] = self

    @classmethod
    def load(cls):
        with open(cls.path, 'r') as f:
            objs = json.load(f)
            for id, obj in objs.items():
                cls(
                    id,
                    obj['name'],
                    obj['wiki_file_name'],
                    obj['file_extension']
                )
        return cls.objs

