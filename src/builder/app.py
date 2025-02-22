# Import parent path
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(parent_dir)

# Import external libraries
from flask import Flask, render_template
import json
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..', '.env'))

# Import local libraries
from src.Loadout import Loadout

app = Flask(__name__)
from flask import Flask, render_template, request, redirect, url_for, jsonify

# Define the absolute path to the 'loadouts' directory
repo_path = os.getenv('REPOSITORY_PATH')  # Absolute path to the repository folder
loadouts_dir = os.path.join(repo_path, "src/loadouts")  # Absolute path to the loadouts folder
    

def get_loadouts():
    """Retrieve the list of existing loadouts."""
    return [f[:-5] for f in os.listdir(loadouts_dir) if f.endswith('.json')]

@app.route('/')
def home():
    return render_template('index.html')


def make_default_loadout_name(i=1):
    # Check if loadout{i} exists
    name = f'loadout{i}'
    if name in get_loadouts():
        return make_default_loadout_name(i+1)
    return name

@app.route('/create_loadout', methods=['POST'])
def create_loadout():
    loadout_name = make_default_loadout_name()
    file_path = os.path.join(loadouts_dir, f"{loadout_name}.json")  # Absolute path to blank.json

    # Ensure the 'loadouts' directory exists
    if not os.path.exists(loadouts_dir):
        os.makedirs(loadouts_dir)

    # Define the content of the blank loadout (empty JSON object)
    loadout_data = {
        "Loadout_Name": loadout_name,
        "Loadout": {
            "Weapons": {
                "Primary": "None",
                "Secondary": "None",
                "Throwable": "None"
            },
            "Stratagems": {
                "Stratagem1": "None",
                "Stratagem2": "None",
                "Stratagem3": "None",
                "Stratagem4": "None"
            },
            "Boosts": {
                "Boost1": "None"
            }
        }
    }

    # Create and write the .json file
    with open(file_path, 'w') as file:
        json.dump(loadout_data, file, indent=4)
    
        return jsonify({
            "path": file_path,
            "loadout_name": loadout_name,
            "loadouts": get_loadouts()  # Send updated list to frontend
        })
    
    return jsonify({"error": "Failed to create loadout."})

@app.route('/name_loadout', methods=['POST'])
def name_loadout():
    data = request.get_json()
    old_name = data['old_name']
    new_name = data['new_name']
    is_brand_new = data['is_brand_new']
    old_path = os.path.join(loadouts_dir, f"{old_name}.json")
    new_path = os.path.join(loadouts_dir, f"{new_name}.json")

    # Ensure the 'loadouts' directory exists
    if not os.path.exists(loadouts_dir):
        os.makedirs(loadouts_dir)

    file_renamed = not (old_name == new_name)
    file_exists = os.path.exists(new_path)
    conditions_to_decision = {
       #(is_brand_new, file_renamed, file_exists): (should_rename, response_type)
        (True, True, True): (False, "retry"), # if its brand new and the file name was changed and it already exists
        (True, True, False): (True, "create"), # if its brand new and the file name was changed and it does not exist
        (True, False, True): (False, "create"), # if its brand new and the file name was not changed then it already exists
        (True, False, False): (False, "create"), # same as above
        (False, True, True): (False, "retry"), # if its not brand new and the file name was changed and it already exists
        (False, True, False): (True, "rename"), # if its not brand new and the file name was changed and it does not exist
        (False, False, True): (False, "nothing"), # if its not brand new and the file name was not changed then it already exists
        (False, False, False): (False, "nothing") # same as above
    }
    decision = conditions_to_decision[(is_brand_new, file_renamed, file_exists)]
    rename, response_type = decision

    if rename:
        os.rename(old_path, new_path)

    response_type_to_response = {
       #response_type: response
        "retry": {
            "message": "Loadout \"" + new_name + "\" already exists.",
            "retry": True
        },
        "create": {
            "message": "Loadout \"" + new_name + "\" created.",
            "loadouts": get_loadouts()
        },
        "rename": {
            "message": "Loadout \"" + old_name + "\" renamed to \"" + new_name + "\".",
            "loadouts": get_loadouts()
        },
        "nothing": {
            "message": "Loadout name unchanged."
        }
    }
    
    response = response_type_to_response[response_type]
    return jsonify(response)

@app.route('/delete_loadout', methods=['POST'])

@app.route('/get_loadouts', methods=['GET'])
def get_loadouts_api():
    """Returns the current list of loadouts."""
    return jsonify({"loadouts": get_loadouts()})

if __name__ == '__main__':
    app.run(debug=True)

