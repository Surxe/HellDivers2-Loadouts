async function create_loadout() {
    try {
        const response = await fetch("/create_loadout", {
            method: "POST",
            headers: { "Content-Type": "application/json" }
        });

        const data = await response.json();
        if (response.ok) {
            rename_loadout(data.loadout_name, true); // Rename the current loadout
        } else {
            alert("Error: " + data.error);
        }
    } catch (error) {
        console.error("Error:", error);
    }
}

function update_loadouts_list(loadouts) {
    const loadoutsList = document.getElementById("loadouts-list");
    loadoutsList.innerHTML = "";  // Clear current list

    loadouts.forEach(loadout => {
        const listItem = document.createElement("li");
        listItem.textContent = loadout;
        loadoutsList.appendChild(listItem);
    });
}

// Load existing loadouts when page loads
window.onload = async function () {
    try {
        const response = await fetch("/get_loadouts");
        const data = await response.json();
        update_loadouts_list(data.loadouts);
    } catch (error) {
        console.error("Failed to fetch loadouts:", error);
    }
};