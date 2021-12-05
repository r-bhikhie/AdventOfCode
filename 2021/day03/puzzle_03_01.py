# Python code for Day 1 - part one of Advent of Code 2021.
# Ravi Bhikhie
#
# Input file: 'input_03.txt' Lines are 12 bits wide.
#
# Q: Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together.
# What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)

# Observations: inputs are 12 digits wide. Max value eps/gam is 2^12 or 4096.

def main():
    
    gamma = ""
    epsilon = ""
    zero_counting_box = [0,0,0,0,0,0,0,0,0,0,0,0]
    one_counting_box = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    with open('input_03.txt', "r", encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            
            for idx, input_bit in enumerate(line):
                if input_bit == "0":
                    zero_counting_box[idx] += 1
                if input_bit == "1":
                    one_counting_box[idx] += 1
    
    for idx,bit in enumerate(zero_counting_box):
        if zero_counting_box[idx] > one_counting_box[idx]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    
    answer = int(gamma,2)*int(epsilon,2)

    print(f'Epsilon: {epsilon}, Gamma: {gamma}.')
    print(f'Final answer: {answer}')

if __name__ == '__main__':
    main()
