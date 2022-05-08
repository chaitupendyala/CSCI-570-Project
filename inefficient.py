from src.inefficient import call_inefficient_sequence_alignment
from src.file_io import read_input_file
import os
import re

if __name__ == "__main__":
    for x in os.listdir("./inputs/"):
        if x.endswith(".txt"):
            print( "Reading File: " + x )
            textcase_number = re.findall(r'\d+',x)
            string1, string2 = read_input_file("./inputs/"+x)
            call_inefficient_sequence_alignment(string1, string2, textcase_number[0])