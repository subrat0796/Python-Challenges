# Running of the applciation

Run the commands in a sequential order

1. chmod +x parser (It helps to make this an executable)
2. sudo mv parser /usr/local/bin (common location for storing exceutable scripts on unix-like systems)
3. parser -c tests/step1/valid.json (run the text file)

# Understanding of the application

The validate_json is a function that takes in a filename and parses it completly to json and checks if it is a valid json or not using the json module
