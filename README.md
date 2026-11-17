🧮 Python Calculator with Memory & History

A command-line calculator built in Python that supports basic arithmetic operations, memory functions, and calculation history tracking.

🚀 Features
Basic Operations
Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
Division by zero handling
Memory Functions
M+ → Add current value to memory
M- → Subtract current value from memory
MR → Recall stored memory value
MC → Clear memory
History Functions
H → View calculation history
CH → Clear calculation history
Additional Features
Continuous calculations using previous results
Input validation for numbers
Error handling for invalid operations
Restart calculator without exiting
Exit option (q)
📂 Project Structure
Plain Text
calculator-project/
│
├── main.py
├── art.py
└── README.md
Files
File	Description
main.py	Contains calculator logic and functionality
art.py	Stores calculator ASCII logo
README.md	Project documentation
🛠 Technologies Used
Python 3
Functions
Dictionaries
Lists
Exception Handling
Recursion
Global Variables
📋 How It Works

The calculator uses a dictionary to associate mathematical symbols with functions.

Python
operations = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide,
}

This makes it easy to call operations dynamically based on user input.

Example:

Python
answer = operations5, 3
print(answer)

Output:

Plain Text
8
▶️ Installation
Clone the Repository
Shell
git clone https://github.com/your-username/calculator-project.git
Navigate to Project Directory
Shell
cd calculator-project
Run the Application
Shell
python main.py
💻 Example Usage
Plain Text
What is the first number?: 10
 
+
-
*
/
 
Pick an operation: +
 
What is the next number?: 5
 
10 + 5 = 15
 
Type 'y' to continue calculating with 15,
or type 'n' to start a new calculation,
or 'q' to quit:
🧠 Memory Example
Plain Text
Current Value: 20
 
Pick an operation: M+
 
Memory: 20
 
Pick an operation: MR
 
Memory recalled: 20
📖 History Example
Plain Text
Calculation History:
 
10 + 5 = 15
15 * 2 = 30
30 - 10 = 20
🔍 Concepts Practiced

This project demonstrates:

Function creation and calling
Dictionary-based operation mapping
User input handling
Exception handling using try-except
Global variables
Loop control (while)
Lists for storing history
Program state management
Modular programming
⚠️ Error Handling

The application handles:

Invalid Number Input
Plain Text
Invalid input, please enter a number.
Invalid Operation
Plain Text
Invalid input, please enter a valid operation.
Division by Zero
Plain Text
Cannot divide by zero.
