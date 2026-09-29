# Config & Binding Manager

#### Video Demo: <https://youtu.be/RfjpJfTqV1k>

#### Description

The **Config & Binding Manager** is a Command-Line Interface utility written in Python. It is designed to assist gamers and system administrators in structuring, validating and filtering complex configuration files and custom keybindings (e.g., for games like CS2 or Rust or system settings).

Managing large configuration files manually often leads to formatting inconsistencies, invalid entries, or duplicate parameters. This project solves that problem by providing a standardized pipeline to process user inputs, convert categories to uniform upper-case tags, validate non-empty commands, and search through datasets with case-intensitive filtering.

---

### Project Structure & File Contents

The project is organized into the following essential files:

* **`project.py`** : the core application module containing `main()` and three primary testable functions:
    * `validate_command(command: str) -> str`: Accepts a raw command string, strips leading/trailing whitespaces , and ensures the entry is non-empty. If an empty string or whitespace-only input is provided, it raises a `ValueError`.
    * `format_config_line(category:str , command: str) -> str`: Normalizes the category string by converting it to uppercase and invokes `validate_command` to costruct a clean, bracketed line format(e.g., `[CS2] sensitivity 1.5`).
    * `filter_commands(lines: list[str], quary: str) -> list[str]`: Implements list filtering by perfoming a case-instensitive search across existing configuration entries, returing a new filtered list matching the query term.
    * `main()` Controls the interactive command-line interface, handles user prompts via `input()`, executes formatting logic , and handles runtime errors gracefully.

* **`test_project.py`**: The automated unit testing suite executed via `pytest`. It uncludes three distincs test functions(`test_validate_command`, `test_format_config_line`, and `test_filter_commands`) that verify boundary conditions, error handling (`pytest.raises(ValueError)`), and edge cases without invoking user input dialogs.
* **`requirements.txt`**: Lists all third-party Python packages requeired to execute and test the application (`pytest`).
* **`README.md`**: Provides full project documantation, architectrual overview, and the Youtube demo link.

---

### Design Desicions

During the development process, the primary architectural desicion was to separate **user interface interactions**(`input` and `print` inside `main()`) from the **core business logic**(`validate_command`, `format_config_line`, and `filter_commands`).

The whole project is 100% testable via unit tests in `test_project.py` in strict accordance with CS50P grading guidelines.

