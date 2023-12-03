first_task_test = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

second_task_test = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def second_task():
    search = ["1", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "2", "3", "4", "5", "6", "7",
              "8", "9"]
    numbers = []
    with open('input.txt') as f:
        # lines = second_task_test.splitlines()
        lines = f.readlines()
        for line in lines:
            first_digit_index = float('inf')
            last_digit_index = -1
            first_digit = None
            last_digit = None
            for s in search:
                index_first = line.find(s)
                index_last = line.rfind(s)
                if index_first != -1:
                    first_digit_index = min(first_digit_index, index_first)
                    last_digit_index = max(last_digit_index, index_last)

            first_digit = line[first_digit_index]
            while first_digit not in search:
                first_digit_index += 1
                first_digit += line[first_digit_index]

            if first_digit.isdigit():
                first_digit = int(first_digit)
            else:
                first_digit = search.index(first_digit)

            last_digit = line[last_digit_index]
            while last_digit not in search:
                last_digit_index += 1
                last_digit += line[last_digit_index]
            if last_digit.isdigit():
                last_digit = int(last_digit)
            else:
                last_digit = search.index(last_digit)

            numbers.append(first_digit * 10 + last_digit)

        print(f"second_task: {sum(numbers)}")

def first_task():
    with open('input.txt') as f:
        lines = f.readlines()
        numbers = []
        for line in lines:
            first_digit = 0
            last_digit = 0
            for i in range(0, len(line)):
                if line[i].isdigit():
                    first_digit = int(line[i])
                    break
            for i in range(len(line) - 1, -1, -1):
                if line[i].isdigit():
                    last_digit = int(line[i])
                    break
            numbers.append(first_digit * 10 + last_digit)
        print(f"first_task: {sum(numbers)}")


def main():
    first_task()
    second_task()

if __name__ == '__main__':
    main()
