#! /bin/bash

for i in {1..15}
do
    python3 basic_3.py "./inputs/in"$i".txt"  "./outputs/inefficient/output_basic"$i".txt"
done