import csv
import argparse

def similarity_score(input_file):
    list1 = []
    list2 = []
    result = []

    with open(input_file) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=" ")
        for row in csvreader:
            row = list(filter(None, row))
            list1.append(int(row[0]))
            list2.append(int(row[1]))

    for num in list1:
        result.append(num * list2.count(num))

    answer = sum(result)
    print(answer)
    return(answer)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the similarity score between two lists of numbers.")
    parser.add_argument("input_file", help="The path to the input file.")
    args = parser.parse_args()
    similarity_score(args.input_file)