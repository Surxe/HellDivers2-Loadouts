async function create_loadout() {
    try {
        // Hide the Create Loadout button
        create_btn = document.getElementById("create_loadout_btn");
        create_btn.style.display = "none";

        const response = await fetch("/create_loadout", {
            method: "POST",
            headers: { "Content-Type": "application/json" }
        });

        const data = await response.json();
        if (response.ok) {
            await rename_loadout(data.loadout_name, true); // Rename the current loadout
        } else {
            alert("Error: " + data.error);
        }

        // Show the Create Loadout button again
        create_btn.style.display = "block";
    } catch (error) {
        console.error("Error:", error);
    } finally {
        // Ensure the Create Loadout button is shown again
        create_btn.style.display = "block";
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