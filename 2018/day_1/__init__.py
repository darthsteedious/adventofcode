def run():
    with open('./input', 'r') as input:
        result = 0
        while True:
            line = input.readline()
            if line is '':
                break

            value = int(line, 10)
            result += value
        print(f'Result: {result}')


if __name__ == '__main__':
    run()
