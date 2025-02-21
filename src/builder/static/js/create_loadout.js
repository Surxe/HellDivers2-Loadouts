async function create_loadout() {
    const loadoutName = prompt("Enter loadout name:"); // Ask for a name
    if (!loadoutName) return;

    try {
        const response = await fetch("/create_loadout", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name: loadoutName })
        });

        const data = await response.json();
        if (response.ok) {
            alert(data.message);
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