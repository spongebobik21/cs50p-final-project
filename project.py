import sys

def validate_command(command: str) -> str:
    """
    Validate and clean an input command string.

    Trims leading and trailing whitespace. Empty string -> ValueError.

    Args:
        command(str): Raw input command from the user.
    Returns:
        str: Cleaned command string.

    Raises:
        ValueError: if the command contains only whitespace or is empty.
    """

    cleaned = command.strip()
    if not cleaned:
        raise ValueError("Command can't be empty")
    return cleaned
def format_config_line(category: str , command: str) -> str:
    """
    Format category and command strings into a standardized config line.

    Converts category to uppercase and validates the command string.

    Args:
        category (str): Target section or category (e.g., "cs2" ,"rust" ).

        command(str): The configuration command or keybinding.

    Returns:
        str: The configuration line, e.g., "[CS2] sensitivity 1.5".
    """
    #Normalize category text to uppercase
    category_clean = category.strip().upper()
    #Reuse validate_command to ensure the command is non-empty
    command_clean = validate_command(command)

    return f"[{category_clean}] {command_clean}"
def filter_commands(lines: list[str], quary: str) -> list[str]:
    """
    Filter a list of config lines based on a search query.

    Perfoms a case-intensitive search across all formatted lines.

    Args:
        lines (list[str]): List of existing formattted config lines.
        quary(str): Search term to filter by.

    Returns:
        list[str]: Filtered list containing only lines that match the quary.
    """

    quary_lower = quary.strip().lower()
    # empty quary -> return original dataset
    if not quary_lower:
        return lines
    # List comprehension filtering matching lines
    return [line for line in lines if quary_lower in line.lower()]
def main():
    """
    Handle command-line input entry point, user prompt inputs, and output handling.

    """

    print("--- Config & Binding Manager ---")
    category = input("Enter Category (e.g. CS2, RUST, AUDIO): ")
    command = input("Enter command/binding: ")
    #Validate and format input
    try:
        formatted = format_config_line(category, command)
        print(f"Formatted line: {formatted}")
    except ValueError as e:
        #Invalid input -> exit via sys.exit
        sys.exit(f"Error: {e}")

if __name__ == "__main__":
    main()
