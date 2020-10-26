def parse_ranges(unparsed):
    ranges = unparsed.split(',')
    result = []
    for i in ranges:
        j = i.split('-')
        start = int(j[0])
        try:
            end = int(j[-1])
        except:
            end = start
        while start <= end:
            yield start
            start += 1


print(f"{list(parse_ranges('0-0, 4-8, 20-21, 43-45'))}")

numbers = parse_ranges('100-1000000000000')
print(next(numbers))
print(next(numbers))