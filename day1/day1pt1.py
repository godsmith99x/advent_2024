import csv
import argparse

def total_distance(input_file):

    list1 = []
    list2 = []

    with open(input_file) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=" ")
        for row in csvreader:
            row = list(filter(None, row))
            list1.append(int(row[0]))
            list2.append(int(row[1]))

    list1.sort()
    list2.sort()

    answer = sum(list(map(lambda x, y: abs(x - y), list1, list2)))
    print(answer)
    return(answer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the total distance between two lists of numbers.")
    parser.add_argument("input_file", help="The path to the input file.")
    args = parser.parse_args()
    total_distance(args.input_file)