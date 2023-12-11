from math import pow
import os

dirpath = os.path.dirname(os.path.abspath(__file__)) + "\\"
filename = "ex1.txt"
# filename = "ex2.txt"
filename = "input.txt"

def get_file_contents() -> list[str]:
    with open(dirpath + filename, "r") as f:
        return [ x.replace("\n","") for x in f.readlines() ]

def split_card_input(card_line:str) -> dict:
    game, c = card_line.strip().split(":")
    win, lose = c.strip().split("|")
    return {
        game: {
            "win": [ int(x) for x in win.strip().split(" ") ],
            "mine": [ int(x) for x in lose.strip().split(" ") ]
        }
    }

def sol1():
    contents = get_file_contents()
    contents = [ x.replace("  "," ") for x in contents ]
    content_dict = {}
    total = 0
    for line in contents:
        content_dict.update(split_card_input(line))
    for game, vals in content_dict.items():

        i = [ x for x in vals['mine'] if x in vals['win'] ]
        if len(i) > 0:
            total += pow(2, len(i) - 1)
    print(total)

def sol2():
    contents = get_file_contents()

if __name__ == "__main__":
    sol1()
    # sol2()
