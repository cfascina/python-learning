# zip() makes an iterator that aggregates elements from each of the iterables.
# Returns an iterator of tuples, where the i-th tuple contains the i-th element
# from each of the argument sequences or iterables. The iterator stops when the
# shortest input iterable is exhausted.

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
result = zip(list_1, list_2)
print("Function zip() w/ same lenght lists:")
print(list(result))

list_1 = [1, 2]
list_2 = [3, 4, 5]
result = zip(list_1, list_2)
print("\nFunction zip() w/ different lenght lists:")
print(list(result))

def switch_dict_values(dict_1, dict_2):
    final_dict = {}

    for dict_1_key, dict_2_value in zip(dict_1, dict_2.values()):
        final_dict[dict_1_key] = dict_2_value

    return final_dict

dict_1 = {'a': 1, 'b': 2}
dict_2 = {'c': 3, 'd': 4}

result = zip(dict_1, dict_2)
print("\nFunction zip() w/ dictionaries:")
print(list(result))

result = switch_dict_values(dict_1, dict_2)
print("\nFunction zip() switching keys/values of two dictionaries:")
print(result)
