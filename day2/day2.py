move_scores = {
    'A': 1,
    'B': 2,
    'C': 3
}

if __name__ == '__main__':
    total_score = 0

    with open('day2-input.txt', 'r') as file:
        for line in file.readlines():
            content = line.strip().split()

            elf = move_scores[content[0]]
            result_wanted = content[1]

            if result_wanted == 'Y': # Draw (= same move as the elf)
                total_score += elf + 3 
            elif result_wanted == 'Z': # Win
                me = (elf % 3) + 1
                total_score += me + 6 
            else: # Lose
                me = ((1 + elf) % 3) + 1
                total_score += me

    print(total_score)

