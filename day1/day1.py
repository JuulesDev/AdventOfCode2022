
if __name__ == '__main__':
    most_calories = 0
    current_elf_calories = 0
    with open('./day1-input', 'r') as file:
        for line in file.readlines():
            content = line.strip()

            if content != '':
                current_elf_calories += int(content)
            else:
                if current_elf_calories > most_calories:
                    most_calories = current_elf_calories
                current_elf_calories = 0

    print(most_calories)
