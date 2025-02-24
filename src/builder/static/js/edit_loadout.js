function edit_loadout(loadout) {
    const loadout_id = loadout.id;
    console.log("Edit button clicked for:", loadout);
    // Go to /edit_loadout
    window.location.href = "/edit_loadout?loadout_id=" + loadout_id;
}