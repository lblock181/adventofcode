import os

dirpath = os.getcwd()
# filename = "ex1.txt"
# filename = "ex2.txt"
# filename = "input1.txt"
filename = "input2.txt"


def sol2():
    with open(dirpath + filename, 'r') as f:
        contents:list[str] = f.readlines()

    valid_games: list[int] = []

    for line in [ x.strip().replace("\n","") for x in contents ]:
        game_id, games = line.split(":")
        game_id = int(game_id.split(" ")[1])
        
        min_red = -1
        min_green = -1
        min_blue = -1
        sets:list[str] = games.split(";")
        for s in sets:
            cubes = s.strip().split(",")
            for c in cubes:
                val, color = c.strip().split(" ")
                val = int(val)
                match color:
                    case "red":
                        if min_red == -1 or val > min_red:
                            min_red = val
                    case "green":
                        if min_green == -1 or val > min_green:
                            min_green = val
                    case "blue":
                        if min_blue == -1 or val > min_blue:
                            min_blue = val
        valid_games.append((min_red * min_blue * min_green))
        

    solution = sum(valid_games)

    print(solution)


def sol1():
    max_red = 12
    max_green = 13
    max_blue = 14
    with open(dirpath + filename, 'r') as f:
        contents:list[str] = f.readlines()

    valid_games: list[int] = []

    for line in [ x.strip().replace("\n","") for x in contents ]:
        game_id, games = line.split(":")
        game_id = int(game_id.split(" ")[1])
        
        sets:list[str] = games.split(";")
        game_possible: bool = True
        for s in sets:
            cubes = s.strip().split(",")
            for c in cubes:
                val, color = c.strip().split(" ")
                val = int(val)
                match color:
                    case "red":
                        if val > max_red:
                            game_possible = False
                    case "green":
                        if val > max_green:
                            game_possible = False
                    case "blue":
                        if val > max_blue:
                            game_possible = False
                if not game_possible:
                    break
        if game_possible:
            valid_games.append(game_id)

    solution = sum(valid_games)

    print(solution)

if __name__ == "__main__":
    # sol1()
    sol2()