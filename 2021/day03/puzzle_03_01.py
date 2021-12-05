# Python code for Day 1 - part one of Advent of Code 2021.
# Ravi Bhikhie
#
# Input file: 'input_03.txt' Lines are 12 bits wide.
#
# Q: Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together.
# What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)

def main():
    
    answer = 0
    gamma = 0
    epsilon = 0
    
    with open('input_02.txt', "r", encoding='utf-8') as f:
        for line in f:
            pass

    print(f'Episilon: {epsilon}, Gamma: {gamma}.')
    print(f'Final answer: {answer}')

if __name__ == '__main__':
    main()
