
# 🐍 Quiz Management System

**Author:** Dharmendra Kumar

A comprehensive, console-based quiz application built with Python. This project allows for the complete management of quizzes, from creation to execution, and saves all data persistently to a JSON file.

This system is built with a clean, object-oriented design, separating admin functionalities (`QuizManager`) from user functionalities (`QuizTaker`).

---

## 🚀 How to Run

1.  **Clone the repository:**
    ```sh
    # Replace with your actual repository URL
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
    ```
2.  **Navigate to the directory:**
    ```sh
    cd YOUR_REPOSITORY_NAME
    ```
3.  **Run the application:**
    ```sh
    python quiz_app.py
    ```
    *(Note: The first time you run it, a `quizzes.json` file will be created in the directory to store your quizzes.)*

---

## ⚙️ Features

### 🛠️ Admin Functions
* **Create Quiz:** Dynamically create new, named quizzes.
* **Add Questions:** Add multiple-choice questions (with 4 options) to any existing quiz.
* **Persistent Storage:** All quizzes and questions are automatically saved to `quizzes.json` and reloaded every time the program starts.
* **Robust Error Handling:** The application gracefully handles invalid inputs (e.g., text instead of numbers) and file-not-found errors.

### 🎓 User Functions
* **List & Select:** View a complete list of all available quizzes and choose one to take.
* **Randomized Experience:** Both the order of the questions and the order of the multiple-choice options are shuffled every time a quiz is taken.
* **Instant Feedback:** Receive immediate "Correct!" or "Wrong" feedback after each question.
* **Final Score:** Get a detailed score and percentage at the end of the quiz.

---

## 💻 Technical Stack

* **Language:** Python 3
* **Data Storage:** JSON (using Python's built-in `json` module)
* **Core Modules:** `os` (for file system checks), `random` (for shuffling)

---

## 📈 Possible Future Improvements

This project serves as a strong foundation. Future enhancements could include:
* **User Accounts:** A login system to protect the admin area and track user scores.
* **Expanded Admin Tools:** Add functionality to delete quizzes or edit existing questions.
* **Score History:** Save scores for each user to track their progress over time.
* **GUI Interface:** Rebuild the application with a graphical interface using **Tkinter** or **PyQt**.
