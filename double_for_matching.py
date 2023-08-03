import pickle
import time


def find_matches(list1, list2):
    matches = []
    for i, elem1 in enumerate(list1):
        for j, elem2 in enumerate(list2):
            if elem1 == elem2:
                matches.append((elem1, i, j))
    return matches


if __name__ == "__main__":
    # Load the lists from the pickled files
    with open("list1.pkl", "rb") as file:
        list1 = pickle.load(file)

    with open("list2.pkl", "rb") as file:
        list2 = pickle.load(file)

    # Measure the execution time
    start_time = time.time()
    matches_list = find_matches(list1, list2)
    end_time = time.time()

    print(len(matches_list), "matches found.")
    print(matches_list[:10])

    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")
