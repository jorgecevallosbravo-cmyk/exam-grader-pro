# Exam Grader Pro

A professional web-based tool for grading multiple-choice exams with intelligent answer parsing and flexible grading scales.

![Exam Grader Pro](https://via.placeholder.com/1200x600/0a0e27/00d4ff?text=Exam+Grader+Pro)

## Features

- ✅ **Smart Answer Parsing** - Accepts answers in any format (plain letters, numbered lists, punctuated sequences)
- 🎯 **Flexible Grading Scales** - Choose from 10-point, 100-point, 20-point, 5-point, or custom scales
- 📊 **Detailed Results** - Side-by-side comparison showing which questions were correct/incorrect
- 🎨 **Professional Design** - Modern dark theme with smooth animations
- 📱 **Responsive** - Works on desktop, tablet, and mobile devices
- ⚡ **Fast & Lightweight** - Pure HTML/CSS/JS, no dependencies

## Use Case

This tool is designed for educators who want to:
- Create PDF exams with 30-50 multiple-choice questions
- Upload one question to their LMS (like Moodle) instead of creating 50 individual questions
- Quickly grade student submissions by copy-pasting their answer strings
- Save hours of exam setup time while maintaining grading accuracy

## How It Works

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

## Supported Answer Formats

Students can submit answers in ANY of these formats:

```
ADCABCBA...                          ✓ Plain letters
1) A, 2) D, 3) C, 4) A...            ✓ Numbered with parentheses
1. A, 2. D, 3. C, 4. A...            ✓ Numbered with periods
A, D, C, A, B, C, B, A...            ✓ Comma-separated
A; D; C; A; B; C; B; A...            ✓ Semicolon-separated
```

The app automatically extracts only the letters and ignores formatting.

## Grading Scales

Choose from preset scales or define your own:

- **10-point scale** (Ecuador, many Latin American countries)
- **100-point scale** (USA, many universities)
- **20-point scale** (France, some European systems)
- **5-point scale** (Germany, some grading systems)
- **Custom** (enter any number 1-1000)

All grades display with exactly 2 decimal places (e.g., `8.67 / 10`).

## Installation

### Option 1: Direct Download
1. Download `index.html` from this repository
2. Open it in any modern web browser
3. Done! No installation required.

### Option 2: Host on GitHub Pages
1. Fork this repository
2. Go to Settings → Pages
3. Select main branch as source
4. Your app will be live at `https://yourusername.github.io/exam-grader-pro`

### Option 3: Self-Host
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/exam-grader-pro.git
   ```
2. Host the `index.html` file on any web server
3. Access via your domain

## Usage Example

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
- Final Grade: `8.67 / 10`
- Correct: 26
- Incorrect: 4
- Percentage: 86.67%

## Browser Support

- ✅ Chrome/Edge (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Opera
- ⚠️ Internet Explorer (not supported)

## Technologies Used

- HTML5
- CSS3 (with custom properties/variables)
- Vanilla JavaScript (no frameworks)
- Google Fonts: DM Sans, JetBrains Mono

## Contributing

Contributions are welcome! If you have suggestions for improvements:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## License

MIT License - feel free to use this tool for personal or commercial purposes.

## Author

**Jorge B. Cevallos**  
Academic Tutor & Instructor at ESPAM MFL

## Acknowledgments

Built to solve a real problem: reducing the administrative burden on educators while maintaining assessment quality.

---

**⭐ If this tool saves you time, please star the repository!**
