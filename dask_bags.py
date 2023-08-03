import pickle
import time
import dask
import dask.bag as db


def find_matches(list1, list2):
    bag1 = db.from_sequence(list1)
    bag2 = db.from_sequence(list2)

    common_elements = set(bag1).intersection(bag2)

    matches = []
    for element in common_elements:
        positions_list1 = [i for i, x in enumerate(list1) if x == element]
        positions_list2 = [i for i, x in enumerate(list2) if x == element]
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
