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

        return jsonify({"message": "Loadout created successfully!", "path": file_path})
    
    return jsonify({
        "message": "Loadout created successfully!",
        "path": file_path,
        "loadouts": get_loadouts()  # Send updated list to frontend
    })

    


@app.route('/edit_loadout', methods=['GET', 'POST'])
def edit_loadout():
    if request.method == 'POST':
        # Edit the loadout name from the form
        old_name = request.form['old_name']
        new_name = request.form['new_name']
        if old_name in loadouts:
            loadouts[loadouts.index(old_name)] = new_name
        return redirect(url_for('home'))
    return render_template('edit_loadout.html', loadouts=loadouts)

if __name__ == '__main__':
    app.run(debug=True)

