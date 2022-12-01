def part2():
    calories, all_calories = 0, []

    with open("in.txt") as f:
        for line in f:
            # Blank line means we got total calories carried by the elf
            if len(line.strip()) == 0:
                all_calories.append(calories)
                calories = 0
            else:
                calories += int(line.strip())
    ans = sum(sorted(all_calories)[-3:])
    print(ans)


part2()
