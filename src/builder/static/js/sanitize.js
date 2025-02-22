function sanitize_input(file_name, replacement="_", max_length=50) {
    // Remove unsafe characters (anything not alphanumeric, space, dot, underscore, or hyphen)
    file_name = file_name.replace(/[<>:"/\\|?*\x00-\x1F]/g, replacement);

    // Trim excessive replacements (avoid "__" or "--" sequences)
    file_name = file_name.replace(new RegExp(`${replacement}+`, "g"), replacement).trim().trim(replacement);

    // Ensure filename isn't too long
    return file_name.substring(0, max_length);
}

function sanitized_to_file_name(sanitized_name, replacement="_") {
    // Replace spaces with underscores
    return sanitized_name.replace(/\s+/g, replacement);
}

function sanitize_and_display() {
    const input_field = document.getElementById("input")
    const output_field = document.getElementById("output")

    const sanitized_name = sanitize_input(input_field.value);
    output_field.textContent = sanitized_name;
    output_field.style.display = "block";
}