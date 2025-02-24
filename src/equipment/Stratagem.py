# Import parent path
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Import local libraries
from equipment.Equipment import Equipment

class Stratagem(Equipment):
    valid_departments = ["Patriotic Administration Center", "Orbital Cannons", "Hangar", "Bridge", "Engineering Bay", "Robotics Workshop", "Warbonds"]

    def __init__(self, id, name, department, wiki_file_name=None, file_extension="png"):
        if wiki_file_name is None:
            wiki_file_name = name

        super().__init__(
            id, 
            name, 
            wiki_file_name=f"{wiki_file_name} Stratagem Icon.{file_extension}", 
            file_extension=file_extension,
            parent_dirs=f"stratagems/{department}".lower().replace(" ", "-")
            )

        if department not in self.valid_departments:
            raise ValueError(f"For stratagem \"{self.id}\", Invalid department {department}, must be one of {self.valid_departments}")
        self.department = department

