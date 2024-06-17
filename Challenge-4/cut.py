import argparse
from utils.utility import file_not_found_error
import re
import sys

def main():
  
  args = sys.argv

  flag = None
  files = None
  deliminator = "\t"

  for arg in args:
    flag_match = re.match(r'-f(.*)' , arg)
    file_match = re.match(r'.*\.(csv|tsv)$' , arg)
    deliminator_match = re.match(r'-d(.*)' , arg)

    if flag_match:
      flag = arg
    elif file_match: 
      files = arg   
    elif deliminator_match:
      deliminator = arg

  if flag is not None and files is not None:
    arr_indices = [int(x.strip()) for x in flag[2:].split(",")]
    if deliminator != "\t":
      deliminator = deliminator[2:]

    with open(files , 'r') as file:
      for line in file:
        chars = [x.strip() for x in line.split(deliminator)]
        string = ""
        for idx in arr_indices:
          string += chars[idx-1] + "\t"
        print(string)

if __name__ == "__main__":
  main()


