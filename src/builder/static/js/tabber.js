function tabber_tab_clicked(event, tab_id) {
    // Remove "active" class from all buttons
    document.querySelectorAll(".tab-button").forEach(button => {
        button.classList.remove("active");
    });

    // Check if the tab is active
    tab = document.getElementById(tab_id);
    if (tab.classList.contains("active")) {
        // Hide the tab and button and return
        tab.classList.remove("active");
        return;
    }

    // Hide all tab contents
    document.querySelectorAll(".tab-content").forEach(tab => {
        tab.classList.remove("active");
    });

    // Show the selected tab and mark the button as active
    tab.classList.add("active");
    event.currentTarget.classList.add("active");
}
