function show_prompt(prompt, default_value="") {
    return new Promise((resolve) => {
        const prompt_section = document.getElementById("prompt_section");
        remove_prompt(prompt_section);

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

        // Allow {Enter} to submit
        input.addEventListener("keyup", (event) => {
            if (event.key === "Enter") {
                event.preventDefault();
                resolve(input.value);
            }
        });

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

function remove_prompt(prompt_section) {
    prompt_section.innerHTML = ''; // Clear previous content
}