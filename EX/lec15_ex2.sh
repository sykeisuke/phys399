#!/bin/bash
for file in *.txt
do
  wc -l "$file" >> summary.txt
done
