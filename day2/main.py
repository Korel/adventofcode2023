test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def first_task():
    wanted_red = 12
    wanted_green = 13
    wanted_blue = 14
    lines = test_input.splitlines()
    games = []
    for line in lines:
        line = line[line.find(':') + 1:]
        game_sets = line.split(';')
        for game_set in game_sets:
            game_set = game_set[1:]
            number = ""
            index = 0
            while index < len(game_set) and game_set[index].isdigit():
                number += game_set[index]
                index += 1


def main():
    first_task()


if __name__ == '__main__':
    main()
