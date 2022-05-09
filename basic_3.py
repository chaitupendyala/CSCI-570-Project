from src.inefficient import call_inefficient_sequence_alignment
from src.file_io import read_input_file
import os
import re
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please provide the input and output file names.")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        print ("Input FIle: " + input_file)
        print ("Output FIle: " + output_file)
        string1, string2 = read_input_file(input_file)
        call_inefficient_sequence_alignment(string1, string2, output_file)