function show_prompt(prompt, default_value="") {
    return new Promise((resolve) => {
        const prompt_section = document.getElementById("prompt_section");
        prompt_section.innerHTML = ''; // Clear previous content

        // Create label
        const label = document.createElement("label");
        label.textContent = prompt;
        label.setAttribute("for", "input");

        // Create input field
        const input = document.createElement("input");
        input.type = "text";
        input.id = "input";
        input.name = "input";
        input.oninput = sanitize_and_display;
        input.textContent = default_value

        // Create output field
        const output = document.createElement("p");
        output.textContent = "Sanitized filename: ";
        const output_span = document.createElement("span");
        output_span.id = "output";
        output.appendChild(output_span);

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
        prompt_section.appendChild(output);
        prompt_section.appendChild(document.createElement("br"));
        prompt_section.appendChild(button);

        // Autofocus on input field
        input.focus();
    });
}

async function get_user_input(prompt, default_value="") {
    const user_input = await show_prompt(prompt, default_value);

    
        

    console.log("User input:", user_input);
    return user_input;
}