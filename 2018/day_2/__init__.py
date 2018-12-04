def run():
    freqs = set()
    with open('./input', 'r') as fp:
        current = 0
        while True:
            line = fp.readline()
            if line == '':
                fp.seek(0)
                continue

            value = int(line, 10)
            current = current + value
            if current in freqs:
                return current
            else:
                freqs.add(current)


if __name__ == '__main__':
    result = run()
    print(result)
