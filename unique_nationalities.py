nationalities = [
    "United States",
    "Brazil",
    "Germany",
    "Spain",
    "The Netherlands",
    "United States",
    "United States",
    "Australia",
    "Japan",
    "Egypt",
    "South-Africa",
    "South-Korea",
    "China",
    "Japan",
    "Mexico",
    "Germany",
    "Sweden",
    "The Netherlands",
    "Canada"
]

def unique_items(lst):

    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    print(unique_lst)


if __name__ == "__main__":
    unique_items(nationalities)