def input_string_generator(slice1, slice1_indexes, slice2, slice2_indexes):
    string1 = slice1
    string2 = slice2

    for indices in slice1_indexes:
        string1 = string1[:indices + 1] + string1 + string1[indices + 1:]
    
    for indices in slice2_indexes:
        string2 = string2[:indices + 1] + string2 + string2[indices + 1:]
    
    return string1, string2