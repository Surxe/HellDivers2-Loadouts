function show_prompt(prompt, default_value="") {
    return new Promise((resolve) => {
        const prompt_section = document.getElementById("prompt_section");
        prompt_section.innerHTML = ''; // Clear previous content

        // Create label
        const label = document.createElement("label");
        label.textContent = prompt;
        label.setAttribute("for", "user_input");

        // Create input field
        const input = document.createElement("input");
        input.type = "text";
        input.id = "user_input";
        input.name = "user_input";
        input.textContent = default_value

        // Create submit button
        const button = document.createElement("button");
        button.textContent = "Submit";

        // Handle submission
        button.addEventListener("click", () => {
            resolve(input.value);
            prompt_section.innerHTML = ''; // Clear after submission
        });

        // Append elements
        prompt_section.appendChild(label);
        prompt_section.appendChild(document.createElement("br"));
        prompt_section.appendChild(input);
        prompt_section.appendChild(document.createElement("br"));
        prompt_section.appendChild(button);

        // Autofocus on input field
        input.focus();
    });
}

function sanitize_input(file_name, replacement="_", max_length=50) {
    // Remove unsafe characters (anything not alphanumeric, space, dot, underscore, or hyphen)
    file_name = file_name.replace(/[<>:"/\\|?*\x00-\x1F]/g, replacement);

    // Replace multiple spaces or special characters with a single replacement
    file_name = file_name.replace(/\W+/g, replacement); // Remove non-word characters

    // Trim excessive replacements (avoid "__" or "--" sequences)
    file_name = file_name.replace(new RegExp(`${replacement}+`, "g"), replacement).trim(replacement);

    // Ensure filename isn't too long
    return file_name.substring(0, max_length);
}

function sanitized_to_file_name(sanitized_name, replacement="_") {
    // Replace spaces with underscores
    return sanitized_name.replace(/\s+/g, replacement);
}

async function get_user_input(prompt, default_value="") {
    const user_input = await show_prompt(prompt, default_value);

    
        

    console.log("User input:", user_input);
    return user_input;
}