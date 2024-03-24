import argparse

def count_bytes(filename):
    try:
        with open (filename , 'r') as file:
            byte_count = len(file.read())
            print(f"The byte count is {byte_count} bytes")
    except FileNotFoundError:
        print("The file doesn't exists")
    except Exception as err:
        print(f"There was some unknown error {err}")

def main():
    parser = argparse.ArgumentParser(description='Copy of wc in linux')

    parser.add_argument('-c' , '--bytes' , dest='filename' , required=False, help="Count bytes in a file")

    args = parser.parse_args()
    count_bytes(args.filename)

if __name__ == '__main__':
    main()
    

