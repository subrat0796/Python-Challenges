# Running of the application

Run the commands in a sequential order

1. chmod +x ccwc (It helps to make this an executable)
2. sudo mv ccwc /usr/local/bin (common location for storing exceutable scripts on unix-like systems)
3. ccwc -c test.txt (run the text file)

# Understanding of the application

The count_bytes function takes the filename into account and counts the no of bytes in the file

The main function is responsible for creating a command line argument using argparse and it adds up arguments . Finally it takes up the args.filename and pushes it to count_bytes function

The final if statement is added to evaluate this as a python idiom that checks whether the python script is being run as the main program or if it is being imported as a module into another script

<!-- ## Each function defination

1. count_bytes() -->
