
def create_character(name, strength, intelligence, charisma):
    """Creates and validates an RPG character with visual stat representation."""

    # Validate name
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"

    # Validate stats
    stats = [strength, intelligence, charisma]
    if not all(isinstance(stat, int) for stat in stats):
        return "All stats should be integers"
    if any(stat < 1 for stat in stats):
        return "All stats should be no less than 1"
    if any(stat > 4 for stat in stats):
        return "All stats should be no more than 4"
    if sum(stats) != 7:
        return "The character should start with 7 points"

    # Create character representation
    def create_stat_line(abbreviation, value):
        full_dots = '●' * value
        empty_dots = '○' * (10 - value)
        return f"{abbreviation} {full_dots}{empty_dots}"

    str_line = create_stat_line("STR", strength)
    int_line = create_stat_line("INT", intelligence)
    cha_line = create_stat_line("CHA", charisma)

    return f"{name}\n{str_line}\n{int_line}\n{cha_line}"
print(create_character("ren", 4, 2, 1))
