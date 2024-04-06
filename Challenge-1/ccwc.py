import argparse

def file_not_found_error():
    print("The file doesn't exists")

def count_bytes(filename):
    try:
        with open (filename , 'r') as file:
            byte_count = len(file.read())
            print(f"The byte count is {byte_count} bytes")
    except FileNotFoundError:
        file_not_found_error()
    except Exception as err:
        print(f"There was some unknown error {err}")

def count_chars(filename):

    char_freq = {}
    total_char_count = 0
    try:
        with open(filename , 'r') as file:
            for line in file:
                total_char_count += len(line)
                for char in line:
                    char_freq[char] = char_freq.get(char,0) + 1
        print(f"The total_char_count {total_char_count} and char_freq dict {char_freq}")
    except FileNotFoundError:
        file_not_found_error()
    
def count_lines(filename):
    total_line_count = 0
    try:
        with open(filename , 'r') as file:
            for line in file:
                total_line_count += 1
        print(f"Total lines in the file {total_line_count}")
    except FileNotFoundError:
        file_not_found_error()

def count_words(filename):
    total_words_count = 0
    try:
        with open(filename , 'r') as file:
            for line in file:
                total_words_count += (len(line.split()))
        print(f"Total words in the file {total_words_count}")
    except FileNotFoundError:
        file_not_found_error()

def main():
    parser = argparse.ArgumentParser(description='Copy of wc in linux')

    operations = {
        'filename_bytes' : count_bytes,
        'filename_words' : count_words,
        'filename_lines' : count_lines,
        'filename_chars' : count_chars
    }

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-c' , '--bytes' , dest='filename_bytes' , action='store' , help="Count bytes in a file")
    group.add_argument('-m' , '--chars' , dest='filename_chars' , action='store' , help="Count chars in a file")
    group.add_argument('-l' , '--lines' , dest='filename_lines' , action='store' , help="Count lines in a file")
    group.add_argument('-w' , '--words' , dest='filename_words' , action='store' , help="Count words in a file")
    args = parser.parse_args()

    operation = None

    for operation_type,filename in vars(args).items():
        if filename:
            operation = operations.get(operation_type)
            if operation:
                operation(filename)
            break
    
    

if __name__ == '__main__':
    main()
    

