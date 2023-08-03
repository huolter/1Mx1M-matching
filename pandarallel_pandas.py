import pickle
import time
import pandas as pd
from pandarallel import pandarallel


def find_matches(list1, list2):
    pandarallel.initialize()  # Initialize parallel processing

    df1 = pd.DataFrame(
        {'list1_element': list1, 'list1_position': range(len(list1))})
    df2 = pd.DataFrame(
        {'list2_element': list2, 'list2_position': range(len(list2))})

    # Rename the column in df2 to match the column name in df1 for the merge
    df2.rename(columns={'list2_element': 'list1_element'}, inplace=True)

    common_elements = pd.merge(df1, df2, on='list1_element', how='inner')

    matches_list = common_elements[[
        'list1_element', 'list1_position', 'list2_position']].values.tolist()

    return matches_list


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
