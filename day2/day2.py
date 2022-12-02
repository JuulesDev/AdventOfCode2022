move_scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'A': 1,
    'B': 2,
    'C': 3
}

if __name__ == '__main__':
    total_score = 0

    with open('day2-input.txt', 'r') as file:
        for line in file.readlines():
            content = line.strip().split()

            me = move_scores[content[1]]
            elf = move_scores[content[0]]

            current_score = me

            result_match = me - elf
            if result_match == 0: # Draw
                current_score += 3
            elif result_match in [1, -2]: # I win
                current_score += 6
            # Else, i lost

            total_score += current_score

    print(total_score)

