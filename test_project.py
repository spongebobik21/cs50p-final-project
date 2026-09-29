import pytest
from project import filter_commands, format_config_line , validate_command
def test_validate_command():
    """
    Test space stripping and empty string validation.
    """

    assert validate_command("  fps_max 144   ") == "fps_max 144"
    with pytest.raises(ValueError):
        validate_command(" ")

def test_format_config_line():
    """
    Test string conversion to uppercase category tags.
    """
    assert(format_config_line("cs2", "cl_crosshairsize 1") == "[CS2] cl_crosshairsize 1")
    assert format_config_line(" audio ", " volume 0.5 ") == "[AUDIO] volume 0.5"

def test_filter_commands():
    """
    Test case-intensitive substring matching on list items.
    """
    dataset = [
        "[CS2] viewmodel_offset_x 2",
        "[RUST] fps.limit 144",
        "[CS2] sensitivity 1.5",
    ]
    assert filter_commands(dataset, "CS2") == [
    "[CS2] viewmodel_offset_x 2",
    "[CS2] sensitivity 1.5",
    ]
    assert filter_commands(dataset, "fps") == ["[RUST] fps.limit 144"]
    assert len(filter_commands(dataset, "")) == 3
