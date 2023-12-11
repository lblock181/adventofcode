import os

dirpath = os.path.dirname(os.path.abspath(__file__)) + "\\"
# filename = "ex1.txt"
filename = "ex2.txt"
filename = "input.txt"

def get_file_contents() -> list[str]:
    with open(dirpath + filename, "r") as f:
        return [ x.strip().replace("\n","") for x in f.readlines() ]

def sol1():
    contents = get_file_contents()
    coord_set = set()
    for r_ind, line in enumerate(contents):
        for char_ind, ch in enumerate(line):
            if ch.isdigit() or ch == ".":
                continue
            for curr_row in [r_ind - 1, r_ind, r_ind + 1]:
                for curr_col in [char_ind - 1, char_ind, char_ind + 1]:
                    if curr_row < 0 or curr_row >= len(contents) or curr_col < 0 or curr_col >= len(contents[curr_row]) or not contents[curr_row][curr_col].isdigit():
                        continue
                    while curr_col > 0 and contents[curr_row][curr_col - 1].isdigit():
                        curr_col -= 1
                    coord_set.add((curr_row, curr_col))

    solution = [] 
    for row, col in coord_set:
        temp_str = ""
        while col < len(contents[row]) and contents[row][col].isdigit():
            temp_str += contents[row][col]
            col += 1
        solution.append(int(temp_str))
    print(sum(solution))

def sol2():
    contents = get_file_contents()
    solution = []
    for r_ind, line in enumerate(contents):
        for char_ind, ch in enumerate(line):
            if ch != "*":
                continue
            coord_set = set()
            for curr_row in [r_ind - 1, r_ind, r_ind + 1]:
                for curr_col in [char_ind - 1, char_ind, char_ind + 1]:
                    if curr_row < 0 or curr_row >= len(contents) or curr_col < 0 or curr_col >= len(contents[curr_row]) or not contents[curr_row][curr_col].isdigit():
                        continue
                    while curr_col > 0 and contents[curr_row][curr_col - 1].isdigit():
                        curr_col -= 1
                    coord_set.add((curr_row, curr_col))
            if len(coord_set) != 2:
                continue
            temp_sol = [] 
            for row, col in coord_set:
                temp_str = ""
                while col < len(contents[row]) and contents[row][col].isdigit():
                    temp_str += contents[row][col]
                    col += 1
                temp_sol.append(int(temp_str))
            solution.append(temp_sol[0] * temp_sol[1])
    
    print(sum(solution))

if __name__ == "__main__":
    # sol1()
    sol2()
