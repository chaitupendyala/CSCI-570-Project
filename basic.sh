#! /bin/bash

for i in {1..15}
do
    python3 basic_3.py "in"$i".txt"  "output_basic"$i".txt"
done