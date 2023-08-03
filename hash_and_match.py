import pickle
import time


def find_matches(list1, list2):
    hash_table = {}
    matches = []

    # Build hash table for list1
    for i, elem1 in enumerate(list1):
        if elem1 in hash_table:
            hash_table[elem1].append(i)
        else:
            hash_table[elem1] = [i]

    # Find matches in list2
    for j, elem2 in enumerate(list2):
        if elem2 in hash_table:
            for i in hash_table[elem2]:
                matches.append((elem2, i, j))

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
