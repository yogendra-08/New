# 🎯 Digital Quiz App with Stats

A desktop quiz application that fetches live questions from Open Trivia Database API and provides detailed performance statistics using advanced statistical analysis.

---

## 📋 Project Overview

This is a mini college project that demonstrates integration of external APIs, GUI development, data management, and statistical analysis in Python.

**Features:**
- 🌐 Live quiz questions from Open Trivia Database API
- 🎮 Interactive GUI built with Tkinter
- 📊 Performance statistics (Mean, Median, Mode, Standard Deviation)
- 💾 Quiz history storage using Pandas
- 📈 Track progress over multiple quiz attempts

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.x** | Core programming language |
| **Tkinter** | GUI framework for quiz interface |
| **Requests** | HTTP library to fetch questions from API |
| **Pandas** | Data storage and management |
| **SciPy** | Statistical calculations (mean, median, mode) |
| **NumPy** | Numerical operations and array handling |

---

## 📁 Project Structure

```
digital-quiz-app/
│
├── main.py                 # Entry point - Main menu GUI
├── quiz_app.py            # Quiz logic and API integration
├── stats_manager.py       # Statistical analysis using SciPy
├── data/
│   └── quiz_history.csv   # Stores quiz attempts (auto-generated)
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Internet connection (for API calls)

### Step 1: Clone or Download Project
```bash
cd digital-quiz-app
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python main.py
```

---

## 📦 Dependencies

Install all required packages:
```bash
pip install requests pandas scipy numpy
```

Or use the requirements.txt file:
```bash
pip install -r requirements.txt
```

---

## 🎮 How to Use

1. **Launch Application**
   - Run `python main.py`
   - Main menu will appear

2. **Start Quiz**
   - Click "Start Quiz" button
   - Select category, difficulty, and number of questions
   - Answer questions one by one
   - View your score at the end

3. **View Statistics**
   - Click "View Statistics" button
   - See your performance metrics:
     - Mean Score
     - Median Score
     - Mode Score
     - Standard Deviation
     - Total Quizzes Taken
     - Overall Accuracy

4. **Exit**
   - Click "Exit" to close the application

---

## 📊 Statistical Features

The app uses **SciPy** to calculate:

- **Mean Score**: Average score across all attempts
- **Median Score**: Middle value of all scores
- **Mode Score**: Most frequently achieved score
- **Standard Deviation**: Measure of score consistency
- **Accuracy**: Overall percentage of correct answers

---

## 🌐 API Information

**API Used:** Open Trivia Database
- **URL:** https://opentdb.com/api.php
- **Documentation:** https://opentdb.com/api_config.php
- **Free to use, no API key required**

**Available Categories:**
- General Knowledge
- Science & Nature
- Computers
- Mathematics
- Sports
- Geography
- History
- And many more...

**Difficulty Levels:**
- Easy
- Medium
- Hard

---

## 💾 Data Storage

Quiz results are stored in `data/quiz_history.csv` with the following columns:
- Date & Time
- Category
- Difficulty
- Total Questions
- Correct Answers
- Score (%)
- Time Taken

---

## 🎓 Learning Outcomes

This project demonstrates:
1. ✅ API integration with external services
2. ✅ GUI development using Tkinter
3. ✅ Data management with Pandas
4. ✅ Statistical analysis with SciPy
5. ✅ File I/O operations
6. ✅ Error handling and validation
7. ✅ Object-oriented programming

---

## 🐛 Troubleshooting

**Issue:** Module not found error
- **Solution:** Install dependencies using `pip install -r requirements.txt`

**Issue:** API connection error
- **Solution:** Check your internet connection

**Issue:** CSV file not found
- **Solution:** The file is auto-created on first quiz completion

---

## 📝 Future Enhancements

- 🔹 Add timer for each question
- 🔹 Multiplayer mode
- 🔹 Leaderboard system
- 🔹 Export statistics as PDF
- 🔹 Add more visualization (graphs/charts)
- 🔹 Custom question sets

---

---

## 📄 License

This project is created for educational purposes as a college mini project.

---

## 🙏 Acknowledgments

- Open Trivia Database for providing free quiz API
- Python community for excellent libraries
- Preeti Mam for project guidance

---

## 📞 Contact

For any queries or suggestions:
- Email: [yogendradbhange@gmail.com]
- GitHub: [yogendra-08]

---

**Happy Quizzing! 🎉**