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

loadouts_list_cache = []

def get_loadouts():
    """Retrieve the list of existing loadouts."""
    for loadout_file_name in os.listdir(loadouts_dir):
        if loadout_file_name.endswith('.json'):
            with open(os.path.join(loadouts_dir, loadout_file_name), 'r') as file:
                loadout_id = loadout_file_name.split('.')[0]
                loadout = json.load(file)
                loadout_name = loadout.get('Loadout_Name', None)
                if loadout_name is None:
                    return jsonify({"error": f"Failed to get loadouts. \"Loadout_Name\" not found in \"{loadout_file_name}\"."})
                
                loadouts_list_cache.append({"id": loadout_id, "name": loadout_name})

            if loadout_name == "":
                return jsonify({"error": f"Failed to get loadouts. Failed to open \"{loadout_file_name}\"."})
            
    return jsonify({"loadouts": loadouts_list_cache})

@app.route('/')
def home():
    return render_template('index.html')


def make_default_loadout_name(i=1):
    # Check if loadout{i} exists
    name = f'loadout{i}'
    if name in any(loadout["name"] for loadout in loadouts_list_cache):
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
            "loadouts": loadouts_list_cache  # Send updated list to frontend
        })
    
    return jsonify({"error": "Failed to create loadout."})

@app.route('/name_loadout', methods=['POST'])
def name_loadout():
    data = request.get_json()
    old_file_name = data['old_file_name']
    new_file_name = data['new_file_name']
    new_name = data['new_name']
    is_brand_new = data['is_brand_new']
    old_path = os.path.join(loadouts_dir, f"{old_file_name}.json")
    new_path = os.path.join(loadouts_dir, f"{new_file_name}.json")

    # Ensure the 'loadouts' directory exists
    if not os.path.exists(loadouts_dir):
        os.makedirs(loadouts_dir)

    new_alr_exists = os.path.exists(new_path)

    # Get the old name of the loadout
    # Load the old loadout
    old_name = ""
    with open(old_path, 'r') as file:
        old_loadout = json.load(file)
        old_name = old_loadout.get('Loadout_Name', None)
        if old_name is None:
            return jsonify({"error": f"Failed to rename loadout. \"Loadout_Name\" not found in \"{old_file_name}.json\"."})
    if old_name == "":
        return jsonify({"error": f"Failed to rename loadout. Failed to open \"{old_file_name}.json\"."})

    loadout_renamed = not (old_name == new_name)
    
    conditions_to_decision = {
       #(is_brand_new, loadout_renamed, new_alr_exists): (should_rename, response_type)
        (True, True, True): (False, "retry"), # if its brand new and the file name was changed and it already exists
        (True, True, False): (True, "create"), # if its brand new and the file name was changed and it does not exist
        (True, False, True): (False, "create"), # if its brand new and the file name was not changed then it already exists
        (True, False, False): (False, "create"), # same as above
        (False, True, True): (False, "retry"), # if its not brand new and the file name was changed and it already exists
        (False, True, False): (True, "rename"), # if its not brand new and the file name was changed and it does not exist
        (False, False, True): (False, "nothing"), # if its not brand new and the file name was not changed then it already exists
        (False, False, False): (False, "nothing") # same as above
    }
    decision = conditions_to_decision[(is_brand_new, loadout_renamed, new_alr_exists)]
    rename, response_type = decision

    if rename:
        os.rename(old_path, new_path)
        old_loadout['Loadout_Name'] = new_name
        new_path_opened = False
        with open(new_path, 'w') as file:
            new_path_opened = True
            json.dump(old_loadout, file, indent=4)
        if not new_path_opened:
            return jsonify({"error": f"Failed to rename loadout. Failed to write \"{new_file_name}.json\"."})

    response_type_to_response = {
       #response_type: response
        "retry": {
            "message": "Loadout \"" + new_name + "\" already exists.",
            "retry": True
        },
        "create": {
            "message": "Loadout \"" + new_name + "\" created.",
            "loadouts": loadouts_list_cache
        },
        "rename": {
            "message": "Loadout \"" + old_name + "\" renamed to \"" + new_name + "\".",
            "loadouts": loadouts_list_cache
        },
        "nothing": {
            "message": "Loadout name unchanged."
        }
    }
    
    response = response_type_to_response[response_type]
    return jsonify(response)

@app.route('/update_loadouts_list_cache', methods=['POST'])
def update_loadouts_list_cache():
    data = request.get_json()
    append_loadouts = data.get('append_loadouts', []) # [list of loadouts to append]
    rename_loadouts = data.get('rename_loadouts', []) # [list of tuples (old_name, new_name) to rename]
    delete_loadouts = data.get('delete_loadouts', []) # [list of loadouts to delete]
    
    for loadout in append_loadouts:
        if loadout in loadouts_list_cache:
            return jsonify({"error": f"Failed to update loadouts list cache. Loadout \"{loadout}\" already exists."})
        loadouts_list_cache.append(loadout)
    for old_name, new_name in rename_loadouts:
        if old_name not in loadouts_list_cache:
            return jsonify({"error": f"Failed to update loadouts list cache. Loadout \"{old_name}\" not found."})
        if new_name in loadouts_list_cache:
            return jsonify({"error": f"Failed to update loadouts list cache. Loadout \"{new_name}\" already exists."})
        loadouts_list_cache.remove(old_name)
        loadouts_list_cache.append(new_name)
    for loadout in delete_loadouts:
        if loadout not in loadouts_list_cache:
            return jsonify({"error": f"Failed to update loadouts list cache. Loadout \"{loadout}\" not found."})
        loadouts_list_cache.remove(loadout)

    return jsonify({"loadouts": loadouts_list_cache})

@app.route('/get_loadouts', methods=['GET'])
def get_loadouts_api():
    """Returns the current list of loadouts."""
    if not loadouts_list_cache: # If the cache is empty, initialize it
        return get_loadouts()
    return jsonify({"loadouts": loadouts_list_cache})

@app.route('/edit_loadout')
def edit_loadout():
    loadout_id = request.args.get('loadout_id')
    if not loadout_id:
        return "Error: No loadout ID specified.", 400

    loadout_path = os.path.join(loadouts_dir, f"{loadout_id}.json")

    # Get the loadout data
    loadout_data = {}
    with open(loadout_path, 'r') as file:
        loadout_data = json.load(file)
    if not loadout_data:
        return "Error: Failed to load loadout data.", 400
    
    return render_template('edit_loadout.html', loadout=loadout_data)

if __name__ == '__main__':
    app.run(debug=True)

