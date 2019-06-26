from collections import OrderedDict

normal_dict_01 = {}
normal_dict_01['a'] = 'A'
normal_dict_01['b'] = 'B'

print("normal_dict_01:")
for key, value in normal_dict_01.items():
    print(key + ': ' + str(value))

normal_dict_02 = {}
normal_dict_02['b'] = 'B'
normal_dict_02['a'] = 'A'

print("\nnormal_dict_02:")
for key, value in normal_dict_02.items():
    print(key + ': ' + str(value))

print("\nAre 'normal_dict_01' and 'normal_dict_02' equal? " + str(normal_dict_01 == normal_dict_02))
print("In normal dictionaries, it doesn't matter the order the elements were created, as long as they have the same key/value pairs.")

ordered_dict_01 = OrderedDict()
ordered_dict_01['a'] = 'A'
ordered_dict_01['b'] = 'B'

print("\nordered_dict_01:")
for key, value in ordered_dict_01.items():
    print(key + ': ' + str(value))

ordered_dict_02 = OrderedDict()
ordered_dict_02['b'] = 'B'
ordered_dict_02['a'] = 'A'

print("\nordered_dict_02:")
for key, value in ordered_dict_02.items():
    print(key + ': ' + str(value))

print("\nAre 'ordered_dict_01' and 'ordered_dict_02' equal? " + str(ordered_dict_01 == ordered_dict_02))
print("Because in ordered dictionaries, the order the elementes were created matters, even if they have the same key/value pairs.")
