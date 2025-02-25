# Import parent path
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(parent_dir)

# Import external libraries
import mwclient
import requests

# Import local libraries
from src.equipment.create_objects import *

weapons = Weapon.load()
stratagems = Stratagem.load()
boosts = Boost.load()
equipment = {**weapons, **stratagems, **boosts}

class AssetGrabber:
    def __init__(self, url):
        self.url = url
        self.site = mwclient.Site(url, path="/")
    
    def get_asset(self, equipment_obj):
        # If it already exists, skip it
        if equipment_obj.asset_exists():
            return False
        
        # Download asset from the URL
        file_name = f"File:{equipment_obj.wiki_file_name}"
        page = self.site.pages[file_name]

        # Get image url
        img_info = page.imageinfo
        if 'url' not in img_info:
            print(f"Failed to find a url for {file_name} or lacking permissions to access it")
            return False
        
        image_url = img_info["url"]
        if image_url is None:
            print(f"Failed to find {file_name} url or lacking permissions to access it")
            return False
        
        response = requests.get(image_url) # download it

        # Save image to file
        if response.status_code == 200:
            # Ensure dir exists
            dir = os.path.join("src/builder/static/assets", equipment_obj.parent_dirs)
            if not os.path.exists(dir):
                os.makedirs(dir)

            with open(os.path.join(dir, f"{equipment_obj.id}.{equipment_obj.file_extension}"), "wb") as file:
                file.write(response.content)
        else:
            print(f"Failed to find {file_name} asset")
            return False

        return True



asset_grabber = AssetGrabber("helldivers.wiki.gg")

for equipment in equipment.values():
    # Download asset
    success = asset_grabber.get_asset(equipment)
