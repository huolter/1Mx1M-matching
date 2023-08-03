import random
import pickle


def generate_random_string(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(characters) for _ in range(length))


def generate_list(size, length):
    return [generate_random_string(length) for _ in range(size)]


def save_list_to_file(data_list, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data_list, file)


if __name__ == "__main__":
    # 6 is the num of chars to be included in each element
    list1 = generate_list(1000000, 6)
    list2 = generate_list(1000000, 6)

    save_list_to_file(list1, "list1.pkl")
    save_list_to_file(list2, "list2.pkl")

    print("Lists saved to list1.pkl and list2.pkl.")
    print("Have a look...")
    print(list1[:10])
    print(list2[:10])
