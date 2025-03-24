document.addEventListener("DOMContentLoaded", function () {
    let selected_equipment = new Set(); // Using a Set to avoid duplicates

    document.querySelectorAll(".equipment-options .equipment-slot").forEach(slot => {
        slot.addEventListener("click", function () {
            console.log(selected_equipment);
            let equipment_id = this.id; // Assuming ID is stored in data-tooltip

            if (equipment_id && !selected_equipment.has(equipment_id)) {
                // Get current slot to add it to
                let target_slot = document.querySelector(`.selected-equipment .equipment-slot[id="${selected_equipment.size}"]`);

                selected_equipment.add(equipment_id);
                
                if (target_slot) {
                    target_slot.style.border = "2px solid red"; // Change CSS to indicate selection
                }
            }
        });
    });
});