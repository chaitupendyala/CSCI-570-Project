import os
from .string_generator import input_string_generator

def read_input_file(file_name):
    f = open(file_name,'r')
    slice1 = ''
    slice1_indexes = []
    slice2 = ''
    slice2_indexes = []

    with open(file_name, 'r') as f:
        lines = [ line.strip() for line in f.readlines() ]
        first_string = True
        for line in lines:
            if first_string and slice1 == '' and not line.isnumeric():
                slice1 = line
            elif first_string and line.isnumeric():
                slice1_indexes.append(int(line))
            elif not line.isnumeric() and slice1 != '':
                slice2 = line
                first_string = False
            elif not first_string and line.isnumeric():
                slice2_indexes.append(int(line))
    string1, string2 = input_string_generator( slice1, slice1_indexes, slice2, slice2_indexes )
    return string1, string2