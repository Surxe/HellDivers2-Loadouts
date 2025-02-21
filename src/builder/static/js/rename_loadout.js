async function rename_loadout(old_loadout_name) {
    // Request a new name for the loadout
    const new_loadout_name = prompt("Enter a new name for the loadout", old_loadout_name);
    if (!new_loadout_name) {
        return;
    }
    try {
        const response = await fetch("/rename_loadout", {
            method: "POST",
            body: JSON.stringify({ old_name: old_loadout_name, new_name: new_loadout_name }),
            headers: { "Content-Type": "application/json" }
        });

        const data = await response.json();
        if (response.ok) {
            update_loadouts_list(data.loadouts) // Rename the current loadout
            setTimeout(() => {
                alert("Renamed Loadout \"" + data.old_name + "\" to " + data.new_name);
            }, 0); // Show the alert after the new list is rendered, delay 0ms
            
        } else {
            alert("Error: " + data.error);
        }
    } catch (error) {
        console.error("Error:", error);
    }
}