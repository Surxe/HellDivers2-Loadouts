function tabber_tab_clicked(event, tab_id, tabber_id) {
    // Remove "active" class from all buttons in the same tabber group
    document.querySelectorAll(`.${tabber_id}.tab-button`).forEach(button => {
        button.classList.remove("active");
    });

    const this_tab = document.getElementById(tab_id);

    // Check if the tab is active
    if (this_tab.classList.contains("active")) {
        // Hide the tab and return
        this_tab.classList.remove("active");
        return;
    }

    // Hide all tab contents in the same tabber group
    document.querySelectorAll(`.${tabber_id}.tab-content`).forEach(tab => {
        tab.classList.remove("active");
    });

    // Show the selected tab and mark the button as active
    this_tab.classList.add("active");
    event.currentTarget.classList.add("active");
}
