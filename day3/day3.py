letters = [''] + [chr(l) for l in range(ord('a'), ord('z') + 1)] + \
    [chr(l) for l in range(ord('A'), ord('Z') + 1)]


def search_same_item(part1: str, part2: str) -> str:
    for item1 in part1:
        for item2 in part2:
            if item1 == item2:
                return item1
    return ''


if __name__ == '__main__':
    total = 0

    with open('day3-input.txt', 'r') as file:
        for line in file.readlines():
            content = line.strip()
            part1 = content[:len(content)//2]
            part2 = content[len(content)//2:]

            same_item = search_same_item(part1, part2)
            total += letters.index(same_item)

    print("Total:", total)
