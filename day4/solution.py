import os

dirpath = os.path.dirname(os.path.abspath(__file__)) + "\\"
filename = "ex1.txt"
# filename = "ex2.txt"
# filename = "input.txt"

def get_file_contents() -> list[str]:
    with open(dirpath + filename, "r") as f:
        return [ x.replace("\n","") for x in f.readlines() ]

def sol1():
    contents = get_file_contents()

def sol2():
    contents = get_file_contents()

if __name__ == "__main__":
    sol1()
    sol2()
