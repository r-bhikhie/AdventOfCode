# Puzzle 01 for AOC 2021
#
# Q: How many measurements are larger than the previous measurement?
# Input file: "input_01_01.txt"

inputs = []
with open("input_01_01.txt", 'r') as f:
    for line in f:
        line = line.strip()
        inputs.append(int(line))

def main():
    answer = 0

    while len(inputs) > 3:
        set_a = inputs[0:3]
        set_b = inputs[1:4]
        print(set_a)
        print(set_a)

        inputs.pop(0)
        if sum(set_b) > sum(set_a):
            answer +=1
    print(f"Number of increases: {answer}.")

if __name__ == "__main__":
    main()
