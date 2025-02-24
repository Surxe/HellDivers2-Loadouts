# Import parent path
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Import local libraries
from equipment.Equipment import Equipment

# Make weapon class that inherits from Equipment
class Weapon(Equipment):
    valid_slots = ['Primary', 'Secondary', 'Throwable']
    valid_categories = {
        "Primary": ["Assault Rifle", "Marksman Rifle", "Sniper Rifle", "Submachine Gun", "Shotgun", "Explosive", "Energy-Based", "Special"],
        "Secondary": ["Pistol", "Melee", "Special"],
        "Throwable": ["Standard", "Special"]
    }

    def __init__(self, id, name, slot, category, wiki_file_name=None, file_extension='png'):
        if wiki_file_name is None:
            wiki_file_name = name

        super().__init__(
            id, 
            name, 
            wiki_file_name=f"{wiki_file_name} {slot} Weaponry.{file_extension}", 
            file_extension=file_extension, 
            parent_dirs=f"weapons/{slot}/{category}".lower().replace(" ", "-")
            )

        self.file_extension = file_extension

        if slot not in self.valid_slots:
            raise ValueError(f"For weapon \"{self.id}\", Invalid slot \"{slot}\", must be one of {self.valid_slots}")
        self.slot = slot

        if category not in self.valid_categories[slot]:
            raise ValueError(f"For weapon \"{self.id}\", Invalid category \"{category}\" for slot {slot}, must be one of {self.valid_categories[slot]}")
        self.category = category

        