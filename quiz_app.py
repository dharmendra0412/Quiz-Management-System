import json
import os
import random

# The name of the file where quizzes are stored
DB_FILE = "quizzes.json"

class QuizManager:
    """
    Manages the creation, loading, and saving of quizzes.
    Handles all interactions with the JSON database file.
    """
    
    def __init__(self):
        """Initializes the QuizManager by loading existing quizzes."""
        self.quizzes = self.load_quizzes()

    def load_quizzes(self):
        """
        Loads the quizzes from the JSON file.
        Returns an empty dictionary if the file doesn't exist or is empty.
        """
        if not os.path.exists(DB_FILE):
            return {}  # No file, return empty quiz list
        
        try:
            with open(DB_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}  # File is corrupt or empty, return empty
    
    def save_quizzes(self):
        """Saves the current quiz dictionary to the JSON file."""
        with open(DB_FILE, 'w') as f:
            json.dump(self.quizzes, f, indent=4)
    
    def list_quizzes(self):
        """Prints a list of all available quiz names."""
        if not self.quizzes:
            print("No quizzes available.")
            return False
        
        print("\n--- Available Quizzes ---")
        for i, quiz_name in enumerate(self.quizzes.keys(), 1):
            print(f"  {i}. {quiz_name}")
        return True

    def create_quiz(self):
        """
        Prompts the admin to create a new, empty quiz.
        """
        quiz_name = input("Enter the name for the new quiz: ").strip()
        
        if not quiz_name:
            print("Quiz name cannot be empty.")
            return
            
        if quiz_name in self.quizzes:
            print(f"A quiz with the name '{quiz_name}' already exists.")
        else:
            self.quizzes[quiz_name] = []  # Create an empty list for questions
            self.save_quizzes()
            print(f"Quiz '{quiz_name}' created successfully!")
            
    def add_question(self):
        """
        Prompts the admin to add a new question to an existing quiz.
        """
        if not self.list_quizzes():
            return
        
        try:
            choice = int(input("Enter the number of the quiz to add a question to: "))
            quiz_name = list(self.quizzes.keys())[choice - 1]
        except (ValueError, IndexError):
            print("Invalid choice.")
            return

        print(f"\nAdding a new question to '{quiz_name}':")
        
        question_text = input("Enter the question: ").strip()
        if not question_text:
            print("Question cannot be empty.")
            return

        # Get options
        options = []
        for i in range(4):
            option = input(f"Enter option {i+1}: ").strip()
            if not option:
                print("Option cannot be empty.")
                return
            options.append(option)
        
        # Get correct answer
        while True:
            try:
                correct_choice = int(input("Enter the number of the correct option (1-4): "))
                if 1 <= correct_choice <= 4:
                    correct_answer = options[correct_choice - 1]
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Create the question dictionary
        new_question = {
            "question": question_text,
            "options": options,
            "answer": correct_answer
        }
        
        # Add to the quiz and save
        self.quizzes[quiz_name].append(new_question)
        self.save_quizzes()
        print("Question added successfully!")

class QuizTaker:
    """
    Handles the logic for a user taking a quiz.
    """
    import json
import os
import random

# The name of the file where quizzes are stored
DB_FILE = "quizzes.json"

class QuizManager:
    """
    Manages the creation, loading, and saving of quizzes.
    Handles all interactions with the JSON database file.
    """
    
    def __init__(self):
        """Initializes the QuizManager by loading existing quizzes."""
        self.quizzes = self.load_quizzes()

    def load_quizzes(self):
        """
        Loads the quizzes from the JSON file.
        Returns an empty dictionary if the file doesn't exist or is empty.
        """
        if not os.path.exists(DB_FILE):
            return {}  # No file, return empty quiz list
        
        try:
            with open(DB_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}  # File is corrupt or empty, return empty
    
    def save_quizzes(self):
        """Saves the current quiz dictionary to the JSON file."""
        with open(DB_FILE, 'w') as f:
            json.dump(self.quizzes, f, indent=4)
    
    def list_quizzes(self):
        """Prints a list of all available quiz names."""
        if not self.quizzes:
            print("No quizzes available.")
            return False
        
        print("\n--- Available Quizzes ---")
        for i, quiz_name in enumerate(self.quizzes.keys(), 1):
            print(f"  {i}. {quiz_name}")
        return True

    def create_quiz(self):
        """
        Prompts the admin to create a new, empty quiz.
        """
        quiz_name = input("Enter the name for the new quiz: ").strip()
        
        if not quiz_name:
            print("Quiz name cannot be empty.")
            return
            
        if quiz_name in self.quizzes:
            print(f"A quiz with the name '{quiz_name}' already exists.")
        else:
            self.quizzes[quiz_name] = []  # Create an empty list for questions
            self.save_quizzes()
            print(f"Quiz '{quiz_name}' created successfully!")
            
    def add_question(self):
        """
        Prompts the admin to add a new question to an existing quiz.
        """
        if not self.list_quizzes():
            return
        
        try:
            choice = int(input("Enter the number of the quiz to add a question to: "))
            quiz_name = list(self.quizzes.keys())[choice - 1]
        except (ValueError, IndexError):
            print("Invalid choice.")
            return

        print(f"\nAdding a new question to '{quiz_name}':")
        
        question_text = input("Enter the question: ").strip()
        if not question_text:
            print("Question cannot be empty.")
            return

        # Get options
        options = []
        for i in range(4):
            option = input(f"Enter option {i+1}: ").strip()
            if not option:
                print("Option cannot be empty.")
                return
            options.append(option)
        
        # Get correct answer
        while True:
            try:
                correct_choice = int(input("Enter the number of the correct option (1-4): "))
                if 1 <= correct_choice <= 4:
                    correct_answer = options[correct_choice - 1]
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Create the question dictionary
        new_question = {
            "question": question_text,
            "options": options,
            "answer": correct_answer
        }
        
        # Add to the quiz and save
        self.quizzes[quiz_name].append(new_question)
        self.save_quizzes()
        print("Question added successfully!")

class QuizTaker:
    """
    Handles the logic for a user taking a quiz.
    """
    
    def __init__(self, quiz_questions):
        """
        Initializes the QuizTaker with a list of questions.
        """
        self.questions = random.sample(quiz_questions, len(quiz_questions)) # Shuffle questions
        self.score = 0
    
    def run_quiz(self):
        """Runs the quiz, prompting the user and tracking the score."""
        if not self.questions:
            print("This quiz has no questions! Tell an admin.")
            return
            
        print("\n--- Starting Quiz ---")
        
        for i, q_data in enumerate(self.questions, 1):
            print(f"\nQuestion {i} of {len(self.questions)}:")
            print(f"  {q_data['question']}")
            
            # Shuffle options for display
            options = q_data['options']
            random.shuffle(options)
            
            for j, option in enumerate(options, 1):
                print(f"  {j}. {option}")
            
            # Get user's answer
            while True:
                try:
                    user_choice = int(input("Your answer (1-4): "))
                    if 1 <= user_choice <= len(options):
                        break
                    else:
                        print(f"Invalid choice. Please enter a number between 1 and {len(options)}.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            
            user_answer = options[user_choice - 1]
            correct_answer = q_data['answer']
            
            # Check answer
            if user_answer == correct_answer:
                print("Correct! 🎉")
                self.score += 1
            else:
                print(f"Wrong. 😟 The correct answer was: {correct_answer}")
        
        # Show final score
        print("\n--- Quiz Complete ---")
        print(f"Your final score is: {self.score} / {len(self.questions)}")
        percentage = (self.score / len(self.questions)) * 100
        print(f"Percentage: {percentage:.2f}%")

# --- Main Application Logic ---

def admin_menu(manager):
    """Displays the admin menu and handles admin choices."""
    while True:
        print("\n--- 🛠️ Admin Menu ---")
        print("  1. Create a new quiz")
        print("  2. Add a question to a quiz")
        print("  3. List all quizzes")
        print("  4. Back to main menu")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            manager.create_quiz()
        elif choice == '2':
            manager.add_question()
        elif choice == '3':
            manager.list_quizzes()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu(manager):
    """Displays the user menu for taking a quiz."""
    print("\n--- 🎓 Take a Quiz ---")
    if not manager.list_quizzes():
        return
    
    try:
        quiz_list = list(manager.quizzes.keys())
        choice = int(input(f"Enter the number of the quiz you want to take (1-{len(quiz_list)}): "))
        quiz_name = quiz_list[choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return

    quiz_data = manager.quizzes[quiz_name]
    
    if not quiz_data:
        print(f"The quiz '{quiz_name}' has no questions. Please contact an admin.")
        return
        
    taker = QuizTaker(quiz_data)
    taker.run_quiz()

def main():
    """The main function of the application."""
    manager = QuizManager()
    
    while True:
        print("\n======= Welcome to the Quiz Management System =======")
        print("  1. Take a quiz")
        print("  2. Admin options")
        print("  3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            user_menu(manager)
        elif choice == '2':
            admin_menu(manager)
        elif choice == '3':
            print("Thank you for using the Quiz Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
    def __init__(self, quiz_questions):
        """
        Initializes the QuizTaker with a list of questions.
        """
        self.questions = random.sample(quiz_questions, len(quiz_questions)) # Shuffle questions
        self.score = 0
    
    def run_quiz(self):
        """Runs the quiz, prompting the user and tracking the score."""
        if not self.questions:
            print("This quiz has no questions! Tell an admin.")
            return
            
        print("\n--- Starting Quiz ---")
        
        for i, q_data in enumerate(self.questions, 1):
            print(f"\nQuestion {i} of {len(self.questions)}:")
            print(f"  {q_data['question']}")
            
            # Shuffle options for display
            options = q_data['options']
            random.shuffle(options)
            
            for j, option in enumerate(options, 1):
                print(f"  {j}. {option}")
            
            # Get user's answer
            while True:
                try:
                    user_choice = int(input("Your answer (1-4): "))
                    if 1 <= user_choice <= len(options):
                        break
                    else:
                        print(f"Invalid choice. Please enter a number between 1 and {len(options)}.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            
            user_answer = options[user_choice - 1]
            correct_answer = q_data['answer']
            
            # Check answer
            if user_answer == correct_answer:
                print("Correct! 🎉")
                self.score += 1
            else:
                print(f"Wrong. 😟 The correct answer was: {correct_answer}")
        
        # Show final score
        print("\n--- Quiz Complete ---")
        print(f"Your final score is: {self.score} / {len(self.questions)}")
        percentage = (self.score / len(self.questions)) * 100
        print(f"Percentage: {percentage:.2f}%")

# --- Main Application Logic ---

def admin_menu(manager):
    """Displays the admin menu and handles admin choices."""
    while True:
        print("\n--- 🛠️ Admin Menu ---")
        print("  1. Create a new quiz")
        print("  2. Add a question to a quiz")
        print("  3. List all quizzes")
        print("  4. Back to main menu")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            manager.create_quiz()
        elif choice == '2':
            manager.add_question()
        elif choice == '3':
            manager.list_quizzes()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu(manager):
    """Displays the user menu for taking a quiz."""
    print("\n--- 🎓 Take a Quiz ---")
    if not manager.list_quizzes():
        return
    
    try:
        quiz_list = list(manager.quizzes.keys())
        choice = int(input(f"Enter the number of the quiz you want to take (1-{len(quiz_list)}): "))
        quiz_name = quiz_list[choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return

    quiz_data = manager.quizzes[quiz_name]
    
    if not quiz_data:
        print(f"The quiz '{quiz_name}' has no questions. Please contact an admin.")
        return
        
    taker = QuizTaker(quiz_data)
    taker.run_quiz()

def main():
    """The main function of the application."""
    manager = QuizManager()
    
    while True:
        print("\n======= Welcome to the Quiz Management System =======")
        print("  1. Take a quiz")
        print("  2. Admin options")
        print("  3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            user_menu(manager)
        elif choice == '2':
            admin_menu(manager)
        elif choice == '3':
            print("Thank you for using the Quiz Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
