# Python code for Day 2 - part two of Advent of Code 2021.
# Ravi Bhikhie
#
# Input file: 'input_02.txt'
# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
# It increases your horizontal position by X units.
# It increases your depth by your aim multiplied by X.
#
# Q: What do you get if you multiply your final horizontal position by your final depth?

input_data = []
with open('input_02.txt', "r", encoding='utf-8') as f:
    for line in f:
        input_data.append(line)

def main():
    aim = 0
    depth = 0
    forward = 0
    
    print(f'{input_data}')

if __name__ == '__main__':
    main()

