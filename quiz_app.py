"""
quiz_app.py - Handles API calls and quiz logic
"""

import requests
import html
import random
from datetime import datetime

class QuizApp:
    """Main Quiz Application Class"""
    
    def __init__(self):
        self.api_url = "https://opentdb.com/api.php"
        self.questions = []
        self.current_question_index = 0
        self.score = 0
        self.user_answers = []
        self.quiz_category = ""
        self.quiz_difficulty = ""
        self.start_time = None
        
    def fetch_questions(self, amount=10, category=None, difficulty=None):
        """
        Fetch questions from Open Trivia Database API
        
        Args:
            amount (int): Number of questions (1-50)
            category (int): Category ID (optional)
            difficulty (str): 'easy', 'medium', or 'hard' (optional)
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Build API parameters
            params = {
                'amount': amount,
                'type': 'multiple'  # Multiple choice questions
            }
            
            if category:
                params['category'] = category
                
            if difficulty:
                params['difficulty'] = difficulty.lower()
            
            # Make API request
            response = requests.get(self.api_url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Check if questions were returned
            if data['response_code'] == 0:
                self.questions = data['results']
                self.current_question_index = 0
                self.score = 0
                self.user_answers = []
                self.start_time = datetime.now()
                
                # Decode HTML entities and shuffle options
                for question in self.questions:
                    question['question'] = html.unescape(question['question'])
                    question['correct_answer'] = html.unescape(question['correct_answer'])
                    question['incorrect_answers'] = [html.unescape(ans) for ans in question['incorrect_answers']]
                    
                    # Combine and shuffle all answers
                    all_answers = question['incorrect_answers'] + [question['correct_answer']]
                    random.shuffle(all_answers)
                    question['all_answers'] = all_answers
                
                return True
            else:
                print(f"API Error: Response code {data['response_code']}")
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"Network Error: {e}")
            return False
        except Exception as e:
            print(f"Error fetching questions: {e}")
            return False
    
    def get_current_question(self):
        """
        Get the current question
        
        Returns:
            dict: Current question data or None
        """
        if 0 <= self.current_question_index < len(self.questions):
            return self.questions[self.current_question_index]
        return None
    
    def check_answer(self, user_answer):
        """
        Check if the user's answer is correct
        
        Args:
            user_answer (str): User's selected answer
        
        Returns:
            bool: True if correct, False otherwise
        """
        current_q = self.get_current_question()
        if current_q:
            is_correct = user_answer == current_q['correct_answer']
            
            # Store user answer
            self.user_answers.append({
                'question': current_q['question'],
                'user_answer': user_answer,
                'correct_answer': current_q['correct_answer'],
                'is_correct': is_correct
            })
            
            if is_correct:
                self.score += 1
            
            return is_correct
        return False
    
    def next_question(self):
        """
        Move to the next question
        
        Returns:
            bool: True if there are more questions, False if quiz is complete
        """
        self.current_question_index += 1
        return self.current_question_index < len(self.questions)
    
    def get_progress(self):
        """
        Get current progress
        
        Returns:
            tuple: (current_question_number, total_questions)
        """
        return (self.current_question_index + 1, len(self.questions))
    
    def calculate_percentage(self):
        """
        Calculate score percentage
        
        Returns:
            float: Score percentage
        """
        if len(self.questions) > 0:
            return (self.score / len(self.questions)) * 100
        return 0.0
    
    def get_quiz_summary(self):
        """
        Get complete quiz summary
        
        Returns:
            dict: Summary with all quiz details
        """
        end_time = datetime.now()
        time_taken = (end_time - self.start_time).total_seconds() if self.start_time else 0
        
        return {
            'date': end_time.strftime('%Y-%m-%d %H:%M:%S'),
            'category': self.quiz_category,
            'difficulty': self.quiz_difficulty,
            'total_questions': len(self.questions),
            'correct_answers': self.score,
            'incorrect_answers': len(self.questions) - self.score,
            'score_percentage': self.calculate_percentage(),
            'time_taken_seconds': int(time_taken),
            'user_answers': self.user_answers
        }
    
    def reset_quiz(self):
        """Reset quiz for a new attempt"""
        self.questions = []
        self.current_question_index = 0
        self.score = 0
        self.user_answers = []
        self.start_time = None
    
    @staticmethod
    def get_categories():
        """
        Get available quiz categories
        
        Returns:
            dict: Category ID and names
        """
        return {
            'Any Category': None,
            'General Knowledge': 9,
            'Books': 10,
            'Film': 11,
            'Music': 12,
            'Musicals & Theatres': 13,
            'Television': 14,
            'Video Games': 15,
            'Board Games': 16,
            'Science & Nature': 17,
            'Computers': 18,
            'Mathematics': 19,
            'Mythology': 20,
            'Sports': 21,
            'Geography': 22,
            'History': 23,
            'Politics': 24,
            'Art': 25,
            'Celebrities': 26,
            'Animals': 27,
            'Vehicles': 28,
            'Comics': 29,
            'Gadgets': 30,
            'Anime & Manga': 31,
            'Cartoon & Animations': 32
        }
    
    @staticmethod
    def get_difficulties():
        """
        Get available difficulty levels
        
        Returns:
            list: Difficulty levels
        """
        return ['Any Difficulty', 'Easy', 'Medium', 'Hard']


# Test the class
if __name__ == "__main__":
    print("Testing QuizApp class...")
    
    quiz = QuizApp()
    
    # Test fetching questions
    print("\n1. Fetching 5 easy questions from General Knowledge...")
    if quiz.fetch_questions(amount=5, category=9, difficulty='easy'):
        print(f"✓ Successfully fetched {len(quiz.questions)} questions")
        
        # Display first question
        q = quiz.get_current_question()
        if q:
            print(f"\nSample Question:")
            print(f"Q: {q['question']}")
            print(f"Options: {q['all_answers']}")
            print(f"Correct Answer: {q['correct_answer']}")
    else:
        print("✗ Failed to fetch questions")
    
    # Test categories
    print(f"\n2. Available Categories: {len(quiz.get_categories())}")
    
    # Test difficulties
    print(f"3. Available Difficulties: {quiz.get_difficulties()}")
    
    print("\n✓ QuizApp class is working correctly!")