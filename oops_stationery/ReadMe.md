# Pre-requisites
* Python 3.8/3.9

# How to run the code

We have provided scripts to execute the code. The filename which has the main method should be named as `geektrust.py` and should not be renamed to anything else.

Use `run.sh` if you are Linux/Unix/macOS Operating systems and `run.bat` if you are on Windows. Both the files run the commands silently and prints only output from the input files in the directory `smaple_input`

Internally both the scripts run the following commands 

* `python -m geektrust sample_input/input1.txt` - This will run the solution passing in the sample input file `input1.txt` as the command line argument.
* `python -m geektrust sample_input/input2.txt` - This will run the solution passing in the sample input file `input2.txt` as the command line argument.
* `python -m geektrust sample_input/input3.txt` - This will run the solution passing in the sample input file `input3.txt` as the command line argument.
* `python -m geektrust sample_input/input4.txt` - This will run the solution passing in the sample input file `input4.txt` as the command line argument.

 We expect your program to take the location to the text file as parameter. Input needs to be read from a text file, and output should be printed to the console. The text file will contain only commands in the format prescribed by the respective problem. We have added the code snippet to help you read from the file passed as command line argument. 

 # Running the code for multiple test cases

Run `run.sh` or `run.bat` in your local machine to ensure your solution is working correctly. Once confirmed please uplaod it in Geektrust and check for the test cases.

# Help

* You can refer our help documents [here](https://help.geektrust.com)
* You can read build instructions [here](https://github.com/geektrust/coding-problem-artefacts/tree/master/Python#no-build)