# A1.1

list_1 = [50, 40, 30, 100]
list_2 = [10, 20, 1, 51]

joinded_list = list_1 + list_2
joinded_list.sort()

print(joinded_list)

# A1.2

def list_combiner(list_a: list, list_b: list) -> list:
    """combines two lists, outputs combined lists, accending order

    Args:
        list_a (list): first list
        list_b (list): second list

    Returns:
        list: combined sorted list
    """
    combined_list = list_1 + list_2
    combined_list.sort()
    return combined_list

print(list_combiner(list_1, list_2))