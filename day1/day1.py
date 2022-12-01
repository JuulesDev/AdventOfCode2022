
def store_value(value: int, pos: int, tab: list[int]):
    """Store a value in a tab, shift every other value."""
    for i_store in range(pos):
        tab[i_store] = tab[i_store + 1]
    tab[pos] = value

def manage_elf(elf_calories: int, top_calories: list[int]):
    """Compare elf calories to the top, and add it to the top if needed."""
    if elf_calories > top_calories[-1]: 
        # Edge case if current calories is better than the top
        store_value(elf_calories, len(top_calories)-1, top_calories)
    elif elf_calories > top_calories[0]:
        # If elf fit in the top
        for i_elf in range(len(top_calories)):
            # Looking for the right place to put the current elf
            if elf_calories <= top_calories[i_elf]:
                store_value(elf_calories, i_elf-1, top_calories)
                break


if __name__ == '__main__':
    top_calories = [0 for _ in range(3)]
    current_calories = 0

    with open('./day1-input', 'r') as file:
        for line in file.readlines():
            content = line.strip()

            if content != '': # Add calories to current Elf
                current_calories += int(content)
            else: # End of current Elf
                manage_elf(current_calories, top_calories)
                current_calories = 0

    print(sum(top_calories))

