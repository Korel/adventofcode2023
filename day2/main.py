test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def parse_game(line: str):
    line = line[line.find(':') + 1:]
    line = line.replace(" ", "")
    line = line.replace("\n", "")
    game = line.split(';')
    games_parsed = []
    for game_set in game:
        game_parsed = []
        revealed = game_set.split(',')
        for r in revealed:
            number = ""
            index = 0
            while index < len(r) and r[index].isdigit():
                number += r[index]
                index += 1
            cube = r[index:]
            game_parsed.append((int(number), cube))
        games_parsed.append(game_parsed)
    return games_parsed
    

def first_task():
    wanted_red = 12
    wanted_green = 13
    wanted_blue = 14
    f = open("input.txt", "r")
    # lines = test_input.splitlines()
    lines = f.readlines()
    games = []
    for line in lines:
        games.append(parse_game(line))

    possible = []

    for game in games:
        possible.append(True)
        for gsets in game:
            if possible[-1] == False:
                break
            for gset in gsets:
                amount = gset[0]
                cube = gset[1]
                if amount <= wanted_red:
                    continue
                if cube == "red":
                    possible[-1] = False
                    break
                if amount <= wanted_green:
                    continue
                if cube == "green":
                    possible[-1] = False
                    break
                if amount <= wanted_blue:
                    continue
                if cube == "blue":
                    possible[-1] = False
                    break  
    total = 0
    for i in range(len(possible)):
        if possible[i]:
            total += i + 1
    print("first_task: ", total)
    # assert(total == 8) # if test input
    

def second_task():
    # lines = test_input.splitlines()
    with open("input.txt", "r") as f:
        lines = f.readlines()
    games = []
    for line in lines:
        games.append(parse_game(line))
    
    powers = []
    for game in games:
        reds = 0
        greens = 0
        blues = 0
        for gsets in game:
            for gset in gsets:
                if gset[1] == "red":
                    reds = max(reds, gset[0])
                elif gset[1] == "green":
                    greens = max(greens, gset[0])
                else:
                    blues = max(blues, gset[0])
        powers.append(reds * greens * blues)
    print("second_task: ", sum(powers))
    # assert(sum(powers) == 2286) # if test input
    

def main():
    # first_task()
    second_task()


if __name__ == '__main__':
    main()
