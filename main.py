"""
main.py - Digital Quiz App with Statistics
Complete GUI Application using Tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from quiz_app import QuizApp
from stats_manager import StatsManager
import sys


class QuizGUI:
    """Main GUI Application for Digital Quiz App"""
    
    def __init__(self, root):
        """Initialize the main application"""
        self.root = root
        self.root.title("Digital Quiz App with Stats")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Initialize quiz and stats managers
        self.quiz = QuizApp()
        self.stats = StatsManager()
        
        # Color scheme
        self.bg_color = "#2C3E50"
        self.fg_color = "#ECF0F1"
        self.button_color = "#3498DB"
        self.button_hover = "#2980B9"
        self.success_color = "#27AE60"
        self.error_color = "#E74C3C"
        
        # Configure root window
        self.root.configure(bg=self.bg_color)
        
        # Show main menu
        self.show_main_menu()
    
    def clear_window(self):
        """Clear all widgets from the window"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    # ==================== MAIN MENU ====================
    
    def show_main_menu(self):
        """Display the main menu"""
        self.clear_window()
        
        # Title
        title_label = tk.Label(
            self.root,
            text="🎯 Digital Quiz App",
            font=("Arial", 32, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        )
        title_label.pack(pady=50)
        
        subtitle_label = tk.Label(
            self.root,
            text="Test Your Knowledge with Live Questions",
            font=("Arial", 14),
            bg=self.bg_color,
            fg=self.fg_color
        )
        subtitle_label.pack(pady=10)
        
        # Button frame
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=50)
        
        # Start Quiz Button
        start_btn = tk.Button(
            button_frame,
            text="📝 Start Quiz",
            font=("Arial", 16, "bold"),
            bg=self.button_color,
            fg="white",
            width=20,
            height=2,
            command=self.show_quiz_setup,
            cursor="hand2"
        )
        start_btn.pack(pady=15)
        
        # View Statistics Button
        stats_btn = tk.Button(
            button_frame,
            text="📊 View Statistics",
            font=("Arial", 16, "bold"),
            bg=self.success_color,
            fg="white",
            width=20,
            height=2,
            command=self.show_statistics,
            cursor="hand2"
        )
        stats_btn.pack(pady=15)
        
        # Exit Button
        exit_btn = tk.Button(
            button_frame,
            text="❌ Exit",
            font=("Arial", 16, "bold"),
            bg=self.error_color,
            fg="white",
            width=20,
            height=2,
            command=self.exit_app,
            cursor="hand2"
        )
        exit_btn.pack(pady=15)
        
        # Footer
        footer_label = tk.Label(
            self.root,
            text="Powered by Open Trivia Database API",
            font=("Arial", 10),
            bg=self.bg_color,
            fg=self.fg_color
        )
        footer_label.pack(side="bottom", pady=20)
    
    # ==================== QUIZ SETUP ====================
    
    def show_quiz_setup(self):
        """Display quiz setup/configuration window"""
        self.clear_window()
        
        # Title
        title_label = tk.Label(
            self.root,
            text="⚙️ Quiz Setup",
            font=("Arial", 28, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        )
        title_label.pack(pady=30)
        
        # Setup frame
        setup_frame = tk.Frame(self.root, bg=self.bg_color)
        setup_frame.pack(pady=20)
        
        # Number of Questions
        tk.Label(
            setup_frame,
            text="Number of Questions:",
            font=("Arial", 14),
            bg=self.bg_color,
            fg=self.fg_color
        ).grid(row=0, column=0, padx=20, pady=15, sticky="w")
        
        self.questions_var = tk.StringVar(value="10")
        questions_spinbox = tk.Spinbox(
            setup_frame,
            from_=5,
            to=20,
            textvariable=self.questions_var,
            font=("Arial", 12),
            width=15
        )
        questions_spinbox.grid(row=0, column=1, padx=20, pady=15)
        
        # Category Selection
        tk.Label(
            setup_frame,
            text="Category:",
            font=("Arial", 14),
            bg=self.bg_color,
            fg=self.fg_color
        ).grid(row=1, column=0, padx=20, pady=15, sticky="w")
        
        categories = list(self.quiz.get_categories().keys())
        self.category_var = tk.StringVar(value=categories[0])
        category_combo = ttk.Combobox(
            setup_frame,
            textvariable=self.category_var,
            values=categories,
            font=("Arial", 12),
            width=25,
            state="readonly"
        )
        category_combo.grid(row=1, column=1, padx=20, pady=15)
        
        # Difficulty Selection
        tk.Label(
            setup_frame,
            text="Difficulty:",
            font=("Arial", 14),
            bg=self.bg_color,
            fg=self.fg_color
        ).grid(row=2, column=0, padx=20, pady=15, sticky="w")
        
        difficulties = self.quiz.get_difficulties()
        self.difficulty_var = tk.StringVar(value=difficulties[0])
        difficulty_combo = ttk.Combobox(
            setup_frame,
            textvariable=self.difficulty_var,
            values=difficulties,
            font=("Arial", 12),
            width=25,
            state="readonly"
        )
        difficulty_combo.grid(row=2, column=1, padx=20, pady=15)
        
        # Buttons
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=40)
        
        start_btn = tk.Button(
            button_frame,
            text="🚀 Start Quiz",
            font=("Arial", 14, "bold"),
            bg=self.success_color,
            fg="white",
            width=15,
            height=2,
            command=self.start_quiz,
            cursor="hand2"
        )
        start_btn.pack(side="left", padx=10)
        
        back_btn = tk.Button(
            button_frame,
            text="⬅️ Back",
            font=("Arial", 14, "bold"),
            bg=self.error_color,
            fg="white",
            width=15,
            height=2,
            command=self.show_main_menu,
            cursor="hand2"
        )
        back_btn.pack(side="left", padx=10)
    
    def start_quiz(self):
        """Start the quiz with selected options"""
        try:
            # Get selections
            num_questions = int(self.questions_var.get())
            category_name = self.category_var.get()
            difficulty = self.difficulty_var.get()
            
            # Get category ID
            categories = self.quiz.get_categories()
            category_id = categories[category_name]
            
            # Store for stats
            self.quiz.quiz_category = category_name
            self.quiz.quiz_difficulty = difficulty if difficulty != "Any Difficulty" else "Mixed"
            
            # Fetch questions
            loading_label = tk.Label(
                self.root,
                text="⏳ Loading questions...",
                font=("Arial", 16),
                bg=self.bg_color,
                fg=self.fg_color
            )
            loading_label.pack(pady=20)
            self.root.update()
            
            difficulty_param = None if difficulty == "Any Difficulty" else difficulty
            
            if self.quiz.fetch_questions(num_questions, category_id, difficulty_param):
                self.show_quiz_window()
            else:
                messagebox.showerror(
                    "Error",
                    "Failed to fetch questions. Please check your internet connection."
                )
                self.show_quiz_setup()
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.show_quiz_setup()
    
    # ==================== QUIZ WINDOW ====================
    
    def show_quiz_window(self):
        """Display the quiz question window"""
        self.clear_window()
        
        question = self.quiz.get_current_question()
        if not question:
            self.show_results()
            return
        
        current, total = self.quiz.get_progress()
        
        # Progress bar
        progress_frame = tk.Frame(self.root, bg=self.bg_color)
        progress_frame.pack(fill="x", padx=20, pady=10)
        
        progress_label = tk.Label(
            progress_frame,
            text=f"Question {current} of {total}",
            font=("Arial", 14, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        )
        progress_label.pack()
        
        # Category and Difficulty
        info_label = tk.Label(
            self.root,
            text=f"📁 {question['category']} | ⭐ {question['difficulty'].title()}",
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.fg_color
        )
        info_label.pack(pady=5)
        
        # Question
        question_frame = tk.Frame(self.root, bg="white", relief="solid", borderwidth=2)
        question_frame.pack(padx=40, pady=20, fill="both", expand=True)
        
        question_label = tk.Label(
            question_frame,
            text=question['question'],
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#2C3E50",
            wraplength=700,
            justify="center"
        )
        question_label.pack(pady=30)
        
        # Answer options
        self.selected_answer = tk.StringVar()
        
        options_frame = tk.Frame(self.root, bg=self.bg_color)
        options_frame.pack(pady=20)
        
        for i, answer in enumerate(question['all_answers']):
            radio_btn = tk.Radiobutton(
                options_frame,
                text=answer,
                variable=self.selected_answer,
                value=answer,
                font=("Arial", 13),
                bg=self.bg_color,
                fg=self.fg_color,
                selectcolor="#34495E",
                activebackground=self.bg_color,
                activeforeground=self.fg_color,
                wraplength=600,
                justify="left",
                cursor="hand2"
            )
            radio_btn.pack(anchor="w", padx=50, pady=8)
        
        # Submit button
        submit_btn = tk.Button(
            self.root,
            text="✅ Submit Answer",
            font=("Arial", 14, "bold"),
            bg=self.success_color,
            fg="white",
            width=20,
            height=2,
            command=self.submit_answer,
            cursor="hand2"
        )
        submit_btn.pack(pady=20)
    
    def submit_answer(self):
        """Submit the selected answer"""
        answer = self.selected_answer.get()
        
        if not answer:
            messagebox.showwarning("Warning", "Please select an answer!")
            return
        
        # Check answer
        is_correct = self.quiz.check_answer(answer)
        
        # Show feedback
        if is_correct:
            messagebox.showinfo("✅ Correct!", "Well done! That's the correct answer.")
        else:
            correct_answer = self.quiz.get_current_question()['correct_answer']
            messagebox.showinfo(
                "❌ Incorrect",
                f"Sorry, the correct answer was:\n\n{correct_answer}"
            )
        
        # Move to next question
        if self.quiz.next_question():
            self.show_quiz_window()
        else:
            self.show_results()
    
    # ==================== RESULTS WINDOW ====================
    
    def show_results(self):
        """Display quiz results"""
        self.clear_window()
        
        summary = self.quiz.get_quiz_summary()
        
        # Save to stats
        self.stats.save_quiz_result(summary)
        
        # Title
        title_label = tk.Label(
            self.root,
            text="🎊 Quiz Complete!",
            font=("Arial", 32, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        )
        title_label.pack(pady=30)
        
        # Score card
        score_frame = tk.Frame(self.root, bg="white", relief="solid", borderwidth=3)
        score_frame.pack(padx=50, pady=20)
        
        score_percentage = summary['score_percentage']
        
        # Score display
        score_label = tk.Label(
            score_frame,
            text=f"{score_percentage:.1f}%",
            font=("Arial", 48, "bold"),
            bg="white",
            fg=self.success_color if score_percentage >= 70 else self.error_color
        )
        score_label.pack(pady=20)
        
        # Details
        details_text = f"""
        Correct Answers: {summary['correct_answers']} ✅
        Incorrect Answers: {summary['incorrect_answers']} ❌
        Total Questions: {summary['total_questions']}
        Time Taken: {summary['time_taken_seconds']} seconds
        """
        
        details_label = tk.Label(
            score_frame,
            text=details_text,
            font=("Arial", 14),
            bg="white",
            fg="#2C3E50",
            justify="left"
        )
        details_label.pack(pady=20, padx=40)
        
        # Performance message
        if score_percentage >= 90:
            message = "🌟 Outstanding! You're a genius!"
        elif score_percentage >= 70:
            message = "👏 Great job! Well done!"
        elif score_percentage >= 50:
            message = "👍 Good effort! Keep practicing!"
        else:
            message = "💪 Don't give up! Try again!"
        
        message_label = tk.Label(
            self.root,
            text=message,
            font=("Arial", 16, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        )
        message_label.pack(pady=20)
        
        # Buttons
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=20)
        
        retry_btn = tk.Button(
            button_frame,
            text="🔄 Try Again",
            font=("Arial", 12, "bold"),
            bg=self.button_color,
            fg="white",
            width=15,
            height=2,
            command=self.show_quiz_setup,
            cursor="hand2"
        )
        retry_btn.pack(side="left", padx=10)
        
        stats_btn = tk.Button(
            button_frame,
            text="📊 View Stats",
            font=("Arial", 12, "bold"),
            bg=self.success_color,
            fg="white",
            width=15,
            height=2,
            command=self.show_statistics,
            cursor="hand2"
        )
        stats_btn.pack(side="left", padx=10)
        
        home_btn = tk.Button(
            button_frame,
            text="🏠 Main Menu",
            font=("Arial", 12, "bold"),
            bg=self.error_color,
            fg="white",
            width=15,
            height=2,
            command=self.show_main_menu,
            cursor="hand2"
        )
        home_btn.pack(side="left", padx=10)
    
    # ==================== STATISTICS WINDOW ====================
    
    def show_statistics(self):
        """Display statistics window"""
        self.clear_window()
        
        # Check if there are any stats
        if self.stats.get_total_quizzes() == 0:
            self.show_no_stats()
            return
        
        # Title
        title_label = tk.Label(
            self.root,
            text="📊 Your Statistics",
            font=("Arial", 28, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        )
        title_label.pack(pady=20)
        
        # Get statistics
        stats_summary = self.stats.get_statistics_summary()
        
        # Create scrollable frame
        canvas = tk.Canvas(self.root, bg=self.bg_color, highlightthickness=0)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.bg_color)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((400, 0), window=scrollable_frame, anchor="n")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Main Statistics Card
        main_stats_frame = tk.Frame(scrollable_frame, bg="white", relief="solid", borderwidth=2)
        main_stats_frame.pack(padx=40, pady=10, fill="x")
        
        tk.Label(
            main_stats_frame,
            text="📈 Overall Performance",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#2C3E50"
        ).pack(pady=10)
        
        stats_text = f"""
        Total Quizzes Taken: {stats_summary['total_quizzes']}
        Total Questions Answered: {stats_summary['total_questions_answered']}
        
        📊 Score Statistics (Using SciPy & NumPy):
        Mean Score: {stats_summary['mean_score']}%
        Median Score: {stats_summary['median_score']}%
        Mode Score: {stats_summary['mode_score']}%
        Standard Deviation: {stats_summary['std_deviation']:.2f}
        
        🎯 Performance:
        Overall Accuracy: {stats_summary['overall_accuracy']}%
        Best Score: {stats_summary['best_score']}%
        Worst Score: {stats_summary['worst_score']}%
        """
        
        tk.Label(
            main_stats_frame,
            text=stats_text,
            font=("Arial", 13),
            bg="white",
            fg="#2C3E50",
            justify="left"
        ).pack(pady=15, padx=20)
        
        # Recent Quizzes
        recent_frame = tk.Frame(scrollable_frame, bg="white", relief="solid", borderwidth=2)
        recent_frame.pack(padx=40, pady=10, fill="x")
        
        tk.Label(
            recent_frame,
            text="📝 Recent Quizzes",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#2C3E50"
        ).pack(pady=10)
        
        recent_quizzes = self.stats.get_recent_quizzes(5)
        
        for _, quiz in recent_quizzes.iterrows():
            quiz_info = f"{quiz['date']} | {quiz['category']} | {quiz['difficulty']} | Score: {quiz['score_percentage']:.1f}%"
            tk.Label(
                recent_frame,
                text=quiz_info,
                font=("Arial", 11),
                bg="white",
                fg="#34495E"
            ).pack(pady=3, padx=20, anchor="w")
        
        tk.Label(recent_frame, text="", bg="white").pack(pady=5)
        
        canvas.pack(side="left", fill="both", expand=True, padx=20)
        scrollbar.pack(side="right", fill="y")
        
        # Back button
        back_btn = tk.Button(
            self.root,
            text="⬅️ Back to Menu",
            font=("Arial", 12, "bold"),
            bg=self.error_color,
            fg="white",
            width=20,
            height=2,
            command=self.show_main_menu,
            cursor="hand2"
        )
        back_btn.pack(side="bottom", pady=20)
    
    def show_no_stats(self):
        """Show message when no statistics available"""
        self.clear_window()
        
        title_label = tk.Label(
            self.root,
            text="📊 Statistics",
            font=("Arial", 28, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        )
        title_label.pack(pady=50)
        
        message_label = tk.Label(
            self.root,
            text="No quiz data available yet.\n\nTake a quiz to see your statistics!",
            font=("Arial", 16),
            bg=self.bg_color,
            fg=self.fg_color,
            justify="center"
        )
        message_label.pack(pady=50)
        
        back_btn = tk.Button(
            self.root,
            text="⬅️ Back to Menu",
            font=("Arial", 14, "bold"),
            bg=self.error_color,
            fg="white",
            width=20,
            height=2,
            command=self.show_main_menu,
            cursor="hand2"
        )
        back_btn.pack(pady=30)
    
    # ==================== UTILITY METHODS ====================
    
    def exit_app(self):
        """Exit the application"""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.quit()


# ==================== MAIN EXECUTION ====================

def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = QuizGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()