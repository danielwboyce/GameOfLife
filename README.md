#Report Cards

##About

This program functions by taking data from four .csv files about a student, their test results, and their courses. It parses the files into a format that Python can more easily handle (a series of maps) and then calculates each student's grades in each of their courses. This is accomplished through a simple understanding of how the data between the different .csv files is interrelated (a diagram can be found [here](https://www.danielwboyce.com/img/ReportCardDataInterrelated.png)) and then running simple calculations on test results to find course grades.

##Running the program

To install requirements, run

```pip install -r requirements.txt```

Then to run the program, run

```python3 (directory to Main.py) (directory to courses.csv) (directory to marks.csv) (directory to students.csv) (directory to tests.csv) (directory where output.txt should be written)```

For example, if you're operating with all your files in the directory you're executing from, you would execute

```python3 Main.py courses.csv marks.csv students.csv tests.csv ouput.txt```

##My tests

Note: The largest of the test cases I used is included in the folder test_data, including the appropriate output file. The output was verified with Excel for the test cases I created.
