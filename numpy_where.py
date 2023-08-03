import pickle
import time
import numpy as np


def find_matches(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)

    matches = []
    for element in common_elements:
        positions_list1 = np.where(np.array(list1) == element)[0]
        positions_list2 = np.where(np.array(list2) == element)[0]
        matches.extend((element, pos1, pos2)
                       for pos1 in positions_list1 for pos2 in positions_list2)

    return matches


def load_list_from_file(filename):
    with open(filename, "rb") as file:
        data_list = pickle.load(file)
    return data_list


def main():
    list1 = load_list_from_file("list1.pkl")
    list2 = load_list_from_file("list2.pkl")

    start_time = time.time()
    matches_list = find_matches(list1, list2)
    end_time = time.time()

    print(len(matches_list), "matches found.")
    print("First 10 matches:")
    print(matches_list[:10])

    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")


if __name__ == "__main__":
    main()
