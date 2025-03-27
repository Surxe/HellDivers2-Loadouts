function edit_loadout(loadout) {
    const loadout_id = loadout.id;
    console.log("Edit button clicked for:", loadout);
    // Go to /edit_loadout
    window.location.href = "/edit_loadout?loadout_id=" + loadout_id;
}

document.addEventListener("DOMContentLoaded", function () {
    let selected_equipment = new Set(); // Using a Set to avoid duplicates
    let selected_loadout_type = null;
    let selected_loadout_id = null;

    // When a loadout slot is clicked, store the slot (class) and index (id)
    document.querySelectorAll(".selected-equipment .equipment-slot").forEach(slot => {
        slot.addEventListener("click", function () {
            // Reset brightness of all slots
            document.querySelectorAll(".selected-equipment .equipment-slot").forEach(slot => {
                slot.style.setProperty('--brightness', 1);
            });

            // Select this slot
            selected_loadout_type = this.getAttribute("data-type");
            selected_loadout_id = this.id;

            this.style.setProperty('--brightness', 2); // Change CSS to indicate selection

            console.log("Loadout slot clicked:", selected_loadout_id, selected_loadout_type);
        });
    });

    // When an equipment is clicked, equip it
    document.querySelectorAll(".equipment-options .equipment-slot").forEach(slot => {
        slot.addEventListener("click", function () {
            console.log(selected_equipment);
            let equipment_id = this.id; // Assuming ID is stored in data-tooltip

            if (equipment_id && !selected_equipment.has(equipment_id)) {
                selected_equipment.add(equipment_id);
                
                // Get current slot to add it to
                let target_slot = document.querySelector(`.selected-equipment .equipment-slot[id="${selected_loadout_id}"]`);

                // Edit slot's image's src to slot content
                
                
            }
        });
    });
});