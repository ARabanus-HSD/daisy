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



# DEBUGGING

def framed_print(input_str, frame_size, frame_symbol="#"):
    """Put your print in the right frame.
    """
    string_length = len(input_str)
    for _ in range(frame_size):
        print((string_length + 2 + 2 * frame_size) * frame_symbol)
    # print actual content
    print(f"{frame_size * frame_symbol} {input_str} {frame_size * frame_symbol}")
    for _ in range(frame_size):
        print((string_length + 2 + 2 * frame_size) * frame_symbol)
framed_print("yes this look awesome!", 3, ">")