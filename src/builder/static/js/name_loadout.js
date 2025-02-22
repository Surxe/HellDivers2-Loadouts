async function name_loadout(old_loadout_name, is_brand_new=false) {
    // Request a new name for the loadout
    // Add a new input field to the prompt section, wait for user to click submit

    // If its brand new the current loadout name has no relevancy to be displayed
    const prompt = is_brand_new ? "Enter a name for the new loadout" : "Enter a new name for the loadout";
    const default_value = is_brand_new ? "" : old_loadout_name;
    await show_prompt(prompt, default_value)
    const output_field = document.getElementById("output");
    const new_loadout_name = sanitized_to_file_name(output_field.textContent);
    remove_prompt(document.getElementById("prompt_section"));

    if (!new_loadout_name) {
        return;
    }
    try {
        const response = await fetch("/name_loadout", {
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
                name_loadout(old_loadout_name, is_brand_new); // Retry renaming
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