Regular expression
0. Simply matching School
Repetition Token #0
2. Repetition Token #1
3. Repetition Token #2
4. Repetition Token #3

0x06. Regular expression
 By Sylvain Kalache
 Weight: 1
 Ongoing second chance project - started 01-18-2022, must end by 01-22-2022 (in about 15 hours) - you're done with 0% of tasks.
 QA review fully automated.
In a nutshell…
Auto QA review: 1.0/24 mandatory & 0.0/9 optional
Altogether:  4.17%
Mandatory: 4.17%
Optional: 0.0%
Calculation:  4.17% + (4.17% * 0.0%)  == 4.17%
Concepts
For this project, students are expected to look at this concept:

Regular Expression
Background Context
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
Resources
Read or watch:

Regular expressions - basics
Regular expressions - advanced
Rubular is your best friend
Use a regular expression against a problem: now you have 2 problems
Learn Regular Expressions with simple, interactive exercises
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 20.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
The first line of all your Bash scripts should be exactly #!/usr/bin/env ruby
All your regex must be built for the Oniguruma library
Quiz questions
Show

Tasks
0. Simply matching School
mandatory
Score: 0.00% (Checks completed: 0.00%)


Requirements:

The regular expression must match School
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
Example:

sylvain@ubuntu$ ./0-simply_match_holberton.rb School | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Best School" | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "School Best School" | cat -e
SchoolSchool$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Grace Hopper" | cat -e
$
Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x06-regular_expressions
File: 0-simply_match_school.rb
    
1. Repetition Token #0
mandatory
Score: 0.00% (Checks completed: 0.00%)


Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x06-regular_expressions
File: 1-repetition_token_0.rb
    
2. Repetition Token #1
mandatory
Score: 0.00% (Checks completed: 0.00%)


Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x06-regular_expressions
File: 2-repetition_token_1.rb
    
3. Repetition Token #2
mandatory
Score: 0.00% (Checks completed: 0.00%)


Requirements:
4. Repetition Token #3
5. Not quite HBTN yet
