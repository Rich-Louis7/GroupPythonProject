def display_lesson():
    print("Welcome to the Programming Lesson on Input and Output!\n")
    print("Today, we will cover the following topics:")
    print("1. Understanding Input and Output")
    print("2. The input() function")
    print("3. The print() function")
    print("4. Formatting Output")
    print("5. File Input and Output\n")

    # Lesson on Understanding Input and Output
    print("--- 1. Understanding Input and Output ---")
    print("Input refers to taking data from the user or an external source into the program.")
    print("Output refers to displaying data to the user or sending data to an external source.\n")

    # Lesson on the input() function
    print("--- 2. The input() function ---")
    print("The input() function allows you to take input from the user. It returns the data as a string.")
    print("Example: name = input('Enter your name: ') stores the input in the variable 'name'.\n")

    # Lesson on the print() function
    print("--- 3. The print() function ---")
    print("The print() function is used to display output to the user.")
    print("Example: print('Hello, World!') will display the text 'Hello, World!' to the user.\n")

    # Lesson on Formatting Output
    print("--- 4. Formatting Output ---")
    print("You can format output using f-strings, which allow you to embed variables directly into strings.")
    print("Example: name = 'John'; print(f'Hello, {name}!') will display 'Hello, John!'.")
    print("You can also format numbers using '{:.2f}' to display floating-point numbers to 2 decimal places.\n")

    # Lesson on File Input and Output
    print("--- 5. File Input and Output ---")
    print("You can read and write to files using Python. To read, use open(filename, 'r').")
    print("Example: with open('file.txt', 'r') as file: data = file.read() will read the contents of 'file.txt'.")
    print("To write to a file, use open(filename, 'w') or 'a' for appending.")
    print("Example: with open('output.txt', 'w') as file: file.write('Hello, file!') writes text to 'output.txt'.\n")

    # Mentioning Redirection (more advanced)
    print("Advanced: You can also redirect input and output using command-line redirection.")
    print("For example, python script.py < input.txt > output.txt would redirect input from 'input.txt' and output to 'output.txt'.\n")

def quiz():
    print("--- Quiz Time! ---\n")
    score = 0

    # Question 1: input() function
    print("1. What type of data does the input() function return?")
    print("a) Integer")
    print("b) String")
    print("c) Float")
    print("d) Boolean")
    answer1 = input("Enter your answer (a/b/c/d): ")
    if answer1.lower() == "b":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The input() function always returns a string.\n")

    # Question 2: print() function
    print("2. Which of the following is used to display output in Python?")
    print("a) input()")
    print("b) display()")
    print("c) print()")
    print("d) output()")
    answer2 = input("Enter your answer (a/b/c/d): ")
    if answer2.lower() == "c":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The print() function is used for displaying output.\n")

    # Question 3: Formatting Output
    print("3. How would you display a floating-point number with 2 decimal places in Python?")
    print("a) {:.0f}")
    print("b) {:.2f}")
    print("c) {:.3f}")
    print("d) {:.1f}")
    answer3 = input("Enter your answer (a/b/c/d): ")
    if answer3.lower() == "b":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct format is '{:.2f}' for rounding to 2 decimal places.\n")

    return score

def grade(score):
    print(f"\nYour score is {score} out of 3.")
    if score == 3:
        print("Excellent! You have a great understanding of Input and Output concepts.")
    elif score == 2:
        print("Good job! You have a decent understanding, but review the topics again.")
    else:
        print("You need to review the topics more. Keep practicing and learning!")

def main():
    display_lesson()
    score = quiz()
    grade(score)

# Start the program
main()
