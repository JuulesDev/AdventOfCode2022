
def store_value(value: int, pos: int, tab: list[int]):
    for i_store in range(pos):
        tab[i_store] = tab[i_store + 1]
    tab[pos] = value


if __name__ == '__main__':
    top_calories = [0, 0, 0]
    current_elf_calories = 0

    with open('./day1-input', 'r') as file:
        for line in file.readlines():
            content = line.strip()

            if content != '':
                current_elf_calories += int(content)
            else:
                # End of elf calories

                # If better than best
                if current_elf_calories > top_calories[-1]:
                    store_value(current_elf_calories, len(top_calories)-1, top_calories)

                # Search for right place
                elif current_elf_calories > top_calories[0]:
                    for i_elf in range(len(top_calories)):
                        if current_elf_calories <= top_calories[i_elf]:
                            store_value(current_elf_calories, i_elf-1, top_calories)
                            break
                current_elf_calories = 0

    print(sum(top_calories))
