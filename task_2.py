import timeit
import pandas as pd
from BTrees.OOBTree import OOBTree


try:
    df = pd.read_csv("generated_items_data.csv")
except FileNotFoundError:
    print("Файл не знайдено.")
    df = pd.DataFrame()


def add_item_to_tree(tree, ID, name, category, price):
    tree[ID] = {"Name": name, "Category": category, "Price": price}


def add_item_to_dict(dictionary, ID, name, category, price):
    dictionary[ID] = {"Name": name, "Category": category, "Price": price}


def range_query_tree(tree, min_price, max_price):
    return [
        item
        for _, item in tree.items(min_price, max_price)
        if min_price <= item["Price"] <= max_price
    ]


def range_query_dict(dictionary, min_price, max_price):
    return [
        item for item in dictionary.values() if min_price <= item["Price"] <= max_price
    ]


def main():
    tree = OOBTree()
    dictionary = {}
    min_price = 10
    max_price = 500

    # Заповнення даними
    if not df.empty:
        for _, row in df.iterrows():
            add_item_to_tree(
                tree, row["ID"], row["Name"], row["Category"], row["Price"]
            )
            add_item_to_dict(
                dictionary, row["ID"], row["Name"], row["Category"], row["Price"]
            )

    time_tree = timeit.timeit(
        lambda: range_query_tree(tree, min_price, max_price), number=100
    )
    time_dict = timeit.timeit(
        lambda: range_query_dict(dictionary, min_price, max_price), number=100
    )

    print(f"Total range_query time for OOBTree: {time_tree:.6f} seconds")
    print(f"Total range_query time for Dict: {time_dict:.6f} seconds")


if __name__ == "__main__":
    main()
