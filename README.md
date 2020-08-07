# Quiz-Maker
This application will generate a quiz with 5 questions which are randomly selected from a questions file.

Before starting this application you will need a questions file. The questions file must be formatted in a specific way
in order for it to work.

The questions file must have the questions in its entirety on odd numbered lines, and an answer set on even numbered lines.

The answer set must be formatted like so: A)ans B)fake_ans C)fake_ans D)fake_ans where a is the correct answer.

You must make sure there is no new line after the last question and answer set as the file must contain an even number of lines.

math_questions.txt has already been made as an example.

After you have the correct formatted questions file you can start the application and browse for the file, which will then generate the quiz.

The user will enter either a, b, c, or d as their answers and after the quiz is finished it will print out the number of questions the user got correct.

Notes: 
Not alot of checks to make sure the user is inputting and interacting with the application correctly.

The application has only been checked against .txt files.
