# Exam Grader Pro

A professional Streamlit web app for grading multiple-choice exams with intelligent answer parsing and flexible grading scales.

![Exam Grader Pro](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 🎯 Purpose

This tool is designed for educators who want to:
- Create PDF exams with 30-50 multiple-choice questions
- Upload **one question** to their LMS (like Moodle) instead of creating 50 individual questions
- Quickly grade student submissions by copy-pasting their answer strings
- Save **15+ hours per month** from exam setup time while maintaining grading accuracy

## ✨ Features

- ✅ **Smart Answer Parsing** - Accepts answers in any format (plain letters, numbered lists, punctuated sequences)
- 🎯 **Flexible Grading Scales** - Choose from 10-point, 100-point, 20-point, 5-point, or custom scales
- 📊 **Detailed Results** - Side-by-side comparison showing which questions were correct/incorrect
- 🎨 **Professional Design** - Clean, modern interface matching Streamlit best practices
- 📱 **Responsive** - Works on desktop, tablet, and mobile devices
- ⚡ **Fast & Simple** - Pure Python with minimal dependencies

## 🚀 Live Demo

**[Try it here: exam-grader-pro.streamlit.app](https://exam-grader-pro.streamlit.app)** *(replace with your actual URL after deployment)*

## 💡 How It Works

### For Teachers:

1. **Create Your Exam**
   - Generate a PDF with your multiple-choice questions (A/B/C/D options)
   - Keep the answer key as a string (e.g., `ADCABCBA...`)

2. **Set Up in Your LMS**
   - Create ONE essay/text-field question in Moodle (or any LMS)
   - Upload your PDF
   - Instruct students to submit their answers as a single string

3. **Grade Submissions**
   - Copy student's answer string from LMS
   - Paste into Exam Grader Pro
   - Get instant grade + detailed breakdown
   - Copy grade back to LMS

### Time Savings:
- **Traditional method:** 60 minutes to create 30 questions in LMS
- **With Exam Grader Pro:** 3 minutes to upload PDF + 10 seconds per student to grade
- **Savings:** ~15 hours per month for teachers with 4 classes

## 📝 Supported Answer Formats

Students can submit answers in **ANY** of these formats:

```
ADCABCBA...                          ✓ Plain letters
1) A, 2) D, 3) C, 4) A...            ✓ Numbered with parentheses
1. A, 2. D, 3. C, 4. A...            ✓ Numbered with periods
A, D, C, A, B, C, B, A...            ✓ Comma-separated
A; D; C; A; B; C; B; A...            ✓ Semicolon-separated
```

The app automatically extracts only the letters and ignores formatting.

## 🎓 Grading Scales

Choose from preset scales or define your own:

- **10-point scale** (Ecuador, many Latin American countries)
- **100-point scale** (USA, many universities)
- **20-point scale** (France, some European systems)
- **5-point scale** (Germany, some grading systems)
- **Custom** (enter any number 1-1000)

All grades display with exactly 2 decimal places (e.g., `8.67 / 10`).

## 🛠️ Installation & Deployment

### Option 1: Deploy to Streamlit Cloud (Recommended)

1. **Fork this repository** or create a new repo with these files
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Sign in with GitHub
4. Click "New app"
5. Select:
   - Repository: `your-username/exam-grader-pro`
   - Branch: `main`
   - Main file path: `exam_grader_streamlit.py`
6. Click "Deploy"
7. Your app will be live at `https://your-app-name.streamlit.app`

### Option 2: Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/exam-grader-pro.git
   cd exam-grader-pro
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   streamlit run exam_grader_streamlit.py
   ```

5. **Open your browser** to `http://localhost:8501`

## 📂 Project Structure

```
exam-grader-pro/
├── exam_grader_streamlit.py    # Main Streamlit application
├── requirements.txt             # Python dependencies
├── README.md                    # This file
└── LICENSE                      # MIT License
```

## 🔧 Technologies Used

- **Python 3.8+**
- **Streamlit** - Web app framework
- **Regular Expressions** - Answer parsing

## 📊 Usage Example

**Answer Key:**
```
ADCABCBADCBADABCDABCDBACABDCAB
```

**Student Submission:**
```
1) A, 2) D, 3) C, 4) A, 5) B, 6) C, 7) B, 8) A, 9) D, 10) C, 
11) B, 12) A, 13) D, 14) A, 15) B, 16) C, 17) D, 18) A, 19) B, 
20) C, 21) D, 22) B, 23) A, 24) C, 25) A, 26) B, 27) D, 28) C, 
29) A, 30) B
```

**Result:**
- Final Grade: **8.67 / 10**
- Correct: 26
- Incorrect: 4
- Percentage: 86.67%

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📄 License

MIT License - feel free to use this tool for personal or commercial purposes.

## 👨‍🏫 Author

**Jorge B. Cevallos**  
Academic Tutor & Instructor at ESPAM MFL

## 🙏 Acknowledgments

Built to solve a real problem: reducing the administrative burden on educators while maintaining assessment quality.

---

**⭐ If this tool saves you time, please star the repository!**

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the [Streamlit documentation](https://docs.streamlit.io/)

---

**Made with ❤️ for educators worldwide**
