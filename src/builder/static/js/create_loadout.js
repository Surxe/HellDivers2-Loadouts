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
            await name_loadout(data.loadout_name, true); // Rename the current loadout
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