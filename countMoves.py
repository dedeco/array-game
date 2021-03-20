def countMoves(numbers):
    first = True
    j = 1
    while True:
        if sum(numbers) == max(numbers) * len(numbers) and first:
            return 0
        m = max(numbers)
        pos = numbers.index(m)
        numbers = list(map(lambda x: x + 1, [y for i, y in enumerate(numbers) if i != pos]))
        numbers.insert(pos, m)
        if sum(numbers) == max(numbers) * len(numbers):
            break
        j += 1

    return j

