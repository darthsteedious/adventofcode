import re
import time


class GuardLogAction:
    def __init__(self, message):
        tm, msg = self.__parse(message)
        self.tm = tm
        self.message = msg

    @staticmethod
    def __parse(message):
        regex = re.compile(r'^\[(.*)\]\s(.*)')
        matches = regex.match(message)
        t, msg = matches.groups()

        parsed_time = time.strptime(t, '%Y-%m-%d %H:%M')
        return parsed_time, msg

    def __str__(self):
        return f'{{t: {time.strftime("%Y-%m-%d %H:%M", self.tm)}, message: {self.message}}}'

    def __repr__(self):
        return self.__str__()


def part_one():
    with open('./input', 'r') as fp:
        actions = [GuardLogAction(line) for line in fp]
        actions.sort(key=lambda a: a.t)
        print(actions)
