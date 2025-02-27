function tabber_tab_clicked(event, tab_id) {
    // Check if the tab is active
    if (document.getElementById(tab_id).classList.contains("active")) {
        // Hide the tab and return
        document.getElementById(tab_id).classList.remove("active");
        return;
    }
    
    // Hide all tab contents
    document.querySelectorAll(".tab-content").forEach(tab => {
        tab.classList.remove("active");
    });

    // Remove "active" class from all buttons
    document.querySelectorAll(".tab-button").forEach(button => {
        button.classList.remove("active");
    });

    // Show the selected tab and mark the button as active
    document.getElementById(tab_id).classList.add("active");
    event.currentTarget.classList.add("active");
}
