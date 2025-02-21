async function create_loadout() {
    try {
        const response = await fetch("/create_loadout", {
            method: "POST",
            headers: { "Content-Type": "application/json" }
        });

        const data = await response.json();
        if (response.ok) {
            update_loadouts_list(data.loadouts); // Update the UI dynamically
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