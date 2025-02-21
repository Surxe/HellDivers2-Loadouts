function create_loadout() {
    // Show loading message
    document.getElementById("loading_message").style.display = "block";

    // Send a POST request to the Flask route
    fetch('/create_loadout', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({})  // Send any data if needed (empty body in this case)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        document.getElementById("loading_message").style.display = "none";
        alert(data.message);  // You can alert or update the UI as needed
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("loading_message").style.display = "none";
    });
}