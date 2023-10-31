# I called this project - Collection Framework

### Package "collect_framework_FEDONYUK_ANATOLIY" - this software package is an open source product and is distributed free of charge) 
### This package counts the number of unique characters passed to a text or text format file.

#### The package is designed both to work in normal mode python application and for user interaction CLI. 
#### To do this, the package implements a command line interface CLI using the "click" library.
#### The application uses "pytest" test framework; the 16 tests obtained with it cover the entire application code!
#### This was confirmed by the “coverage” utility - the coverage was 96%, the tests used mocks to stub file reading.
#### Also, the most expensive function for the processor is optimized - by caching.
#### Using the 'pip' and 'twin' utilities, a full-fledged Python package was created, with all dependencies saved in
#### the 'requirements.txt' file, and uploaded to the index test.pypi.org


#### There are five commands implemented in the command line interface:
1. --string <your text> for direct text entry.
2. -s <your text> short form of the string command for entering text directly.
3. --file <path to file> to enter text directly from the user's file.
4. -f <path to file> is a short form of the command for entering text directly from the user's file.
5. --help a convenient help file for working with the package via the command line.

**The package also implements all the necessary tests and checks for errors in the operation of the program and its command line. All tests are located in the tests folder and can be run in one package, which will run 16 tests covering all aspects of the package!
The package has also been optimized for working with strings through the use of a cache.**

***At the end I will give the text issued by the --help command of the application:***
```
Usage: collect_framework.py [OPTIONS]
  get_number_char. In this case, the --file command will take precedence!

Options:
  -s, --string TEXT  The string to process
  -f, --file PATH    The path to the input text file
  --help             Show this message and exit.
```