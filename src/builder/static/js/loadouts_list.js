function update_loadouts_list(loadouts) {
    const loadoutsList = document.getElementById("loadouts-list");
    loadoutsList.innerHTML = "";  // Clear current list

    // each element in the array is a loadout that looks like { "id": "loadout1", "name": "Loadout 1" }
    // iterate loadouts
    loadouts.forEach(loadout => {
        const loadout_id = loadout.id;
        const loadout_name = loadout.name;
        const list_item = document.createElement("li");
        list_item.textContent = loadout_name;

        // Add a button to the right of the list item
        const edit_button = document.createElement("button");
        edit_button.textContent = "Edit";
        edit_button.onclick = function () {
            console.log("Edit button clicked for:", loadout);
            edit_loadout(loadout);
        };
        list_item.appendChild(edit_button);

        loadoutsList.appendChild(list_item);
    });
}

// Load existing loadouts when page loads
window.onload = async function () {
    try {
        const response = await fetch("/get_loadouts");
        const data = await response.json();
        update_loadouts_list(data.loadouts);
        console.log("Loaded loadouts:", data.loadouts);
    } catch (error) {
        console.error("Failed to fetch loadouts:", error);
    }
};