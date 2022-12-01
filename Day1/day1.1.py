def part1():
    calories, ans = 0, 0

    with open("in.txt") as f:
        for line in f:
            # Blank line means we got total calories carried by the elf
            if len(line.strip()) == 0:
                ans = max(ans, calories)
                calories = 0
            else:
                calories += int(line.strip())
    print(ans)


part1()
