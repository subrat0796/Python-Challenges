import json
import argparse

def is_valid_json(json_file):
    try:
        with open(json_file , 'r') as file:
            json.load(file)
        return True
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON : {e}")
        return False
    except FileNotFoundError:
        print(f"File not found {json_file}")
        return False
    
def main():
    parser = argparse.ArgumentParser(description='Json Parser in Linux')

    parser.add_argument('--file' , '--json_file' , dest='json_file')
    args = parser.parse_args()

    if is_valid_json(args.json_file):
        print("This is a valid json file")
    else:
        print("This is not a valid json file")

if __name__ == '__main__':
    main()

