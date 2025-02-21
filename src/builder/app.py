# Import parent path
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(parent_dir)

# Import external libraries
from flask import Flask, render_template

# Import local libraries
from src.Loadout import Loadout

app = Flask(__name__)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Placeholder for loadouts
loadouts = []

@app.route('/')
def home():
    return render_template('index.html', loadouts=loadouts)

@app.route('/create_loadout', methods=['GET', 'POST'])
def create_loadout():
    if request.method == 'POST':
        # Get the loadout name from the form and add to the list
        loadout_name = request.form['loadout_name']
        loadouts.append(loadout_name)
        return redirect(url_for('home'))
    return render_template('create_loadout.html')

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

