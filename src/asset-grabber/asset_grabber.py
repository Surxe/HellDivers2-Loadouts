# Import parent path
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(parent_dir)

# Import external libraries
import mwclient
import requests

class AssetGrabber:
    def __init__(self, url):
        self.url = url
        self.site = mwclient.Site(url, path="/")
    
    def get_asset(self, asset_config):
        # If it already exists, skip it
        if asset_exists(asset_config.asset_name, asset_config.dir):
            return False
        
        # Download png assets from the URL
        file_name = f"File:{asset_config.page_name}.png"
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
            dir = f"src/assets{asset_config.dir}"
            if not os.path.exists(dir):
                os.makedirs(dir)

            with open(f"{dir}/{asset_config.asset_name}.png", "wb") as file:
                file.write(response.content)
        else:
            print(f"Failed to find {file_name} asset")
            return False

        return True

class AssetConfig:
    def __init__(self, page_name, asset_name, dir='/'):
        self.page_name = page_name
        self.asset_name = asset_name
        self.dir = dir

def asset_exists(asset_name, dir="/"):
    return os.path.exists(f"src/assets{dir}/{asset_name}.png")

primary_weapons = ["AR-23 Liberator", "AR-23P Liberator Penetrator", "AR-23C Liberator Concussive", "StA-52 Assault Rifle", "AR-23A Liberator Carbine", "AR-61 Tenderizer", "BR-14 Adjudicator",
                   "R-2124 Constitution", "R-63 Diligence", "R-63CS Diligence Counter Sniper",
                   "PLAS-39 Accelerator Rifle", "MP-98 Knight", "StA-11 SMG", "SMG-32 Reprimand", "SMG-37 Defender", "SMG-72 Pummeler",
                   "SG-8 Punisher", "SG-8S Slugger", "SG-20 Halt", "SG-451 Cookout", "SG-225 Breaker", "SG-225SP Breaker Spray&Pray", "SG-225IE Breaker Incendiary",
                   "CB-9 Exploding Crossbow", "R-36 Eruptor",
                   "SG-8P Punisher Plasma", "ARC-12 Blitzer", "LAS-5 Scythe", "LAS-16 Sickle", "LAS-17 Double-Edge Sickle", "PLAS-1 Scorcher", "PLAS-101 Purifier",
                   "FLAM-66 Torcher", "JAR-5 Dominator"
                   ]

asset_grabber = AssetGrabber("helldivers.wiki.gg")


for primary_weapon in primary_weapons:
    asset_config = AssetConfig(page_name=f"{primary_weapon} Primary Weaponry", asset_name=primary_weapon, dir="/weapons/primary")

    # Download asset
    success = asset_grabber.get_asset(asset_config)
