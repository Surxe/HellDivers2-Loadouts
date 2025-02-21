async function rename_loadout(old_loadout_name, is_brand_new=false) {
    // Request a new name for the loadout
    const new_loadout_name = prompt("Enter a new name for the loadout", old_loadout_name);
    if (!new_loadout_name) {
        return;
    }
    try {
        const response = await fetch("/rename_loadout", {
            method: "POST",
            body: JSON.stringify({ 
                old_name: old_loadout_name, 
                new_name: new_loadout_name,
                is_brand_new: is_brand_new
            }),
            headers: { "Content-Type": "application/json" }
        });

        const data = await response.json();
        if (response.ok) {
            if (data.retry) {
                alert(data.message);
                rename_loadout(old_loadout_name, is_brand_new); // Retry renaming
                return;
            }
            if (data.loadouts) {
                update_loadouts_list(data.loadouts) // Render with the new loadout
            }
            setTimeout(() => {
                alert(data.message);
            }, 0); // Show the alert after the new list is rendered, delay 0ms
            
        } else {
            alert("Error: " + data.error);
        }
    } catch (error) {
        console.error("Error:", error);
    }
}